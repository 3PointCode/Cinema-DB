from django import forms

class SeatReservationForm(forms.Form):
    email = forms.EmailField(label="Adres email:", max_length=100)
    seat = forms.CharField(widget=forms.HiddenInput())