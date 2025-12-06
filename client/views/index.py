from django.views.generic import TemplateView
from data.models import Student, Course, Enrollment
from typing import Any


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["active_courses"] = Course.objects.filter(status=True)
        context["count_students"] = Student.objects.count()
        context["paid_enrollments"] = Enrollment.objects.filter(status=True).count()
        context["pending_enrollments"] = Enrollment.objects.filter(status=False).count()
        return context
