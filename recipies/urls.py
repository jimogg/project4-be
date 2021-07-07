from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, ChefViewSet

router = DefaultRouter()

router.register(r'recipes', RecipeViewSet,  basename='recipe')
router.register(r'chefs', ChefViewSet, basename='chef')

urlpatterns = router.urls
