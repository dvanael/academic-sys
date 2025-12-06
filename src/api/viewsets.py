from rest_framework import viewsets
from .serializers import StudentSerializer, CourseSerializer
from data.models import Student, Course

# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ["get", "post", "delete", "put"]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    http_method_names = ["get", "post", "delete", "put"]
