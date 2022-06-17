from unicodedata import name
from rest_framework import serializers

from reviews.models import Category, Genre, Title

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели User."""

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        required_fields = ('username', 'email')


class ReviewSerializer(serializers.ModelSerializer):
    pass


class CommentSerializer(serializers.ModelSerializer):
    pass


class CategorySerializer(serializers.ModelSerializer):
    """Сериалайзер модели Category"""

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Genre"""

    class Meta:
        model = Genre
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Title"""
    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    genre = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
        many=True
    )

    class Meta:
        model = Title
        fields = '__all__'
        required_fields = ('name',)
