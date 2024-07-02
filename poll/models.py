from django.db import models

# Create your models here.
class Person(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)


    email=models.CharField(max_length=100)
    mob=models.IntegerField(null=True,blank=True)
    dob=models.DateField(null=True)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin=models.IntegerField(null=True)
    datecreated=models.DateTimeField(null=True)





