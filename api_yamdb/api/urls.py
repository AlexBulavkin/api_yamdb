from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register('categories', views.CategoryViewSet, basename='category')
router.register('genres', views.GenreViewSet, basename='genre')
router.register('titles', views.TitleViewSet, basename='title')
router.register(
    r'^titles/(?P<title_id>[\d+]+)/reviews',
    views.ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>[\d+]+)/reviews/(?P<review_id>[\d+]+)/comments',
    views.CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/signup/', views.registration, name='signup'),
    path('auth/token/', views.get_jwt_token, name='token'),
]
