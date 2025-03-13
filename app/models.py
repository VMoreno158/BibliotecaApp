from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('science_fiction', 'Science Fiction'),
        ('mystery_thriller', 'Mystery/Thriller'),
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('history', 'History'),
        ('biography_memoir', 'Biography/Memoir'),
        ('philosophy', 'Philosophy'),
        ('self_help', 'Self-Help'),
        ('science_technology', 'Science & Technology'),
    ]

    LANGUAGE_CHOICES = [
        ('spanish', 'Spanish'),
        ('english', 'English'),
        ('others', 'Others'),
    ]

    FORMAT_CHOICES = [
        ('ebook', 'eBook'),
        ('physical', 'Physical Book'),
        ('audiobook', 'AudioBook'),
    ]

    AGE_RANGE_CHOICES = [
        ('children', 'Children'),
        ('young_adult', 'Young Adult'),
        ('adult', 'Adult'),
    ]
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)  
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)  
    author = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    format = models.CharField(max_length=15, choices=FORMAT_CHOICES)
    age_range = models.CharField(max_length=15, choices=AGE_RANGE_CHOICES)
    library = models.ForeignKey('Library', on_delete=models.CASCADE, related_name='books')

class User(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    email = models.CharField(max_length=100)
    telf_number = models.CharField(max_length=9)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    birthdate = models.DateField()

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    date = models.DateField(auto_now_add=True)
    returned = models.BooleanField(default=False)
