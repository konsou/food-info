from django.db import migrations
from django.db.models import Count


def delete_duplicates(apps, schema_editor):
    FoodItem = apps.get_model("food_info", "FoodItem")
    eans_with_duplicates = (
        FoodItem.objects.values("ean")
        .annotate(count=Count("id"))
        .values("ean")
        .order_by()
        .filter(count__gt=1)
    )
    for ean in eans_with_duplicates:
        item_ids = FoodItem.objects.filter(ean=ean["ean"]).values_list("pk")[1:]
        FoodItem.objects.filter(pk__in=item_ids).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("food_info", "0003_alter_fooditem_ean_alter_fooditem_weight"),
    ]

    operations = [
        migrations.RunPython(delete_duplicates),
    ]
