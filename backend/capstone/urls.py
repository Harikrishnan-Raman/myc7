"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from rest_framework.documentation import include_docs_urls

from C6Prj import views

urlpatterns = [
    re_path(r'^api/project/$', views.project_list),
    re_path(r'^api/project/(?P<pk>[0-9]+)$', views.project_detail),
    re_path(r'^api/assignment/$', views.assignment_list),
    re_path(r'^api/assignment/(?P<pk>[0-9]+)$', views.assignment_detail),
    re_path(r'^api/evaluation/(?P<pk>[0-9]+)$', views.evaluation_detail),
    re_path(r'^api/submission/(?P<pk>[0-9]+)$', views.submission_detail),
    re_path(r'^api/student/(?P<pk>[0-9]+)$', views.student_detail),
    re_path(r'^api/student/$', views.student_list),
    path('admin/', admin.site.urls),
    path(r'docs/', include_docs_urls(title='Helpdesk API'))
]
