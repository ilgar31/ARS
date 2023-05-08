from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("objects", views.objects, name="objects"),
    path("contacts", views.contacts, name="contacts"),
    path("info", views.info, name="info"),
    path("object/<int:pk>", views.object, name="object")
]
