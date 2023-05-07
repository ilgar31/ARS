from django.shortcuts import render


def index(request):
    return render(request, "ars/index.html")


def objects(request):
    return render(request, "ars/objects.html")


def contacts(request):
    return render(request, "ars/contacts.html")