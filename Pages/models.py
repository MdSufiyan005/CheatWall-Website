from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Create_Test_ClassRoom(models.Model):
    Access_Token = models.CharField(max_length=150,unique=True) 
    Name_Test = models.CharField(max_length=150)
    Discription = models.CharField(max_length=150)  
    App_Name = models.CharField(max_length=150)
    Start_Time = models.DateTimeField()
    End_Time = models.DateTimeField()

    def __str__(self):
        return f'This is {self.Name_Test} exam and its access token is {self.Access_Token}'  

class Student_Response(models.Model):
    Name = models.CharField(max_length=150)
    Enrolment_no = models.CharField(max_length=150)
    RiskScore = models.CharField(max_length=100)
    Image_URL = models.URLField(max_length=500)  
    Test_ClassRoom = models.ForeignKey(Create_Test_ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f'This is {self.Name} and enrolment number is {self.Enrolment_no}'

class Test_Codes(models.Model):
    Test_code = models.CharField(max_length=500)
    Test_classroom = models.ForeignKey(Create_Test_ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f'This is {self.Test_code} and its test classroom is {self.Test_classroom}'