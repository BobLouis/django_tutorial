
from django.shortcuts import render
from .models import Product
from .forms import ProductForm , RawProductForm

# Create your views here

def product_create_view(request):
	my_form=RawProductForm() #init the form
	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)
	context={
		"form" : my_form 
	}
	my_form=RawProductForm()
	return render(request, "products/product_create_post.html",context)








#creat form from RAW POST
# def product_create_view(request):
# 	print('GET',request.GET)
# 	print('POST',request.POST)
# 	if(request.method=="POST"):
# 		my_title=request.POST.get('title')
# 		print('My title',my_title)
# 	context={}
	
# 	return render(request, "products/product_create_raw.html",context)





#create form from form function 
# def product_create_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = ProductForm() #reblank the form


# 	context = {
# 		'form':form
# 	}

# 	return render(request,"products/product_create.html",context)



def product_detail_view(request):
	obj=Product.objects.get(id=9)
	# context = {
	# 	'title' : obj.title,
	# 	'description' : obj.description
	# }
	context = {
		'object' : obj
	}

	return render(request,"product_detail.html",context)
