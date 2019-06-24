from django import forms
from .models import Live


class LiveForm(forms.ModelForm):

    class Meta:
        model = Live
        fields = '__all__'
