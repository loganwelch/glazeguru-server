from django.db import models


class GlazeIngredient(models.Model):
    glaze = models.ForeignKey(Glaze, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
