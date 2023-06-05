from django.db import models
class Faculty(models.Model):
    Name=models.CharField(max_length=20,default="")
    Id=models.CharField(max_length=20,primary_key=True)
    Dept=models.CharField(max_length=20)
    Mobile=models.IntegerField()
    Password=models.CharField(max_length=10,default="")
class Student(models.Model):
    Sname=models.CharField(max_length=20,default="")
    Reg=models.CharField(max_length=20,primary_key = True)
    Dept=models.CharField(max_length=20,default="")
    Class=models.CharField(max_length=20,default="")
    Psd=models.CharField(max_length=10,default="")
class Csbs(models.Model):
    Reg=models.CharField(max_length=10,default="",unique=True) 
    Dm=models.PositiveIntegerField()
    Oops=models.PositiveIntegerField()
    Dbms=models.PositiveIntegerField()
    Os=models.PositiveIntegerField()
    Ds=models.PositiveIntegerField()
class Csbs2(models.Model):
    Reg=models.CharField(max_length=10,default="",unique=True) 
    Dm=models.PositiveIntegerField()
    Oops=models.PositiveIntegerField()
    Dbms=models.PositiveIntegerField()
    Os=models.PositiveIntegerField()
    Ds=models.PositiveIntegerField()

class Csbs3(models.Model):
    Reg=models.CharField(max_length=10,default="",unique=True) 
    Dm=models.PositiveIntegerField()
    Oops=models.PositiveIntegerField()
    Dbms=models.PositiveIntegerField()
    Os=models.PositiveIntegerField()
    Ds=models.PositiveIntegerField()
class Sub(models.Model):
    Dep=models.CharField(max_length=10)
    year=models.PositiveIntegerField()
    S1=models.CharField(max_length=10)
    S2=models.CharField(max_length=10)
    S3=models.CharField(max_length=10)
    S4=models.CharField(max_length=10)
    S5=models.CharField(max_length=10)
    Staff=models.CharField(max_length=10)

