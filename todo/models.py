from django.db import models
from django.forms import CharField



class Task(models.Model):
    task_status = (
        ('not_active', 'Не активно'),
        ('active', 'Активно'),
        ('in_process', 'В процессе'),
        ('done', 'Завершено')
    )
    name = models.CharField(verbose_name='Название задачи', max_length=50)
    content = models.TextField(verbose_name='Контент', blank=True)
    date_added = models.DateTimeField(verbose_name='Время добавления', auto_now=True, auto_now_add=False)
    date_closed = models.DateTimeField(verbose_name='Время завершения', auto_now=False, auto_now_add=False)
    status = models.CharField(verbose_name='Статус', max_length=50, choices=task_status, default='active')