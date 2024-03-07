from django.db import models


class Ingredient(models.Model):
    UNITS = [
            ('Grams', 'Grams'),
            ('Kilograms', 'Kilograms'),
            ('Milliliters', 'Milliliters'),
            ('Liters', 'Liters'),
            ('Teaspoons', 'Teaspoons'),
            ('Tablespoons', 'Tablespoons'),
            ('Cups', 'Cups'),
            ('Ounces', 'Ounces'),
            ('Pounds', 'Pounds'),
            ('Pieces', 'Pieces'),
            ('Slices', 'Slices'),
            ('Cloves', 'Cloves'),
            ('Pinches', 'Pinches'),
            ('Handfuls', 'Handfuls'),
            ('Drops', 'Drops'),
    ]
    name = models.CharField(max_length=70)
    unit = models.CharField(max_length=20,choices=UNITS)
    quantity = models.FloatField(default=5)
    optional = models.BooleanField(default = False)         

    def __str__(self):
        return f'{self.quantity} {self.unit} {self.name}'
class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('dessert', 'Dessert'),
        ('salad', 'Salad'),
        ('appetizer', 'Appetizer'),
        ('main_course', 'Main Course'),
        ('side_dish', 'Side Dish'),
        ('beverage', 'Beverage')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to = "media/",blank=False,null=False)
    category = models.CharField(max_length=50,choices = CATEGORY_CHOICES)
    time_cooked = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient,related_name="recipe")

    def __str__(self):
        return self.name

     

