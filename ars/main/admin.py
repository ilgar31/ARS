from django.contrib import admin
from .models import Object, Object_images, Message


class Object_imagesInline(admin.TabularInline):
    fk_name = 'object'
    model = Object_images


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [Object_imagesInline, ]


admin.site.register(Message)
