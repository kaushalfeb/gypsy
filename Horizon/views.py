from .models import Posts,Projects,Testimonials
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

def postlist(request):
	posts = Posts.objects.all()
	heropost = Posts.objects.all()[:1]
	latest_posts = Posts.objects.all()[2:6]
	editors = Posts.objects.all()[6:10]
	return render(request,'Horizon/postlist.html',
		{'posts':posts,
   		'heropost':heropost,
		'latest_posts':latest_posts,
		'editors':editors}
		)

def home(request):
	posts = Posts.objects.all()
	projects = Projects.objects.all()
	
	first_three_rows = Posts.objects.all()[:3]
	testimonials = Testimonials.objects.all()
	return render(request,'Horizon/homer.html',
			   {'posts':posts,'projects':projects,
	   			'first_three_rows' : first_three_rows,
				'testimonials':testimonials}
			   )

def reading(request,id):
	read = get_object_or_404(Posts,pk=id)
	return render(request,'Horizon/reading.html',{'read':read})
