from django.db import models
from django.contrib.postgres.fields import ArrayField
import pymongo

# Create your models here.

class AuthData(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=40, unique=True)
    password = models.CharField(max_length=50)
    contact = models.CharField(max_length=15, unique=True)
    category = models.CharField(max_length=10)

class Students(models.Model):
    user_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=1)
    batch = models.CharField(max_length=4)
    roll = models.CharField(max_length=8 )
    department = models.CharField(max_length=25)
    year = models.CharField(max_length=1)
    skills = ArrayField(models.CharField(max_length=20))
    description = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    behance = models.CharField(max_length=100)

class Industrialist(models.Model):
    user_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=1)
    company_name = models.CharField(max_length = 20)
    about_company = models.CharField(max_length=100)
    designation = models.CharField(max_length=25)
    expertise = ArrayField(models.CharField(max_length=20))
    linkedin = models.CharField(max_length=100 ,unique=True)
    office_mail = models.EmailField(max_length=100 ,unique=True)

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=15)
    job_type = models.CharField(max_length=15)
    working_hours = models.CharField(max_length=15)
    job_description = models.CharField(max_length=100)
    req_skills = ArrayField(models.CharField(max_length=20))
    req_experience = models.CharField(max_length=10)



