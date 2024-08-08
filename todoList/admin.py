from django.contrib import admin

from todoList.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['task', 'date', 'done']


# Register your models here.
admin.site.register(Todo, TodoAdmin)
