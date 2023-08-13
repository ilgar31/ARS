# Generated by Django 4.2.4 on 2023-08-13 20:44

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название Объекта')),
                ('city', models.CharField(max_length=40, verbose_name='Город')),
                ('description', models.TextField(verbose_name='Описание объекта')),
                ('floor', models.CharField(max_length=50, verbose_name='Количество этажей')),
            ],
            options={
                'verbose_name': 'Объект2',
                'verbose_name_plural': 'Объекты2',
            },
        ),
        migrations.CreateModel(
            name='Object_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.models.img_save)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.object')),
            ],
        ),
    ]