from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import *


@api_view(['GET', 'POST'])
def assignment_list(request):
    if request.method == 'GET':
        data = assignmentDatabase.objects.all()
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
        assignment = assignmentDatabase.objects.get(assignmentCode=pk)
    except assignmentDatabase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = assignment
        serializer = assignmentSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
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
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = projectSerializer(project, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE', 'GET'])
def evaluation_detail(request, pk):
    try:
        eval = evaluationDatabase.objects.get(pk=pk)
    except evaluationDatabase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = eval
        serializer = evaluationSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = evaluationSerializer(eval, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        eval.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        data = studentDatabase.objects.all()
        serializer = studentSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE', 'GET'])
def student_detail(request, pk):
    try:
        stu = studentDatabase.objects.get(pk=pk)
    except studentDatabase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = stu
        serializer = studentSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = studentSerializer(stu, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        stu.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['PUT', 'DELETE', 'GET'])
def submission_detail(request, pk):
    try:
        sub = submissionDatabase.objects.get(pk=pk)
    except submissionDatabase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = sub
        serializer = submissionSerializer(data, context={'request': request}, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = submissionSerializer(sub, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sub.delete()
        return Response(status=status.HTTP_200_OK)