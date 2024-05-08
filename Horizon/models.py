from django.db import models
from django.utils import timezone
from django.conf import settings

class Posts(models.Model):
	title = models.CharField(max_length=100,default='Add your title')
	sub_title = models.CharField(max_length=200,default='Short subtitle')
	genre = models.CharField(max_length=30,default="Essay")
	author = models.CharField(default="Caspian",max_length=50)
	bg_name = models.CharField(max_length=100,default="grass.jpg")
	published = models.DateTimeField(default = timezone.now)
	likes = models.IntegerField(default=0)
	article = models.TextField()
	
	def publish(self):	
		self.published = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Projects(models.Model):
	title = models.CharField(max_length=100)
	about = models.CharField(max_length=200)
	type_proj = models.CharField(max_length=50)
	live = models.BooleanField(default=False)
	tech_used = models.CharField(max_length=100)
	bg_name = models.CharField(max_length=50)
	def publish(self):
		self.save()
	def __str__(self):
		return self.title

class Testimonials(models.Model):
	dp = models.CharField(max_length=200)
	username = models.CharField(max_length=100)
	designation = models.CharField(max_length=200)
	email = models.EmailField(max_length=200,unique=True)
	comment = models.TextField()
	def publish(self):
		self.save()
	def __str__(self):
		return self.username
