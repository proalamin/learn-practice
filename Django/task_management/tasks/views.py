from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #work with database
    #transform data
    # data pass
    # http response / JSON response
    return HttpResponse('this views from task --> home')


def show_task(request):
    return HttpResponse("this is task from task url")


def new_task(request):
    return HttpResponse('this is new task page')

def task_id(request, id):
    return HttpResponse(f'this is new task page {id}')
