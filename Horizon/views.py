from .models import Posts,Projects,Testimonials
from django.http import HttpResponse
from django.shortcuts import render

def postlist(request):
	posts = Posts.objects.all()
	return render(request,'Horizon/postlist.html',{'posts':posts})

def home(request):
	posts = Posts.objects.all()
	projects = Projects.objects.all()
	
	first_three_rows = Posts.objects.all()[:3]
	testimonials = Testimonials.objects.all()
	return render(request,'Horizon/homer.html',{'posts':posts,'projects':projects,'first_three_rows' : first_three_rows,'testimonials':testimonials})