from django.db.models.query import QuerySet
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.User
        fields = ('id', 'email', 'username', 'password', 'avatar')


class RecipeSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(
        source='author',
        read_only=True,
    )

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=models.User.objects.all(),
    )

    class Meta(UserCreateSerializer.Meta):
        model = models.Recipe
        fields = '__all__'
        # fields = ('id', 'title', 'subtitle', 'intro',
        #           'steps', 'summary', 'likes', 'comments')
