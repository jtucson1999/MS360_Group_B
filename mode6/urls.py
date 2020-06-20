from django.urls import path
from mode6 import views

urlpatterns = [
	path('', views.mode6, name='mode6'),
]

