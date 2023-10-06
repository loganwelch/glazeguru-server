from django.db import models


class Glaze(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='created_glazes')
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='GlazeIngredient')
