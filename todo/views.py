from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Task
# Create your views here.
def all_tasks_view(request):
    ctx={}
    ctx['tasks']=Task.objects.all()[::-1]
    return render(request, 'todo_templates/todo_tasks_all.html', ctx)

def create_task_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        content = request.POST["content"]
        status = request.POST["status"]
        # if name == '' or name == None:
        #     messages.info(request, 'Name can not be blank')
        new_task = Task.objects.create(name=name, content=content, status=status)
    return redirect('/todo/')

def update_task_view(request):
    return