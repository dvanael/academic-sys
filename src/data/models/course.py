from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    total_hours = models.IntegerField()
    enrollment_fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)  # True, Ativo; False, Inativo

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name
