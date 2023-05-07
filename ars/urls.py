from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("objects", views.objects, name="objects"),
    path("contacts", views.contacts, name="contacts")
]