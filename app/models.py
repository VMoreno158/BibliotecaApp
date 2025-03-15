from django.db import models
from django.core.exceptions import ValidationError

class Library(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

class Book(models.Model):
    GENRE_CHOICES = [
    ('fiction', 'fiction'),
    ('non_fiction', 'non_fiction'),
    ('fantasy', 'fantasy'),
    ('science_fiction', 'science_fiction'),
    ('mystery_thriller', 'mystery_thriller'),
    ('romance', 'romance'),
    ('horror', 'horror'),
    ('history', 'history'),
    ('biography_memoir', 'biography_memoir'),
    ('philosophy', 'philosophy'),
    ('self_help', 'self_help'),
    ('science_technology', 'science_technology')
    ]

    LANGUAGE_CHOICES = [
        ('spanish', 'spanish'),
        ('english', 'english'),
        ('others', 'others')
    ]

    FORMAT_CHOICES = [
        ('ebook', 'ebook'),
        ('physical', 'physical'),
        ('audiobook', 'audiobook')
    ]

    AGE_RANGE_CHOICES = [
        ('children', 'children'),
        ('young_adult', 'young_adult'),
        ('adult', 'adult')
    ]

    isbn = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=50, blank=False, null=False)
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
