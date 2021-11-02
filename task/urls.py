from django.urls import path

from . import views

urlpatterns = [
    path('<int:task_id>', views.task, name='task-url')
]