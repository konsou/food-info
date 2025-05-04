from django.forms import ModelForm, ImageField, Form

from .models import FoodItem


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = "__all__"


class UploadEANImageForm(Form):
    image = ImageField()
