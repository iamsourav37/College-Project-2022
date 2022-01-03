from django.urls import path, include
from rest_framework.authtoken import views as auth_view

from . import views


urlpatterns = [
    path("", views.api_index),
]