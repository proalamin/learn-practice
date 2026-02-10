from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from sampleV2.models import User


def home(req):
    return render(req, 'home.html')


def insert_data(req):
    name=req.POST.get('name')
    age=req.POST.get('age')
    
    store_user_data=User(user_name=name, user_age=age)
    store_user_data.save()
    
    # return HttpResponse(f"user name -{name} and age is {age}")
    return redirect('views')


def views_data(req):
    data= User.objects.all()
    return render(req, 'views.html', {"allData": data})

def edit_data(req, id):
    user = get_object_or_404(User, id=id)
    return render(req, 'edit_page.html', {"user": user})

def update(req):
    name=req.POST.get('name')
    age=req.POST.get('age')
    id=req.POST.get('id')
    
    user = get_object_or_404(User, id=id)
    
    user.user_name=name
    user.user_age=age
    user.save()

    # return HttpResponse(f"user name -{name} and age is {age}, id-{id}")
    return redirect('views')



def delate_single_user(req, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('views')

    # return HttpResponse(f"delete user id is {id}")