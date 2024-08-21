from django import forms
from djform.models.models import FormModel


class InputForms(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'
