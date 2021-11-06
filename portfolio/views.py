from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages

# Create your views here.

def home(request):
	context = {
		'title' : "Yukty's Portfolio",
	}
	return render(request,'portfolio/home.html',context)

def contactMe(request):
	
	context = {
		'title' : "Contact Yukty",
	}

	if request.POST :
		c_email = request.POST.get("email","")
		c_message = request.POST.get("message","")

		try :
			validate_email(c_email)
		except ValidationError as e:
			messages.warning(request,"Invalid email")
		else:
			contact_obj = Contact(email=c_email,message=c_message)
			contact_obj.save()
			messages.success(request,"Message sent to Yukty")

		return redirect("portfolio-contactMe")
		
	return render(request,'portfolio/contactMe.html',context)
