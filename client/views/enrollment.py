from django.urls import reverse_lazy
from django.views.generic import CreateView
from data.models import Enrollment
from client.forms import EnrollmentForm


class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = "enrollment/create.html"
    success_url = reverse_lazy("index")
