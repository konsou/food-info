import tempfile

from django.core.exceptions import ValidationError
from django.forms import ModelForm, ImageField

from .barcode import read_barcode
from .models import FoodItem


class FoodItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ean'].required = False

    class Meta:
        model = FoodItem
        fields = "__all__"
    ean_image = ImageField(required=False)


    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('ean'):
            return cleaned_data

        if not cleaned_data.get('ean_image'):
            raise ValidationError("EAN or EAN image must be provided")

        with tempfile.NamedTemporaryFile() as tmp:
            for chunk in self.cleaned_data["ean_image"].chunks():
                tmp.write(chunk)

            try:
                ean = read_barcode(tmp.name)
            except (ValueError, OSError):
                raise ValidationError("Invalid barcode")

            self.cleaned_data["ean"] = ean
            return self.cleaned_data

