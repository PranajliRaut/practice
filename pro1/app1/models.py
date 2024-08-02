
from django.db import models
# Create your models here.
class Student(models.Model):
    gen=[("female","FEMALE"),("male","MALE"),("Other","OTHER")]
    stu_id =models.IntegerField(primary_key=True)
    first_name =models.CharField(max_length=30)
    last_name =models.CharField(max_length=39)
    gender =models.CharField(max_length=37,choices=gen)
    cource = models.CharField(max_length=20)
    city =models.CharField(max_length=37)
    email =models.EmailField(max_length=37)