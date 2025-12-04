from django.urls import reverse_lazy
from django.views.generic import CreateView
from data.models import Student
from client.forms import StudentForm


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student/create.html"
    success_url = reverse_lazy("index")
