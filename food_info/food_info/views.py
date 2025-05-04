import tempfile

from django.core.exceptions import ValidationError
from django.http import (
    HttpResponseRedirect,
    HttpRequest,
    HttpResponseNotAllowed,
    HttpResponse,
    JsonResponse,
    HttpResponseBadRequest,
)
from django.shortcuts import render
from django.views.generic import ListView

from .barcode import read_barcode, validate_ean
from .fetch_info import fetch_nutrition_info
from .forms import FoodItemForm, UploadEANImageForm
from .models import FoodItem


class FoodItemListView(ListView):
    model = FoodItem
    template_name = "food-item-list.html"


def new_food_item(request: HttpRequest):
    if request.method == "POST":
        form = FoodItemForm(request.POST, request.FILES)
        form_image = UploadEANImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    else:
        form = FoodItemForm()
        form_image = UploadEANImageForm()

    return render(
        request,
        "new-food-item.html",
        {
            "form": form,
            "form_image": form_image,
        },
    )


def food_info_from_image(request: HttpRequest) -> HttpResponse:
    if not request.method == "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])

    form_image = UploadEANImageForm(request.POST, request.FILES)
    if not form_image.is_valid():
        return HttpResponseBadRequest()

    with tempfile.NamedTemporaryFile() as tmp:
        for chunk in form_image.cleaned_data["image"].chunks():
            tmp.write(chunk)
        try:
            ean = read_barcode(tmp.name)
            validate_ean(ean)
        except (ValueError, OSError, ValidationError):
            return HttpResponseBadRequest()

    nutrition_info = fetch_nutrition_info(ean)._asdict()
    nutrition_info["ean"] = ean

    return JsonResponse(nutrition_info)
