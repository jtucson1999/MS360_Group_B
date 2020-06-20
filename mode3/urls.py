from django.urls import path
from mode3 import views

urlpatterns = [
	path('', views.mode3, name='mode3'),
]

