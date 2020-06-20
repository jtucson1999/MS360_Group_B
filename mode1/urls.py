from django.urls import path
from mode1 import views

urlpatterns = [
	path('', views.mode1, name='mode1'),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)