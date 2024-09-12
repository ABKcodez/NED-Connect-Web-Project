from rest_framework import serializers
from StudentIndustryApp.models import AuthData,Students,Industrialist,Job


class AuthDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthData
        fields = ('user_id', 'first_name', 'last_name', 'email', 'password' ,'contact', 'category')

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('user_id', 'gender', 'batch', 'roll', 'department' ,'year', 'skills','description','linkedin','github','behance')

class IndustrialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industrialist
        fields = ('user_id', 'gender', 'company_name', 'about_company', 'designation' ,'expertise', 'linkedin','office_mail','linkedin','github','behance')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_id', 'job_title', 'job_type', 'working_hours', 'job_description' ,'req_skills', 'req_experience')