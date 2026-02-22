from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
from datetime import date
from django.db.models import Q

def manager_dashboard(request):
    return render(request, 'dashboard/manager_dashboard.html')


def user_dashboard(request):
    return render(request, 'dashboard/user_dashboard.html')


def test(request):
    data ={
        'names': ['john', 'abdul', 'Hamid']
    }
    return render(request, 'test.html', data)


def create_task(request):

    message = None
    form = TaskModelForm()   # default GET form

    if request.method == "POST":
        form = TaskModelForm(request.POST)

        if form.is_valid():
            form.save()
            message = "Task added successfully!"
            form = TaskModelForm()   # 🔥 reset form after save

    context = {
        "form": form,
        "message": message
    }

    return render(request, "test_form.html", context)


def view_task(req):
    # retrieve all data from task model
    # tasks = Task.objects.all()
    
    # retrieve a specific task
    # task_3 = Task.objects.get(pk=2)
    
    # retrieve a specific task
    # first_task = Task.objects.first()
    
    
    # return render(req, 'show_task.html', {"tasks": tasks, "task_3": task_3, "first_task": first_task})
    # return HttpResponse("ok")
    
    # pending_tasks= Task.objects.filter(status = "PENDING")
    
    # show the task which due date today
    # due_date_today= Task.objects.filter(due_date= date.today())
    
    # show the task which priority is not low
    # priority_not_low= TaskDetail.objects.exclude(priority = 'L')
    
    # show the task that contain word c and status PENDING""
    # words= Task.objects.filter(title__icontains = 'c', status= 'PENDING')
    
    # show the task that contain word c OR status PENDING""
    # words_or= Task.objects.filter(Q(title__icontains = 'c') | Q(status= 'PENDING'))
        
    # return render(req, 'show_task.html', {'pending_tasks': pending_tasks, 'due_date_today':due_date_today, "priority_not_low": priority_not_low, 'words': words, "words_or": words_or})
    
    # select related(ForeignKey, OneToOneFiled)
    # tasks = Task.objects.select_related('details').all()
    # tasks = TaskDetail.objects.select_related('task').all()
    
    # foreignkey one one way 
    tasks = Task.objects.select_related('project').all()
    
    """prefetch_related (reverse Foreignkey, manytomany) """
    # tasks = Project.objects.prefetch_related('task_set').alast()
    
    return render(req, 'show_task.html', {'tasks': tasks})