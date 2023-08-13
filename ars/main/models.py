from django.db import models


def img_save(instance, filename):
    return f'main/png/items/item_{instance.item.id}/{filename}'


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
