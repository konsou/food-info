import tempfile

from django.core.exceptions import ValidationError
from django.http import (
    HttpResponseRedirect,
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response

from ..barcode import read_barcode, validate_ean
from ..fetch_info import fetch_item_info
from ..forms import FoodItemForm, UploadEANImageForm
from ..serializers import FoodItemSerializer


def new_food_item(request: HttpRequest) -> HttpResponse:
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


@api_view(["POST"])
def food_item_from_image(request: Request) -> Response:
    form_image = UploadEANImageForm(request.POST, request.FILES)
    if not form_image.is_valid():
        return Response(status=400)

    with tempfile.NamedTemporaryFile() as tmp:
        for chunk in form_image.cleaned_data["image"].chunks():
            tmp.write(chunk)
        try:
            ean = read_barcode(tmp.name)
            validate_ean(ean)
        except (ValueError, OSError, ValidationError):
            return Response(status=400)

    food_item = fetch_item_info(ean)
    food_item.save()
    serializer = FoodItemSerializer(food_item)
    json = JSONRenderer().render(serializer.data)

    return Response(data=json)
