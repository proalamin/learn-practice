from django.db import models

class User(models.Model):
    user_name= models.CharField(max_length=100)
    user_age=models.IntegerField()