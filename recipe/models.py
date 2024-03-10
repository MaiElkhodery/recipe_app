from django.db import models

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
    picture = models.ImageField(upload_to = "media/",blank=True,null=True)
    category = models.CharField(max_length=50,choices = CATEGORY_CHOICES)
    time_cooked = models.IntegerField()
    # ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,default=0)       

    def __str__(self):
        return self.name
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
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,null = True)


    def __str__(self):
        return f'{self.quantity} {self.unit} {self.name}'

    

