# Generated by Django 4.0.6 on 2022-07-10 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date_closed',
        ),
    ]