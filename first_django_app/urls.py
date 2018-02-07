"""
Definition of urls for first_django_app.
"""

from django.contrib import admin
from django.urls import path, include
from first_django_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name="welcome"),
    path('customer/', include('customer.urls'))
]
