from django.contrib import admin

#relative import cause they are in the same project  
from .models import Product

admin.site.register(Product)
# Register your models here.
