from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    uclass = models.CharField(max_length=50)
    div = models.CharField(max_length=50)
    rollno = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=50)
