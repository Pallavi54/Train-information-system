from django import forms
from train_fare.models import fare

class fare_form(forms.ModelForm):
    class Meta:
        model = fare
        fields = '__all__'
    