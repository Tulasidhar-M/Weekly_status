from rest_framework import serializers
from OverallApp.models import Projects_list,Employees_list,Description_name

class Project_listSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects_list 
        fields=('ProjectId','ProjectName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees_list 
        fields=('EmployeeId','EmployeeName','Project')
class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description_name
        fields = ('ProjectName','EmployeeId','EmployeeName','week_start','week_end','Description')
