from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ..forms import UploadEANImageForm
from ..models import FoodItem


def food_item_list(request: HttpRequest) -> HttpResponse:
    items = FoodItem.objects.all()
    photo_form = UploadEANImageForm()
    return render(
        request, "food-item-list.html", {"object_list": items, "photo_form": photo_form}
    )
