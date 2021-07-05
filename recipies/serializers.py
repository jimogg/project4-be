from rest_framework import serializers
from .models import Recipe, Chef


class RecipeSerializer(serializers.ModelSerializer):
    chef_name = serializers.StringRelatedField(
        source='chef',
        read_only=True,
    )

    chef_id = serializers.PrimaryKeyRelatedField(
        queryset=Chef.objects.all(),
        source='chef',
    )

    class Meta:
        model = Recipe
        fields = '__all__'
        # fields = ('id', 'title', 'subtitle', 'intro',
        #           'steps', 'summary', 'likes', 'comments')


class ChefSerializer(serializers.ModelSerializer):
    recipies = RecipeSerializer(many=True, read_only=True,)

    class Meta:
        model = Chef
        fields = ('name', 'recipies',)
