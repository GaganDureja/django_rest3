from rest_framework import serializers
from .models import *



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
    

class CategorySerializer(serializers.Serializer):    
    
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.Serializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = '__all__'