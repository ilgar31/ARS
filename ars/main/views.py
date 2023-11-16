from django.shortcuts import render
from .models import Object, Object_images, Message
from django.core.mail import send_mail
from django.http import JsonResponse


def index(request):

    objects = Object.objects.all()

    if request.method == "POST":
        print(request.POST)
        name = request.POST.get("name")
        number = request.POST.get("number")
        if name and number:
            message = Message()
            message.name = name
            message.number = number
            message.save()
            send_mail(f"Имя: {name}         Номер: {number}", "Сайт АРС отправил эту форму", "sunclub.stor@gmail.com", ["ars.yar@bk.ru"])

    return render(request, "index.html", {"web_objects": objects[:4], "mobile_objects": objects[:2]})


def objects(request):
    my_objects = Object.objects.all()
    return render(request, "objects.html", {"objects": my_objects})


def project(request, pk):
    object_item = Object.objects.get(id=pk)
    images = []
    for i in object_item.images.all():
        images.append(i)

    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        if name and number:
            message = Message()
            message.name = name
            message.number = number
            message.save()
            send_mail(f"Имя: {name}         Номер: {number}", "Сайт АРС отправил эту форму", "sunclub.stor@gmail.com", ["ars.yar@bk.ru"])

    return render(request, "project.html", {"object": object_item, "images": enumerate(images)})
