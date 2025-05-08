import base64
import tempfile

from django.core.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from ...barcode import read_barcode, validate_ean
from ...fetch_info import fetch_item_info
from ...models import FoodItem
from ...serializers import FoodItemSerializer


class FoodItemViewSet(ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class FoodItemFromImage(APIView):
    def post(self, request: Request, *args, **kwargs):
        file = base64.b64decode(request.data["file"])
        with tempfile.NamedTemporaryFile() as tmp:
            tmp.write(file)
            try:
                ean = read_barcode(tmp.name)
                validate_ean(ean)
            except (ValueError, OSError, ValidationError):
                return Response(status=400)

        already_existing_item = FoodItem.objects.filter(ean=ean)[0]
        if already_existing_item:
            return Response(
                {"error": f"{already_existing_item.name} already exists"}, status=400
            )

        food_item = fetch_item_info(ean)
        food_item.save()

        serializer = FoodItemSerializer(food_item)
        json = JSONRenderer().render(serializer.data)

        return Response(data=json)
