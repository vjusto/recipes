import json

from django.db import models


class Recipe(models.Model):
    picture = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    preparation_time = models.IntegerField()
    ingredients_list = models.TextField(default='[]')
    instructions_list = models.TextField(default='[]')

    @property
    def ingredients(self):
        return json.loads(self.ingredients_list)

    @property
    def instructions(self):
        return json.loads(self.instructions_list)
