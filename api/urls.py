from django.urls import path, include
from rest_framework import routers
from . import viewsets
from . import views

router = routers.DefaultRouter()
router.register(r"students", viewsets.StudentViewSet, "student")
router.register(r"courses", viewsets.CourseViewSet, "course")


urlpatterns = [
    path(r"", include(router.urls)),
    path("enrollments/create/", views.EnrollmentCreateView.as_view()),
    path("enrollments/<int:enrollment_id>/pay/", views.EnrollmentPayView.as_view()),
    path(
        "students/<int:student_id>/enrollments/", views.StudentEnrollmentsView.as_view()
    ),
]
