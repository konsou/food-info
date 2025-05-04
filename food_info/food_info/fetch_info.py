import re
from typing import NamedTuple

import requests
from bs4 import BeautifulSoup


class NutritionInfo(NamedTuple):
    kcal_per_100g: float
    fat_per_100g: float
    carbs_per_100g: float
    protein_per_100g: float


def fetch_nutrition_info(ean: int) -> NutritionInfo:
    url = f"https://www.s-kaupat.fi/tuote/placeholder/{ean}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

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

    return NutritionInfo(
        kcal_per_100g=kcal,
        fat_per_100g=fat,
        carbs_per_100g=carbs,
        protein_per_100g=protein,
    )
