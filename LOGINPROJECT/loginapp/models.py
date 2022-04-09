from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class logintable(models.Model):
    username=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phoneno=models.BigIntegerField(validators=[RegexValidator(r'^\d\d\d\d\d\d\d\d\d\d$')],help_text=("format:xxxxxxxxxx,required,unique"),verbose_name=("Contact No"))

