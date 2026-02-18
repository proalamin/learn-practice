from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
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



def create_task(req):
    employees = Employee.objects.all()
    form =TaskForm(employees=employees) # For GET
    
    if req.method == "POST":
        form =TaskForm(req.POST, employees=employees)
        # print(form)
        if form.is_valid():
            # print(form.cleaned_data)
            data= form.cleaned_data
            title = data.get('title')
            description= data.get('description')
            due_date= data.get("due_date")
            assigned_to = data.get('assigned_to')
            
            task = Task.objects.create(title= title, description=description, due_date=due_date)
            
            # assign employee to task
            for emp_id in assigned_to:
                employee = Employee.objects.get(id=emp_id)
                task.assigned_to.add(employee)
                
            return HttpResponse("Task added successfully")

    context = {"form": form}
    return render(req, "test_form.html", context)