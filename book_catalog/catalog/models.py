from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True, default='')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, default=None)
    published = models.DateField(null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'



class LookupBookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.book.title}, {self.genre.name}'


class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birth_date = models.DateTimeField(null=True, blank=True)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} {self.surname}'



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    rating = models.PositiveIntegerField(
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    created =  models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'Review by {self.author}: {self.surname}'



class Favorite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)






