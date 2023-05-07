from django.shortcuts import render
from .models import Objects


def index(request):
    return render(request, "ars/index.html")


def objects(request):
    works = Objects.objects.all()
    data = {"objects": works}
    return render(request, "ars/objects.html", data)


def contacts(request):
    return render(request, "ars/contacts.html")