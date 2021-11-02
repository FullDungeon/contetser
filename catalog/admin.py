from django.contrib import admin

from .models import Task, Topic, Theme

class ThemeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основное', {'fields': ['name', 'order']}),
    ]

    list_display = ['name', 'order']

class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основное',         {'fields': ['name', 'topic', 'preffix']}),
        ('Параметры задачи', {'fields': ['time', 'memory', 'difficult']}),
        ('Содержание',       {'fields': ['text', 'input_text', 'output_text', 'examples']}),
    ]

    list_display = ['name', 'topic', 'preffix']

admin.site.register(Task, TaskAdmin)
admin.site.register(Topic)
admin.site.register(Theme, ThemeAdmin)

