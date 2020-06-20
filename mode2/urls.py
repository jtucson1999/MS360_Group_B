from django.urls import path
from mode2 import views

urlpatterns = [
	path('', views.mode2, name='mode2'),
]

