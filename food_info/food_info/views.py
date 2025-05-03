from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView

from .forms import FoodItemForm
from .models import FoodItem


class FoodItemListView(ListView):
    model = FoodItem

def new_food_item(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = FoodItemForm()

    return render(request, "new-food-item.html", {"form": form})