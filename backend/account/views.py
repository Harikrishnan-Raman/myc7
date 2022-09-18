from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import *


import json
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('All good', status=200)
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


@csrf_exempt
def login_view(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    user = authenticate(username=username, password=password)
    if user is not None and user.role == "admin":
        login(request, user)
        return HttpResponse('hello world 3')
    elif user is not None and user.role == "instructor":
        login(request, user)
        return JsonResponse({'response_code': 'authenticated',  'username' : username, 'role' : user.role, 'univID' : user.universityID}) 
    elif user is not None and user.role == "student":
        login(request, user)
        return JsonResponse({'response_code': 'authenticated',  'username' : username, 'role' : user.role, 'univID' : user.universityID})                
    else:
        return JsonResponse({'response_code': 'unauthenticated', 'username' : username}) 


def admin(request):
    return render(request, 'profile.html')


def instructor(request):
    return render(request, 'profile.html')


def student(request):
    return render(request, 'profile.html')

@api_view(['POST', 'GET'])
def project_list(request):
    if request.method == 'GET':
        data = projectDatabase.objects.all()
        serializer = projectSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = projectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'response_code': 'created'})
        return JsonResponse({'response_code': 'error'})


@api_view(['PUT', 'DELETE', 'GET'])
def project_detail(request, pk):
    try:
        project = projectDatabase.objects.get(pk=pk)
    except projectDatabase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = project
        serializer = projectSerializer(data, context={'request': request}, many=False)
        duration = project.courseEndDate - project.courseStartDate
        courseCode = "FSE-C"+str(project.pk)
        return JsonResponse({'base_data' : serializer.data, 'courseCode': courseCode, 'courseDuration' : round((duration.days/7),1)})
    elif request.method == 'PUT':
        serializer = projectSerializer(project, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['GET', 'POST'])
def assignment_list(request):
    if request.method == 'GET':
        projCode = request.GET['projCode']
        data = assignmentDatabase.objects.filter(projCode=projCode)
        serializer = assignmentSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = assignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'response_code': 'created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE', 'GET'])
def assignment_detail(request, pk):
    try:
        assignment = assignmentDatabase.objects.get(pk=pk)
    except assignmentDatabase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = assignment
        serializer = assignmentSerializer(data, context={'request': request}, many=False)
        duration = assignment.assignmentDueDate - assignment.assignmentStartDate
        courseCode = "FSE-A"+str(assignment.pk)
        return JsonResponse({'base_data' : serializer.data, 'courseCode': courseCode, 'courseDuration' : round((duration.days/7),1)})
    elif request.method == 'PUT':
        serializer = assignmentSerializer(assignment, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        assignment.delete()
        return Response(status=status.HTTP_200_OK)




@api_view(['GET', 'POST'])
def marks_list(request):
    if request.method == 'GET':
        assignmentCode = request.GET['assignmentCode']
        groupID = request.GET['groupID']
        data = marksDatabase.objects.filter(assignmentCode=assignmentCode).filter(groupID=groupID)
        serializer = marksSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = marksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'response_code': 'evaluated'})
        return JsonResponse({'response_code': 'error'})




