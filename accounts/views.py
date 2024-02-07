from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView


from .helpers import *


class RegisterView(APIView):

    def post(self, request):
        try:
            serializer = UserSerializer(data = request.data)

            if not serializer.is_valid():
                return Response({
                    'status':403,
                    'errors': serializer.errors
                })
            
            serializer.save()

            return Response({'status':200, 'message': 'An otp sent to your email and phone'})

        except Exception as e:
            print(e)
            return Response({'status':404, 'message': 'Something went wrong'})
        


class VerifyOtp(APIView):

    def post(self, request):
        try:
            data = request.data
            user_obj = User.objects.get(phone = data.get('phone'))
            otp = data.get('otp')

            if user_obj.otp == otp:
                user_obj.is_phone_verified = True
                user_obj.save()
                return Response({'status':200, 'message':'Your phone is verified'})
            
            return Response({'status':403, 'message':'OTP incorrect'})

        except Exception as e:
            print(e)
            return Response({'status':404, 'message':'Something went wrong'})


    def patch(self, request):
        try:
            data = request.data
            user_obj = User.objects.filter(phone= data.get('phone'))
            if not user_obj.exists():
                return Response({'status':404, 'message':'Mobile number not valid'})


            if send_otp_to_mobile(data.get('phone'), user_obj[0]):
                return Response({'status':200, 'message':'New otp sent'})

            return Response({'status':404, 'message':'try after few seconds'})


        except Exception as e:
            print(e)
            return Response({'status':404, 'message':'Something went wrong'})
