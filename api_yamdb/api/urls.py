from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('genres', views.GenreViewSet, basename='genre')
router.register('titles', views.TitleViewSet, basename='title')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', views.registration, name='signup'),
    path(
        'auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
]
