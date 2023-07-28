from django import forms
from info.models import Students


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'course', 'admissionnumber']