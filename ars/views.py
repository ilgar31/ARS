from django.shortcuts import render
from .models import Objects


def index(request):
    return render(request, "ars/index.html")


def info(request):
    return render(request, "ars/info.html")


def objects(request):
    works = Objects.objects.all()
    data = {"objects": works}
    return render(request, "ars/objects.html", data)


def object(request, pk):
    work = Objects.objects.get(id_object=pk)
    data = {"object": work, "list": [1], "img": [str(work.photo)]}
    return render(request, "ars/object.html", data)


def contacts(request):
    return render(request, "ars/contacts.html")