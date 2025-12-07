from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    total_hours = models.IntegerField(verbose_name="Carga Horária")
    enrollment_fee = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Valor da Matrícula"
    )
    status = models.BooleanField(
        default=False, verbose_name="Status"
    )  # True, Ativo; False, Inativo

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name
