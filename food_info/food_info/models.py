from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    ean = models.IntegerField()
    price = models.FloatField()
    weight = models.FloatField(help_text="Weight in grams")
    carbs_per_100g = models.FloatField()
    protein_per_100g = models.FloatField()
    fat_per_100g = models.FloatField()
    kcal_per_100g = models.FloatField()

    def __str__(self):
        return f"{self.name} {int(self.weight)} g"

    @property
    def price_per_100g_carbs(self) -> float:
        carbs_in_package = self.weight / 100 * self.carbs_per_100g
        price_per_1g_carb = self.price / carbs_in_package
        return price_per_1g_carb * 100