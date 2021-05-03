from django.http import HttpResponse
from django.shortcuts import render

# Create your views here
def home_view(request,*args,**kwargs):
	print('user: ',request.user)
	print(args)
	print(kwargs)
	# return HttpResponse("<h1>Home page</h1>") #string of HTML code
	return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
	# return HttpResponse("<h1>Contact pages</h1>")
	return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
	my_context={
		"my_text": "This is about us",
		"my_number": 123,
		"my_list": [123,456,312,"ABC"]
	}
	# return HttpResponse("<h1>About pages</h1>")
	return render(request,"aboutPage.html",my_context)