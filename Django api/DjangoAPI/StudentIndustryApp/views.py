from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from StudentIndustryApp.models import AuthData,Students,Industrialist,Job
from StudentIndustryApp.serealizers import AuthDataSerializer,StudentsSerializer,IndustrialistSerializer,JobSerializer


# Create your views here.

@csrf_exempt

def AuthDataAPI(request,id=0):
    if request.method == "GET":
        authData = AuthData.objects.all()
        authData_Serializer = AuthDataSerializer(authData, many=True)
        return JsonResponse(authData_Serializer.data,safe=False)
    elif request.method == "POST":
        authData = JSONParser().parse(request)
        authData_Serializer = AuthDataSerializer(data=authData)
        if authData_Serializer.is_valid():
            authData_Serializer.save()
            return JsonResponse("Added Successfully!",safe=False)
        return JsonResponse("Failed to Add!", safe=False)
    elif request.method == "PUT":
        authData = JSONParser().parse(request)
        auth_data = AuthData.objects.get(user_id = authData['user_id'])
        authData_Serializer = AuthDataSerializer(auth_data,data=authData)
        if authData_Serializer.is_valid():
            authData_Serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to update!",safe=False)
    elif request.method == "DELETE":
        auth_data = AuthData.objects.get(user_id = id)
        auth_data.delete()
        return JsonResponse("Deleted!", safe=False)
    
def StudentsAPI(request,id=0):
    if request.method == "GET":
        studentsData = Students.objects.all()
        studentsData_Serializer = StudentsSerializer(studentsData, many=True)
        return JsonResponse(studentsData_Serializer.data,safe=False)
    elif request.method == "POST":
        studentsData = JSONParser().parse(request)
        studentsData_Serializer = StudentsSerializer(data=studentsData)
        if studentsData_Serializer.is_valid():
            studentsData_Serializer.save()
            return JsonResponse("Added Successfully!",safe=False)
        return JsonResponse("Failed to Add!", safe=False)
    elif request.method == "PUT":
        studentsData = JSONParser().parse(request)
        students_data = Students.objects.get(user_id = studentsData['user_id'])
        studentsData_Serializer = AuthDataSerializer(students_data,data=studentsData)
        if studentsData_Serializer.is_valid():
            studentsData_Serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to update!",safe=False)
    elif request.method == "DELETE":
        students_data = AuthData.objects.get(user_id = id)
        students_data.delete()
        return JsonResponse("Deleted!", safe=False)
    
def IndustrialistAPI(request,id=0):
    if request.method == "GET":
        IndustrialistData = Industrialist.objects.all()
        IndustrialistData_Serializer = IndustrialistSerializer(IndustrialistData, many=True)
        return JsonResponse(IndustrialistData_Serializer.data,safe=False)
    elif request.method == "POST":
        IndustrialistData = JSONParser().parse(request)
        IndustrialistData_Serializer = IndustrialistSerializer(data=IndustrialistData)
        if IndustrialistData_Serializer.is_valid():
            IndustrialistData_Serializer.save()
            return JsonResponse("Added Successfully!",safe=False)
        return JsonResponse("Failed to Add!", safe=False)
    elif request.method == "PUT":
        IndustrialistData = JSONParser().parse(request)
        Industrialist_data = Industrialist.objects.get(user_id = IndustrialistData['user_id'])
        IndustrialistData_Serializer = AuthDataSerializer(Industrialist_data,data=IndustrialistData)
        if IndustrialistData_Serializer.is_valid():
            IndustrialistData_Serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to update!",safe=False)
    elif request.method == "DELETE":
        Industrialist_data = AuthData.objects.get(user_id = id)
        Industrialist_data.delete()
        return JsonResponse("Deleted!", safe=False)
    
def JobAPI(request,id=0):
    if request.method == "GET":
        JobData = Job.objects.all()
        JobData_Serializer = JobSerializer(JobData, many=True)
        return JsonResponse(JobData_Serializer.data,safe=False)
    elif request.method == "POST":
        JobData = JSONParser().parse(request)
        JobData_Serializer = JobSerializer(data=JobData)
        if JobData_Serializer.is_valid():
            JobData_Serializer.save()
            return JsonResponse("Added Successfully!",safe=False)
        return JsonResponse("Failed to Add!", safe=False)
    elif request.method == "PUT":
        JobData = JSONParser().parse(request)
        Job_data = Job.objects.get(job_id = JobData['job_id'])
        JobData_Serializer = AuthDataSerializer(Job_data,data=JobData)
        if JobData_Serializer.is_valid():
            JobData_Serializer.save()
            return JsonResponse("Updated Successfully!",safe=False)
        return JsonResponse("Failed to update!",safe=False)
    elif request.method == "DELETE":
        Job_data = AuthData.objects.get(job_id = id)
        Job_data.delete()
        return JsonResponse("Deleted!", safe=False)
    

    


        
