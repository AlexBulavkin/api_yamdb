from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(unique=True, max_length=50)


class Genre(models.Model):
    name = models.TextField(max_length=50, verbose_name='Жанр')
    slug = models.SlugField(unique=True, max_length=50)


class Title(models.Model):
    pass


class GenreTitle(models.Model):
    pass


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
