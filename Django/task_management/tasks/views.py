from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task

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
