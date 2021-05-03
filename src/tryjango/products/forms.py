from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	   class Meta:
	   		model = Product
	   		fields = '__all__'
	   		field = [
	   			'title',
	   			'description',
	   			'price' ,
	   	   		] 



class RawProductForm(forms.Form):
	title        = forms.CharField()
	description  = forms.CharField()
	price     	 = forms.DecimalField() 
	suv          = forms.CharField(required=False)
	#SEARCH FOR django form fields 