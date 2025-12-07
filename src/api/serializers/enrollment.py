from rest_framework import serializers
from data.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    enrollment_date = serializers.DateTimeField(format="%d/%m/%Y %H:%M")

    class Meta:
        model = Enrollment
        fields = ["id", "student", "course", "enrollment_date", "status"]
