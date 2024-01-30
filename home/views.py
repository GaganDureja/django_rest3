from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)    
    return Response({"status":200, "payload":serializer.data})


@api_view(['POST'])
def post_student(request):
    # data = request.data
    serializer = StudentSerializer(data = request.data)
    if not serializer.is_valid():        
        return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

    serializer.save()
    return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})

@api_view(['PUT'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj, data = request.data)
        if not serializer.is_valid():
            return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

        serializer.save()
        return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})
    except Exception as e:        
        return Response({'status':403, 'message':'Invalid ID'})


@api_view(['PATCH'])
def update_student(request, id):
    try:
        student_obj = Student.objects.get(id=id)        
        serializer = StudentSerializer(student_obj, data = request.data, partial=True)
        if not serializer.is_valid():        
            return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

        serializer.save()
        return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})
    except Exception as e:        
        return Response({'status':403, 'message':'Invalid ID'})