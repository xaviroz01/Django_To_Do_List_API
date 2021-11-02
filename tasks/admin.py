from typing import List
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['type', 'status']
    list_filter = ['type','status']
    

# Register your models here.
admin.site.register(Task, TaskAdmin)