from django.urls import path
from catalog import views

urlpatterns = [
	path('', views.index, name='index'),
	path('', views.mode1, name='mode1'),
	path('', views.mode2, name='mode2'),
	path('', views.mode3, name='mode3'),
	path('', views.mode4, name='mode4'),
	path('', views.mode5, name='mode5'),
	path('', views.mode6, name='mode6'),
]
