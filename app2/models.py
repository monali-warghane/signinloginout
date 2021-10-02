from django.db import models

# Create your models here.
class student(models.Model):
    Username=models.CharField(max_length=100)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Email_id=models.EmailField(max_length=100)
    Password=models.IntegerField()
    status=models.BooleanField()