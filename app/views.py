from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Library, Book, Loan, User

@csrf_exempt
def libraries(request): # get_libraries and add_library
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            library = Library(
                name = data['name'],
                location = data['location']
            )
            library.full_clean()
            library.save()

            return JsonResponse({"message": "Library successfully registered", "library.id": library.id})
        
        except KeyError:
            return JsonResponse({"error": "Incomplete fields"}, status=400)
        
    if request.method == 'GET':
        libraries = list(Library.objects.all().values())
        return JsonResponse(libraries, safe=False)
    
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def get_library_id(request, library_id):
    if request.method == 'GET':
        try:
            library = Library.objects.values().get(id=library_id)
            return JsonResponse(library)
        
        except Library.DoesNotExist:
            return JsonResponse({"error": "Library not found"}, status=404)
    
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)    
            library_found = Library.objects.get(id=data['library_id'])

            book = Book(
                isbn = data['isbn'],
                title = data['title'],
                genre = data['genre'].lower(),
                language = data['language'].lower(),
                author = data['author'],
                editorial = data['editorial'],
                format = data['format'].lower(),
                age_range = data['age_range'].lower(),
                library = library_found
            )
            book.full_clean()
            book.save()

            return JsonResponse({"message": "Book successfully registered", "book.id": book.id})
        
        except Library.DoesNotExist:
            return JsonResponse({"error": "Library not found"}, status=404)
        
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def get_books_library(request, library_id):
    if request.method == 'GET':
        try:
            filter = request.GET.get('filter')
            library_find = Library.objects.get(id=library_id)

            if(filter == 'available'):
                books_library = list(Book.objects.filter(library=library_find)
                                     .exclude(id__in=Loan.objects.filter(returned=False)
                                            .values_list("book_id", flat=True))
                                     .values("id", "isbn", "title", "genre", "language",
                                            "author", "editorial","format", "age_range"))

            else:
                books_library = list(Book.objects.filter(library=library_find)
                                     .values("id", "isbn", "title", "genre", 
                                            "language", "author", "editorial", 
                                            "format", "age_range"))

            response = {
                "library": {
                    "id": library_find.id,
                    "name": library_find.name,
                    "location": library_find.location
                },
                "books": books_library
            }

            return JsonResponse(response, safe=False)
        
        except Library.DoesNotExist:
            return JsonResponse({"error": "Library not found"}, status=404)
        
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def books(request, book_id): # get_book and update_book
    if request.method == 'GET':
        try:
            book = Book.objects.values().get(id=book_id)
            return JsonResponse(book)
        
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
        
    if request.method in ['PUT', 'PATCH']:
        try:
            book = Book.objects.get(id=book_id)
            data = json.loads(request.body)

            book.title = data['title']
            book.genre = data['genre'].lower()
            book.language = data['language'].lower()
            book.author = data['author']
            book.editorial = data['editorial']
            book.format = data['format'].lower()
            book.age_range = data['age_range'].lower()
            book.full_clean()
            book.save()

            return JsonResponse({"message": "Book updated successfully", "book_id": book.id}, status=201)
        
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Incomplete fields"}, status=400)

    if request.method == 'DELETE':
        try:
            Book.objects.get(id=book_id).delete()
            return JsonResponse({"message": "Book deleted successfully"}, status=200)
        
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
        
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def users(request): # add_user and get_users
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User(
                dni = data['dni'],
                email = data['email'],
                name = data['name'],
                surname = data['surname'],
                birthdate = data['birthdate']
            )
            user.full_clean()
            user.save()

            return JsonResponse({"message": "User successfully registered", "user.id": user.id})
        
        except KeyError:
            return JsonResponse({"error": "Incomplete fields"}, status=400)
        
    if request.method == 'GET':
        users = list(User.objects.all().values())
        return JsonResponse(users, safe=False)
    
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def get_user_id(request, user_id):
    if request.method == 'GET':
        try:
            user = User.objects.values().get(id=user_id)
            return JsonResponse(user)
        
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
    
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def loans(request): # add_loan and get_loans
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_found = User.objects.get(id=data['user_id'])
            book_found = Book.objects.get(id=data['book_id'])

            existing_loan = Loan.objects.filter(book=book_found).exists()
            if existing_loan:
                return JsonResponse({"error": "This book is already loaned out"}, status=400)

            loan = Loan.objects.create(
                book = book_found,
                user = user_found
            )

            return JsonResponse({"message": "Loan successfully registered", "loan.id": loan.id})
        
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Book.DoesNotExist:
            return JsonResponse({"error": "Book not found"}, status=404)
        except KeyError:
            return JsonResponse({"error": "Incomplete fields"}, status=400)

    if request.method == 'GET':
        loans = list(Loan.objects.all().values())
        return JsonResponse(loans, safe=False)
    
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def get_loans_user(request, user_id):
    if request.method == 'GET':
        try:
            user_find = User.objects.get(id=user_id)
            loans = Loan.objects.filter(user=user_find).select_related('book')

            books_user = list(loans.values(
                "id", "isbn", "title", "genre", "language", "author", "editorial", "format", "age_range"
            ))

            response = {
                "user": {
                    "dni": user_find.dni,
                    "name": user_find.name,
                    "surname": user_find.surname
                },
                "books": books_user
            }
            return JsonResponse(response, safe=False)
        
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"})
        
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def update_loan_returned(request, loan_id):
    if request.method == 'PUT':
        try:
            loan = Loan.objects.get(id=loan_id)
            if(loan.returned):
                return JsonResponse({"message": "Book already returned"})

            loan.returned = True
            loan.save()
            return JsonResponse({"message": "Loan changed to returned"})

        except Loan.DoesNotExist:
            return JsonResponse({"error": "Loan not found"})
        
    return JsonResponse({"error": "Invalid method"}, status=405)




