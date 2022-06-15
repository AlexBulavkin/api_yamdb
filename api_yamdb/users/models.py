from django.contrib.auth.models import AbstractUser
from django.db import models

CHOICES_ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class User(AbstractUser):
    role = models.CharField(max_length=16, choices=CHOICES_ROLES)
    bio = models.TextField(
        'Биография',
        blank=True,
    )
