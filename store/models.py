from django.db import models
from category.models import * 

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=20,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    product_image = models.ImageField(upload_to='photes/products')
    product_desc = models.TextField(max_length=500,blank=True)
    product_price = models.IntegerField()
    product_stock = models.IntegerField()
    is_available = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
