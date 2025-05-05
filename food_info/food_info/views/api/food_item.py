from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response

from ...models import FoodItem
from ...serializers import FoodItemSerializer


class ListFoodItems(APIView):
    serializer_class = FoodItemSerializer

    def get(self, request: Request) -> Response:
        items = FoodItem.objects.all()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)
