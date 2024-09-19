from django.contrib import admin
from .models import ToDoList

# Register your models here.
class ToDoDisplay(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']
    list_display_links = ['name', 'desc']
    ordering = ['id']

admin.site.register(ToDoList, ToDoDisplay)