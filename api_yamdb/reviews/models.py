from unicodedata import category
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=50)


class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name='Жанр')
    slug = models.SlugField(unique=True, max_length=50)


class Title(models.Model):
    name = models.CharField(max_length=50, unique=True)
    year = models.DateTimeField(verbose_name='Дата выхода фильма',)
    description = models.TextField(
        max_length=300,
        verbose_name='Описание фильма'
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL
    )


class GenreTitle(models.Model):
    pass


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
