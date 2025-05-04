import re

import requests
from bs4 import BeautifulSoup

from .models import FoodItem


def fetch_item_info(ean: int) -> FoodItem:
    """Lol no error handling at all"""
    url = f"https://www.s-kaupat.fi/tuote/placeholder/{ean}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    name_with_weight = soup.find(
        "h1", attrs={"data-test-id": "product-name"}
    ).text.strip()
    weight_text = re.search(r"\d*,*\.*\d+\s*g", name_with_weight).group(0)
    weight = float(weight_text.replace("g", "").replace(",", ".").strip())

    name = name_with_weight.replace(weight_text, "").strip()

    price_text = soup.find(
        "span", attrs={"data-test-id": "display-price"}
    ).text.replace(",", ".")
    price = float(re.findall(r"(\d*\.*\d+)", price_text)[0])

    nutrient_info_container = soup.find(
        "div", attrs={"data-test-id": "nutrients-info-per-unit-content"}
    )
    rows = nutrient_info_container.find_all(attrs={"class": "tableRow"})

    kcal_text = rows[1].find_all(attrs={"class": "cell"})[1].text.replace(",", ".")
    kcal = float(re.findall(r"(\d*\.*\d+)", kcal_text)[1])

    fat_text = rows[2].find_all(attrs={"class": "cell"})[1].text.replace(",", ".")
    fat = float(re.findall(r"(\d*\.*\d+)", fat_text)[0])

    carbs_text = rows[4].find_all(attrs={"class": "cell"})[1].text.replace(",", ".")
    carbs = float(re.findall(r"(\d*\.*\d+)", carbs_text)[0])

    protein_text = rows[6].find_all(attrs={"class": "cell"})[1].text.replace(",", ".")
    protein = float(re.findall(r"(\d*\.*\d+)", protein_text)[0])

    return FoodItem(
        name=name,
        weight=weight,
        ean=ean,
        price=price,
        kcal_per_100g=kcal,
        fat_per_100g=fat,
        carbs_per_100g=carbs,
        protein_per_100g=protein,
    )
