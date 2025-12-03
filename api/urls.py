from django.urls import path, include
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r"students", viewsets.StudentViewSet, "student")
router.register(r"courses", viewsets.CourseViewSet, "course")


urlpatterns = [
    path(r"", include(router.urls)),
]
