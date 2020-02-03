from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50) 
    price = models.DecimalField(max_digits=19, decimal_places=10, blank=True, null=True)
    description = models.CharField(max_length=500)
    description_translate = models.CharField(max_length = 500, null = True)
    category = models.name = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product_image', blank = True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
    

