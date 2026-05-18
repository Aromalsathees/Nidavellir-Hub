from django.contrib import admin
from .models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug':('category_name',)}  #slug automatically generting in the admin field
    list_display = ('category_name','category_slug','catgegory_image')

admin.site.register(Category,CategoryAdmin)