from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('email/', views.email, name='email'),  # временный эксперимент с почтой
    path('', include(router.urls)),
    path(
        'auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
]
