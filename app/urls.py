from django.urls import path
from . import views

urlpatterns=[
    path('libraries', views.libraries, name='libraries'), # POST & GET /libraries
    path('libraries/<int:library_id>', views.get_library_id, name='get_library_id'), # GET /libraries/{id}
    
    path('books', views.add_book, name="add_book"), # POST /books/
    path('libraries/<int:library_id>/books', views.get_books_library, name='get_books_library'), # GET /libraries/{id}/books/
    path('books/<int:book_id>', views.books, name="books"), # GET && ( PUT || PATCH ) && DELETE /books/{id}/

    path('users', views.users, name="users"), # POST && GET /users/
    path('users/<int:user_id>', views.get_user_id, name="get_user_id"), # GET /users/{id}/

    path('loans', views.loans, name="loans"), # POST && GET /loans/
    path('users/<int:user_id>/loans', views.get_loans_user, name="get_loans_user"), # GET /users/{id}/loans/
    path('loans/<int:loan_id>', views.update_loan_returned, name="update_loan_returned") # PUT /loans/{id}/ (update to returned)
]
