from django.shortcuts import render
from .models import Object, Object_images


def index(request):
    objects = Object.objects.all()
    return render(request, "index.html", {"objects": objects})


def project(request, pk):
    object_item = Object.objects.get(id=pk)
    return render(request, "project.html", {"object": object_item})