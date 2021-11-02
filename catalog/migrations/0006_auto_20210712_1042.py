# Generated by Django 3.2.5 on 2021-07-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_rename_number_theme_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='preffix',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M')], default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='theme',
            name='order',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]