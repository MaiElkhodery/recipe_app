# Generated by Django 5.0.2 on 2024-03-07 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='optional',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('Grams', 'Grams'), ('Kilograms', 'Kilograms'), ('Milliliters', 'Milliliters'), ('Liters', 'Liters'), ('Teaspoons', 'Teaspoons'), ('Tablespoons', 'Tablespoons'), ('Cups', 'Cups'), ('Ounces', 'Ounces'), ('Pounds', 'Pounds'), ('Pieces', 'Pieces'), ('Slices', 'Slices'), ('Cloves', 'Cloves'), ('Pinches', 'Pinches'), ('Handfuls', 'Handfuls'), ('Drops', 'Drops')], max_length=50),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('dessert', 'Dessert'), ('salad', 'Salad'), ('appetizer', 'Appetizer'), ('main_course', 'Main Course'), ('side_dish', 'Side Dish'), ('beverage', 'Beverage')], max_length=50),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(max_length=200)),
                ('optional', models.BooleanField(default=False)),
            ],
        )
    ]