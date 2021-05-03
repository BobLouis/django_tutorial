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
	title        = forms.CharField(label='titleee',required=False,widget=forms.TextInput(
																					attrs={"placeholder": "your title"}))
	description  = forms.CharField(widget=forms.Textarea(attrs={
																"class" : "newclass",
																"id"    : "my-id-for-textarea",
																"rows"  : 20,
																"cols"  : 120

																}
														) 
									)
	price     	 = forms.DecimalField(initial=199.99) 
	#SEARCH FOR django form fields 