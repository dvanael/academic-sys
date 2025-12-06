from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from data.models import Enrollment, Course, Student
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

        payments = []
        for s in Student.objects.all():
            enrollmets = Enrollment.objects.filter(student_id=s.id)
            paid_total = 0
            pending_total = 0
            for e in enrollmets:
                if e.status:
                    paid_total += e.course_id.enrollment_fee
                else:
                    pending_total += e.course_id.enrollment_fee
            data = {
                "name": s.name,
                "paid_total": paid_total,
                "pending_total": pending_total,
            }
            payments.append(data)
        context["payments"] = payments
        return context
