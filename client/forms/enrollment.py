from django import forms
from data.models import Enrollment


class EnrollmentForm(forms.ModelForm):

    class Meta:
        model = Enrollment
        fields = ["student_id", "course_id", "status"]
