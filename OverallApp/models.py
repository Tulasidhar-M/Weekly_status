from django.db import models

# Create your models here.
class Projects_list(models.Model):
    ProjectId = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=500)

class Employees_list(models.Model):
    EmployeeId = models.CharField(max_length=100)
    EmployeeName = models.CharField(max_length=500)
    Project = models.CharField(max_length=1000)

class Description_name(models.Model):
    ProjectName = models.CharField(max_length=500)
    EmployeeId = models.CharField(max_length=100)
    EmployeeName = models.CharField(max_length=500)
    week_start = models.CharField(max_length=500)
    week_end = models.CharField(max_length=500)
    Description = models.CharField(max_length=1000)