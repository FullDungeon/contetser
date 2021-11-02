from django import template
from django.http.response import HttpResponse
from django.db import models
from django.template import context, loader

from catalog.models import Task

import json

class Example:
    input_text  = ""
    output_text = ""

# Create your views here.
def task(request, task_id):
    task = Task.objects.get(id=int(task_id))

    template = loader.get_template('task/task.html')
    isExamples = False
    examples = {}

    # формирование словаря примеров
    if task.examples != "":                  
        isExamples = True                    
        examples = json.loads(task.examples) 

    context = {
        "site_name":        "Contester 0.1",
        "page_title":       task.topic.name,

        "task_name":        task.name,
        "task_time":        task.time,
        "task_memory":      task.memory,
        "task_difficult":   task.difficult,
        "task_text":        task.text,
        "task_input_text":  task.input_text,
        "task_output_text": task.output_text,
        "is_examples":      isExamples,
        "task_examples":    examples,
    }

    return HttpResponse(template.render(context))