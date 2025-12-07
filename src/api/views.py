from django.db.models import Count
from rest_framework import views
from rest_framework.response import Response
from .serializers import EnrollmentSerializer
from data.models import Course, Enrollment


class EnrollmentCreateView(views.APIView):
    def post(self, request):
        serializer = EnrollmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class StudentEnrollmentsView(views.APIView):
    def get(self, request, student_id):
        enrollments = Enrollment.objects.filter(student=student_id)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)


class EnrollmentPayView(views.APIView):
    def post(self, request, enrollment_id):
        try:
            enrollment = Enrollment.objects.get(id=enrollment_id)
        except Enrollment.DoesNotExist:
            return Response({"error": "Enrollment not found."}, status=404)

        enrollment.status = True  # Pago
        enrollment.save()
        serializer = EnrollmentSerializer(enrollment, many=False)
        return Response(serializer.data)


class ReportEnrollmentsPerCourse(views.APIView):
    def get(self, request):
        data = Course.objects.annotate(total=Count("enrollment")).values(
            "id", "name", "total"
        )
        return Response(data)
