from rest_framework import serializers

from .models import FoodItem


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = [
            "name",
            "weight",
            "ean",
            "price",
            "kcal_per_100g",
            "fat_per_100g",
            "carbs_per_100g",
            "protein_per_100g",
            "price_per_100g_protein",
            "price_per_1000_kcal",
        ]
