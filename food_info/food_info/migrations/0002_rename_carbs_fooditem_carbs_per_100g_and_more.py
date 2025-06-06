# Generated by Django 5.2 on 2025-05-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_info', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='carbs',
            new_name='carbs_per_100g',
        ),
        migrations.RenameField(
            model_name='fooditem',
            old_name='fat',
            new_name='fat_per_100g',
        ),
        migrations.RenameField(
            model_name='fooditem',
            old_name='protein',
            new_name='protein_per_100g',
        ),
        migrations.AddField(
            model_name='fooditem',
            name='kcal_per_100g',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='weight',
            field=models.FloatField(help_text='Weight in grams'),
        ),
    ]
