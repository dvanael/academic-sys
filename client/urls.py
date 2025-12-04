from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("alunos/cadastrar/", views.StudentCreateView.as_view(), name="student-create"),
]
