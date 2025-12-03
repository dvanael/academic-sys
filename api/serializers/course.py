from rest_framework import serializers
from data.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "total_hours", "enrollment_fee", "status"]
