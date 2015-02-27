from django import forms
from .models import LineModel
from .models import DonutModel


class LineForm(forms.ModelForm):
    class Meta:
        model = LineModel


class DonutForm(forms.ModelForm):
    class Meta:
        model = DonutModel
