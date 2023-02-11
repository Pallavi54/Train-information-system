from django import forms
from train_info.models import train_details

class train_form(forms.ModelForm):
    class Meta:
        model = train_details
        fields = '__all__'

    # Train_id = forms.IntegerField(label="Your Train_id")
    # Train_name = forms.CharField(label="Your Train_name")
    # Origin_city = forms.CharField(label="Your Origin_city")
    # Destination_city = forms.CharField(label="Your Destination_city")
    # Departure_time = forms.TimeField(label="Your Departure_time")
    # Arrival_time = forms.TimeField(label="Your Arrival_time")