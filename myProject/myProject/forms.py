from django import forms
from myApp.models import SubjectModel

class SubjectForm(forms.ModelForm):
    class Meta:
        model = SubjectModel
        fields = ['student', 'name', 'credit_hours', 'marks_obtained']
