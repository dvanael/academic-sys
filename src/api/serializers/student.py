from rest_framework import serializers
from data.models import Student


class StudentSerializer(serializers.ModelSerializer):
    admission_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M")

    class Meta:
        model = Student
        fields = ["id", "name", "email", "cpf", "admission_date"]
