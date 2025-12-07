from django.db import models
from .student import Student
from .course import Course


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="enrollments"
    )
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)  # True, Pago; False, Pendente

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = ("student", "course")

    def __str__(self):
        status = "Pago" if self.status else "Pendente"
        return f"Matricula de {self.student.name} em {self.course.name}. {status}"
