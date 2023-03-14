from django.conf.urls import url
from OverallApp import views

urlpatterns=[
    url(r'^projects_list$',views.projectApi),
    url(r'^projects_list/([0-9]+)$',views.projectApi),

    url(r'^employee_list$',views.employeeApi),
    url(r'^employee_list/([0-9]+)$',views.employeeApi),

    url(r'^Description$',views.DescriptionApi),
    url(r'^Description/([0-9]+)$',views.DescriptionApi),

]