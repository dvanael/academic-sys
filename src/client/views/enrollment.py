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

        sql = """
            SELECT
                s.id,
                s.name,
                SUM(CASE WHEN e.status = TRUE THEN c.enrollment_fee ELSE 0 END) AS paid_total,
                SUM(CASE WHEN e.status = FALSE THEN c.enrollment_fee ELSE 0 END) AS pending_total
            FROM student s
            LEFT JOIN enrollment e ON e.student_id = s.id
            LEFT JOIN course c ON e.course_id = c.id
            GROUP BY s.id, s.name
            ORDER BY s.name;
        """

        payments = Student.objects.raw(sql)
        context["payments"] = payments
        return context
