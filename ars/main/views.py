from django.shortcuts import render
from .models import Object, Object_images, Message
from django.core.mail import send_mail
from django.http import JsonResponse


def index(request):

    objects = Object.objects.all()

    if request.method == "POST":
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            from_obj = int(request.POST.get("from"))
            if request.POST.get("type") == "web":
                flag = False
                if len(objects) <= from_obj + 4:
                    flag = True

                objects_list = [{"url": "../project" + str(i.id), "name": i.name, "city": i.city, "floor": i.floor, "description": i.description, "image": '/static/' + str(i.images.all()[0])} for i in objects[from_obj:from_obj + 4]]

                return JsonResponse({"objects": objects_list, "flag": flag, "foto1": '/static/png/city.png', "foto2": '/static/png/floors.png', "foto3": '/static/png/strelka.png'})
            else:
                flag = False
                if len(objects) <= from_obj + 2:
                    flag = True

                objects_list = [{"url": "../project" + str(i.id), "name": i.name, "city": i.city, "floor": i.floor, "description": i.description, "image": '/static/' + str(i.images.all()[0])} for i in objects[from_obj:from_obj + 2]]

                return JsonResponse({"objects": objects_list, "flag": flag, "foto1": '/static/png/city.png', "foto2": '/static/png/floors.png', "foto3": '/static/png/strelka.png'})
        else:
            name = request.POST.get("name")
            number = request.POST.get("number")
            if name and number:
                message = Message()
                message.name = name
                message.number = number
                message.save()
                send_mail(f"Имя: {name}         Номер: {number}", "Сайт АРС отправил эту форму", "sunclub.stor@gmail.com", ["ars.yar@bk.ru"])

    return render(request, "index.html", {"web_objects": objects[:4], "mobile_objects": objects[:2]})


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