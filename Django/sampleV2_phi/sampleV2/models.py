import uuid
from django.db import models

class User(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user_name = models.CharField(max_length=100)
    user_age = models.IntegerField()
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    status = models.BooleanField(default=False)
