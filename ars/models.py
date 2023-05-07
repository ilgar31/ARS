from django.db import models


def png_save(instance, filename):
    return f'png/object_{instance.id_object}/{filename}'


class Objects(models.Model):
    id_object = models.IntegerField("Номер объекта (ID)")
    name = models.CharField("Название Объекта", max_length=300)
    city = models.CharField("Город", max_length=40)
    description = models.TextField("Описание объекта")
    address = models.CharField("Адрес", max_length=150)
    contractor = models.CharField("Генеральный подрядчик", max_length=60)
    customer = models.CharField("Заказчик", max_length=60)
    designer = models.CharField("Проектировщик", max_length=60)
    types_of_work = models.CharField("Виды выполняемых работ", max_length=150)
    building_area = models.CharField("Площадь застройки", max_length=50)
    data = models.DateTimeField("Окончание строительства")
    photo = models.FileField("Фотография", upload_to=png_save)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"

