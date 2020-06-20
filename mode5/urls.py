from django.urls import path
from mode5 import views

urlpatterns = [
	path('', views.mode5, name='mode5'),
]

