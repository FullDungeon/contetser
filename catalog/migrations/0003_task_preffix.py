# Generated by Django 3.2.5 on 2021-07-10 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210710_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='preffix',
            field=models.CharField(default='', max_length=5),
        ),
    ]
