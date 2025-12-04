from django import forms
from data.models import Course


class CoursetForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ["name", "total_hours", "enrollment_fee", "status"]
