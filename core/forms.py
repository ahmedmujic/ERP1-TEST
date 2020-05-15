from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

IZBORI = (
    ('Kartica', 'Kartica'),
    ('Paypal', 'Paypal')
)


class ChartForm(forms.Form):
    ulica_adresa = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Grad', 'class': 'form-control'}))
    adresa_stana = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Adresa', 'class': 'form-control'}))
    country = CountryField().formfield(widget=CountrySelectWidget(
        attrs={'placeholder': '1234', 'class': 'custom-select d-block w-100'}))
    postal = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'id': 'zip', 'class': 'form-control', 'placeholder': 'Postanski broj'}), required=True)
    credit = forms.ChoiceField(widget=forms.RadioSelect, choices=IZBORI)

    """ def __init__(self, request):
        self.ulica_adresa = "prva"
        self.adresa_stana = "druga"
        self.isti_bill = True
        self.credit = False """
