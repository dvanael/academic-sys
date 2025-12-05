from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from data.models import Enrollment
from typing import Any
from client.forms import EnrollmentForm


class EnrollmentCreateView(CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = "enrollment/create.html"
    success_url = reverse_lazy("index")


class EnrollmentListView(TemplateView):
    template_name = "enrollment/list.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["enrollments"] = Enrollment.objects.all()
        return context
