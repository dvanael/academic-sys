from rest_framework import serializers
from data.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ["id", "student_id", "course_id", "enrollment_date", "status"]
