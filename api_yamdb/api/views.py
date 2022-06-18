import random
import string

from django.core.mail import send_mail
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from reviews.models import Category, Genre, Title, Review, Comment
from users.models import User
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleSerializer,
                          UserSerializer,
                          AuthUserSerializer
                          )
from .mixins import CreateListDestroyViewSet
from .filters import TitleFilter


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


@api_view(['POST'])
def registration(request):
    CONFIRMATION_CODE_LEN = 8
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    confirmation_code = (
        ''.join(random.choice(allowed_chars) for _ in range(
            CONFIRMATION_CODE_LEN))
    )
    serializer = AuthUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(confirmation_code=confirmation_code)
        user_email = serializer.data['email']
        send_mail(
            'Welcome to YAMDB',
            f'your confirmation code: {confirmation_code}',
            'yamdb@yamdb.com',  # from
            [user_email],  # to
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass


class CategoryViewSet(CreateListDestroyViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # permission_classes =     "Просмотр доступен для всех пользователей, удаление - Админ"
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CreateListDestroyViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    # permission_classes =     "Просмотр доступен для всех пользователей, удаление - Админ"
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    # permission_classes =     "Просмотр доступен для всех пользователей, частичное обновление инфы и удаление - Админ"
    filter_backends = (TitleFilter,)
