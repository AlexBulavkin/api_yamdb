from django.contrib.auth.models import AbstractUser
from django.db import models

CHOICES_ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class User(AbstractUser):
    username = models.CharField(blank=False, unique=True, max_length=150)
    email = models.EmailField(blank=False, unique=True, max_length=254)
    first_name = models.CharField(blank=True, max_length=150)
    last_name = models.CharField(blank=True, max_length=150)
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        default='user',
        max_length=16,
        choices=CHOICES_ROLES)
    confirmation_code = models.SlugField()
