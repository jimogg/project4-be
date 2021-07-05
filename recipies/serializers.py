from rest_framework import serializers
from .models import Recipe, Author


class RecipeSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(
        source='author',
        read_only=True,
    )

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
    )

    class Meta:
        model = Recipe
        fields = '__all__'
        # fields = ('id', 'title', 'subtitle', 'intro',
        #           'steps', 'summary', 'likes', 'comments')
