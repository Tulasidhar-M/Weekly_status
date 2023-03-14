from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from OverallApp.models import Projects_list,Employees_list,Description_name
from OverallApp.serializers import Project_listSerializer,EmployeeSerializer,DescriptionSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def projectApi(request,id=0):
    if request.method=='GET':
        projects = Projects_list.objects.all()
        project_serializer=Project_listSerializer(projects,many=True)
        return JsonResponse(project_serializer.data,safe=False)
    elif request.method=='POST':
        project_data=JSONParser().parse(request)
        project_serializer=Project_listSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        project_data=JSONParser().parse(request)
        projects=Projects_list.objects.get(ProjectId=project_data['ProjectId'])
        project_serializer=Project_listSerializer(projects,data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        projects=Projects_list.objects.get(ProjectId=id)
        projects.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees_list.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees_list.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees_list.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)
@csrf_exempt
def DescriptionApi(request,id=0):
    if request.method=='GET':
        description = Description_name.objects.all()
        Description_serializer=DescriptionSerializer(description,many=True)
        return JsonResponse(Description_serializer.data,safe=False)
    elif request.method=='POST':
        Description_data=JSONParser().parse(request)
        Description_serializer=DescriptionSerializer(data=Description_data)
        if Description_serializer.is_valid():
            Description_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Description_data=JSONParser().parse(request)
        description=Description_name.objects.get(EmployeeId=Description_data['EmployeeId'])
        Description_serializer=DescriptionSerializer(description,data=Description_data)
        if Description_serializer.is_valid():
            Description_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        description=Description_name.objects.get(EmployeeId=id)
        description.delete()
        return JsonResponse("Deleted Successfully",safe=False)