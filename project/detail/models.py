from django.db import models

# Create your models here.
class Employee_detail(models.Model):
    firstname=models.CharField(max_length=30)
    secondname=models.CharField(max_length=30)
    email=models.EmailField(primary_key=True)
    phone =models.IntegerField(unique=True)
    state=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    skills=models.CharField(max_length=70)
    experience=models.CharField(max_length=1000)
    reference=models.CharField(max_length=60)
    file=models.FileField(upload_to="file")
    address=models.CharField(max_length=4000)
    
    def __str__(self):
        return self.firstname
    
    