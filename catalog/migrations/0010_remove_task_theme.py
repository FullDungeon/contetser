# Generated by Django 3.2.5 on 2021-07-14 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_task_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='theme',
        ),
    ]
