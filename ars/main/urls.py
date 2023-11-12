from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("objects", views.objects, name="objects"),
    path("project<int:pk>", views.project, name="project")
]
