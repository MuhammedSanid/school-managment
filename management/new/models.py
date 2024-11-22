from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    usertype = models.CharField(max_length=20,blank=True,null=True,unique=False,verbose_name="user type")
    approve_student=models.CharField(max_length=10,blank=False,verbose_name="approve_student")
    def __str__(self):
        return self.first_name
class Student(models.Model):
    stud =models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    dob = models.DateField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    

class Teacher(models.Model):
    tch =models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    dep = models.CharField(max_length=10)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name  