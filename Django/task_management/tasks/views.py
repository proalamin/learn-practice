from django.shortcuts import render
from django.http import HttpResponse

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
    return render(req, "test_form.html")