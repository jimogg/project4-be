from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe, Author
from .serializers import RecipeSerializer, AuthorSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
