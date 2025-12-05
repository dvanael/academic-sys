from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("alunos/cadastrar/", views.StudentCreateView.as_view(), name="student-create"),
    path("cursos/cadastrar/", views.CourseCreateView.as_view(), name="course-create"),
    path(
        "matriculas/cadastrar/",
        views.EnrollmentCreateView.as_view(),
        name="enrollment-create",
    ),
]
