from django.contrib import admin
from .models import Todo

class FrontendConfig(Todo):
    name = 'Todo'
    verbose_name = "Дела"

class TodoAdmin(admin.ModelAdmin):
    fields = ('created', 'datecompleted')

admin.site.register(Todo, TodoAdmin)