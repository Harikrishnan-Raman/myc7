from django.urls import path
from . import views
from django.core.exceptions import FieldDoesNotExist
from django.urls import re_path

urlpatterns = [
    path('', views.index, name= 'index'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin, name='admin'),
    path('instructor/', views.instructor, name='instructor'),
    path('student/', views.student, name='student'),
    re_path(r'^api/project/$', views.project_list),
    re_path(r'^api/project/(?P<pk>[0-9]+)$', views.project_detail),
    re_path(r'^api/assignments/$', views.assignment_list),
    re_path(r'^api/assignment/(?P<pk>[0-9]+)$', views.assignment_detail),
    re_path(r'^api/marks/$', views.marks_list),
    re_path(r'^api/jira/$', views.jira_progress),
]
