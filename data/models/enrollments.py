from django.db import models
from .student import Student
from .course import Course


class Enrollment(models.Model):
    student_id = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollments"
    )
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrollments"
    )
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)  # True, Pago; False, Pendente

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = ("student_id", "course_id")

    def __str__(self):
        status = "Pago" if self.status else "Pendente"
        return f"Matricula de {self.student_id.name} em {self.course_id.name}. {status}"
