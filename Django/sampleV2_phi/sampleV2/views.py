from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from sampleV2.models import User


def home(req):
    return render(req, 'home.html')

import random
from django.core.mail import send_mail
from django.conf import settings

def generate_6_digit_code():
    return random.randint(100000, 999999)


def send_email_otp(u_email, otp,id):
    otp = otp
    verification_url = f"http://127.0.0.1:8000/verify/{id}/"

    send_mail(
        subject="OTP Verification",
        message=f"""
        Hello,
        Your OTP is: {otp}
        It will expire in 5 minutes.

        Click below to verify:
        {verification_url}
        """,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[u_email],
        fail_silently=False,
    )

def verify_email(req, id):
    user = get_object_or_404(User, id=id)
    return render(req, "verify.html", {"user": user})

def verify_otp(req, user_id):
    if req.method == "POST":
        input_otp = req.POST.get("otp")
        user = get_object_or_404(User, id=user_id)

        if str(user.otp) == str(input_otp):
            user.status = True
            user.save()
            return HttpResponse("✅ Verification Successful!")
        else:
            return HttpResponse("❌ Wrong OTP")


def insert_data(req):
    name=req.POST.get('name')
    age=req.POST.get('age')
    email=req.POST.get('email')
    otp=generate_6_digit_code()
    # return HttpResponse({opt})
    
    store_user_data=User(user_name=name, user_age=age, email=email, otp=otp)
    store_user_data.save()
    id=store_user_data.id
    send_email_otp(email, otp, id)

    
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