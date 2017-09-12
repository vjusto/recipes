from rest_framework import serializers
from . import models


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ('id', 'picture', 'title', 'preparation_time',)


class RecipeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = ('id', 'picture', 'title', 'preparation_time', 'ingredients', 'instructions')
