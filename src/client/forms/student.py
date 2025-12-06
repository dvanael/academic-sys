from django import forms
from data.models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ["name", "cpf", "email"]
