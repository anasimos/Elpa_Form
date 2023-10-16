from django import forms 
from django.forms import ModelForm
from .models import Reading

# Creat form

class ReadingForm(ModelForm):
    class Meta:
        model= Reading
        fields = ("BPNumber", "fullname", "accNumber", "meterReading")
        widget={
            'BPNumber':forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'BP Number'}),
            'fullname':forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Owner Name'}),
            'accNumber':forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Account Number'}),
            'meterReading':forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Meter Reading'}),
        }
        # labels={
        #     "BPNumber": "Enter BP Number",
        #     "fullname":"Owner Name",
        #     "accNumber":"Account Number",
        #     "meterReading":"Meter Reading",
        # }
        