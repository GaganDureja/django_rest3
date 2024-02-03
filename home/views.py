from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

from rest_framework.views import APIView




@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs, many=True)
    # print(serializer.data,"fffffffffffffffffffffffff")

    return Response({'status':200, 'payload':serializer.data})



class StudentAPI(APIView):
    
    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)    
        return Response({"status":200, "payload":serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if not serializer.is_valid():        
            return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

        serializer.save()
        return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})
    
    def put(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])        
            serializer = StudentSerializer(student_obj, data = request.data)
            if not serializer.is_valid():        
                return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

            serializer.save()
            return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})
        except Exception as e:        
            print(e) 
            return Response({'status':403, 'message':'Invalid ID'})

    def patch(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])        
            serializer = StudentSerializer(student_obj, data = request.data, partial=True)
            if not serializer.is_valid():        
                return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

            serializer.save()
            return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})
        except Exception as e:        
            print(e) 
            return Response({'status':403, 'message':'Invalid ID'})

    def delete(self, request):
        try:
            student_obj = Student.objects.get(id=request.data['id'])
            student_obj.delete()
            return Response({"status":200, "message": "Your data is deleted"})

        except Exception as e:
            return Response({'status':403, 'message':'Invalid ID'})






# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)    
#     return Response({"status":200, "payload":serializer.data})


# @api_view(['POST'])
# def post_student(request):
#     # data = request.data
#     serializer = StudentSerializer(data = request.data)
#     if not serializer.is_valid():        
#         return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

#     serializer.save()
#     return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})

# # @api_view(['PUT'])

# # make new function name and url for this

# # def update_student(request, id):
# #     try:
# #         student_obj = Student.objects.get(id=id)
# #         serializer = StudentSerializer(student_obj, data = request.data)
# #         if not serializer.is_valid():
# #             return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

# #         serializer.save()
# #         return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})
# #     except Exception as e:        
# #         return Response({'status':403, 'message':'Invalid ID'})


# @api_view(['PATCH'])
# def update_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)        
#         serializer = StudentSerializer(student_obj, data = request.data, partial=True)
#         if not serializer.is_valid():        
#             return Response({"status":403, "errors":serializer.errors , "message": "Something went sent"})

#         serializer.save()
#         return Response({"status":200, "payload": serializer.data, "message": "Your data is saved"})
#     except Exception as e:        
#         print(e) 
#         return Response({'status':403, 'message':'Invalid ID'})
    

# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_obj = Student.objects.get(id=id)  
#         student_obj.delete()
#         return Response({"status":200, "message": "Your data is deleted"})

#     except Exception as e:
#         return Response({'status':403, 'message':'Invalid ID'})

