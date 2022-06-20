from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """ Менеджер для User """

    def create_user(self, username, email, password=None, role='', bio=''):
        """ Создает и возвращает пользователя с имэйлом и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            role=role,
            bio=bio)
        user.save()
        return user

    def create_superuser(self, username, email, password, role='', bio=''):
        """ Создает и возввращает пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password, role, bio)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


CHOICES_ROLES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class User(AbstractUser):
    " Кастомная модель User"
    username = models.CharField(
        db_index=True,
        blank=False,
        unique=True,
        max_length=150)
    email = models.EmailField(
        db_index=True,
        blank=False,
        unique=True,
        max_length=254)
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
    confirmation_code = models.SlugField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ['-id']
