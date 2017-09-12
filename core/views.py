from rest_framework import permissions, mixins, viewsets

from . import models
from . import serializers


class RecipeViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = serializers.RecipeDetailSerializer
    queryset = models.Recipe.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeSerializer

        return super().get_serializer_class()
