from django.urls import path
from . import views

urlpatterns = [
    path("", views.cgpa_counter, name="cgpa_counter"),
]
