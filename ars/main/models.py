from django.db import models


def img_save(instance, filename):
    return f'png/items/item_{instance.object.id}/{filename}'


class Object(models.Model):
    name = models.CharField("Название Объекта", max_length=300)
    city = models.CharField("Город", max_length=40)
    description = models.TextField("Описание объекта")
    floor = models.CharField("Количество этажей", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class Object_images(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=img_save)

    def __str__(self):
        return f'{self.image}'


class Message(models.Model):
    name = models.CharField("Имя", max_length=300)
    number = models.CharField("Номер", max_length=300)

    def __str__(self):
        return self.name, self.number

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

