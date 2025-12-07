from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    email = models.EmailField(unique=True, verbose_name="Email")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    admission_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Data de Inscrição"
    )

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name
