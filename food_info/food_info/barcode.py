import cv2
from django.core.exceptions import ValidationError
from pyzbar.pyzbar import decode as pyzbar_decode


def read_barcode(image_path: str) -> int:
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    barcodes = pyzbar_decode(gray)
    for barcode in barcodes:
        return int(barcode.data.decode("utf-8"))

    raise ValueError("No barcode found")


def validate_ean(value):
    if not len(str(value)) == 13:
        raise ValidationError("EAN must be 13 characters long")
