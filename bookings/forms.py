from .models import Booking
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('reference', 'date', 'time', 'group_size',)
        widgets = {
            'reference': forms.TextInput
            (attrs={'class': 'form-control'}),
            'date': DateInput(attrs={'class': 'form-control'}),
            'time': TimeInput(attrs={'class': 'form-control'}),
            'group_size': forms.NumberInput(attrs={'class': 'form-control'}),
        }
