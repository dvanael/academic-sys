from django.urls import reverse_lazy
from django.views.generic import CreateView
from data.models import Course
from client.forms import CourseForm


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "course/create.html"
    success_url = reverse_lazy("index")
