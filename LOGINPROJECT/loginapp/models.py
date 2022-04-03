from django.db import models

# Create your models here.
class logintable(models.Model):
    username=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneno=models.BigIntegerField()

