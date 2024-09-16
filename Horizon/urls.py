from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('blog/',views.postlist,name='postlist'),
	path('blog/<int:id>/',views.reading,name='reading'),
	path('projects/',views.projects, name='projects'),
    path('about/',views.about,name='about'),
]
