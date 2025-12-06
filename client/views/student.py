from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from typing import Any
from data.models import Student
from client.forms import StudentForm


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/create.html"
    success_url = reverse_lazy("index")


class StudentHistoryView(DetailView):
    model = Student
    template_name = "student/history.html"
    context_object_name = "student"
