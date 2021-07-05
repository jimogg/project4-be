from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, AuthorViewSet

router = DefaultRouter()

router.register(r'recipes', RecipeViewSet,  basename='book')
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = router.urls
