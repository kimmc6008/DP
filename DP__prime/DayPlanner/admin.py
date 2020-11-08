from django.contrib import admin
from .models import Search, TodoList
from . import models

# Register your models here.
admin.site.register(Search)
admin.site.register(TodoList)