import random
import string

from django.http import HttpResponse
from django.core.mail import send_mail

# from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, mixins, filters

#from reviews.models import Review, Comment
from users.models import User
from .serializers import (UserSerializer)


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class UserViewSet(CreateListViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


def email(request):

    CONFIRMATION_CODE_LEN = 8

    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    confirmation_code = (
        ''.join(random.choice(allowed_chars) for _ in range(
            CONFIRMATION_CODE_LEN))
    )

    send_mail(
        'Welcome',
        f'your confirmation code: {confirmation_code}',
        'from@example.com',   # Это поле "От кого"
        ['to@example.com'],   # Это поле "Кому" (можно указать список адресов)
    )
    return HttpResponse('check your mailbox')


class ReviewViewSet(viewsets.ModelViewSet):
    pass


class CommentViewSet(viewsets.ModelViewSet):
    pass
