# Generated by Django 4.0.6 on 2022-07-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_task_date_added_remove_task_date_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_added',
            field=models.DateTimeField(auto_now=True, verbose_name='Время добавления'),
        ),
    ]
