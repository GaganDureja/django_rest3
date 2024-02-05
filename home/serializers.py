from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ['name','age']
        # exclude = ['id']
        fields = '__all__'

    def validate(self, data):
        if data.get('age'):
            if data['age'] < 18:
                raise serializers.ValidationError({"error": "Age can't be less than 18"})
        # return super().validate(attrs)
        

        if data.get('name'):           
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error": "Name cannot contain numbers"})


        return data
    

class CategorySerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Category
        fields = '__all__'
    


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'

        # if we want some fields of category and ignore some of them
        # depth = 1