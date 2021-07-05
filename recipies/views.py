from django.shortcuts import render
from rest_framework import viewsets
from .models import Recipe, Chef
from .serializers import RecipeSerializer, ChefSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ChefViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer
