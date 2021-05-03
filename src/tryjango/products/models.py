from django.db import models

# Create your models here.
class Product(models.Model):
	title 	     =  models.CharField(max_length=30)
	description  =  models.TextField(blank=True,null=True)
	price        =  models.DecimalField(max_digits=30,decimal_places=2)
	suv          =  models.TextField(blank=True,null=False) 
	features     =  models.BooleanField(default=False)  #null=True=>data base won't have neccesary have to save