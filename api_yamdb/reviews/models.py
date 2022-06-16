from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50,)
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(max_length=50,)
    slug = models.SlugField(unique=True, max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(max_length=50, unique=True)
    year = models.PositiveSmallIntegerField(verbose_name='Дата выхода фильма',)
    description = models.TextField(
        max_length=300,
        verbose_name='Описание фильма'
    )
    rating = models.PositiveSmallIntegerField(null=True,)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Тип произведения'
        verbose_name_plural = 'Тип произведений'


class GenreTitle(models.Model):
    pass


class Review(models.Model):
    pass


class Comment(models.Model):
    pass
