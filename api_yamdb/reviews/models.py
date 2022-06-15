from django.db import models


class Category(models.Model):
    slug = models.SlugField(unique=True, max_length=50,)
    pass


class Genre(models.Model):
    pass


class Title(models.Model):
    pass


class GenreTitle(models.Model):
    pass


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
