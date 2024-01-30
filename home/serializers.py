from rest_framework import serializers
from .models import Student



class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ['name','age']
        # exclude = ['id']
        fields = '__all__'

    def validate(self, data):
        if data['age'] < 18  and data['age']:
            raise serializers.ValidationError({"error": "Age can't be less than 18"})
        # return super().validate(attrs)
        

        if data['name']:           
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({"error": "Name cannot contain numbers"})


        return data