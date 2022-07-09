from django.shortcuts import render
from .models import Task
# Create your views here.
def all_tasks_view(request):
    ctx={}
    ctx['tasks']=Task.objects.all()
    return render(request, 'todo_templates/todo_tasks_all.html')