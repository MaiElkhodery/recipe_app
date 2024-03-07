from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(max_length=200)
    optional = models.BooleanField(default = False)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to = "media/",blank=False,null=False)
    category = models.CharField(max_length=50)
    time_cooked = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient,related_name='recipes')

    def __str__(self):
        return self.name



     

