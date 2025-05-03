from django.views.generic import ListView
from .models import FoodItem


class FoodItemListView(ListView):
    model = FoodItem