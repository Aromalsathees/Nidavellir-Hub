from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    category_slug = models.SlugField(max_length=100,unique=True,blank=True)
    category_desc = models.TextField(max_length=150,blank=True)
    catgegory_image = models.ImageField(upload_to='photes/categories',blank=True)

    # for altering the names in the database 
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name