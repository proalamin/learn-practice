from django.db import models

class User(models.Model):
    user_name= models.CharField(max_length=100)
    user_age=models.IntegerField()
    email=models.EmailField(default=False)
    otp=models.IntegerField(default="000000")
    status=models.BooleanField(default=False)