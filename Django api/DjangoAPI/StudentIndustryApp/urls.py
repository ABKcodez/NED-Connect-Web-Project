from django.urls import re_path
from StudentIndustryApp import views

urlpatterns = [
    re_path(r'^auth-data$',views.AuthDataAPI),
    re_path(r'^auth-data/([0-9]+)$',views.AuthDataAPI),
    re_path(r'^student-data$',views.StudentsAPI),
    re_path(r'^student-data/([0-9]+)$',views.StudentsAPI),
    re_path(r'^industrialist-data$',views.IndustrialistAPI),
    re_path(r'^industrialist-data/([0-9]+)$',views.IndustrialistAPI)
]