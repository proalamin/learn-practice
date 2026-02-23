from django.shortcuts import render
from django.http import JsonResponse

def studentsView(req):
    students =[
        {'id':1, 'name': 'API al amin'}
    ]
    
    return JsonResponse(students, safe=False)
