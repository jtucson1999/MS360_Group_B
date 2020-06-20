from django.urls import path
from mode4 import views

urlpatterns = [
	path('', views.mode4, name='mode4'),
]

