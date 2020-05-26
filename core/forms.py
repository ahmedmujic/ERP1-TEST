from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from .models import User

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


class Signup_Form(SignupForm):
    def __init__(self, *args, **kwargs):
        super(Signup_Form, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(required=True)
        self.fields['last_name'] = forms.CharField(required=True)
        # self.fields['location'] = forms.CharField(required=True)
        # self.fields['bio'] = forms.CharField(required=True)
        # self.fields['birth_date'] = forms.CharField(required=True)

    # first_name = forms.CharField(max_length=20)
    # last_name = forms.CharField(max_length=30)
    bio = forms.CharField(max_length=30)
    location = forms.CharField(max_length=30)
    birth_date = forms.DateField(widget=forms.SelectDateWidget())

    def save(self, request):
        username = self.cleaned_data['username'],
        first_name = self.cleaned_data['first_name'],
        last_name = self.cleaned_data['last_name'],
        location = self.cleaned_data['location'],
        bio = self.cleaned_data['bio'],
        birth_date = self.cleaned_data['birth_date']
        user = super(Signup_Form, self).save(request)
        # user2.save()
        print(username)
        print(first_name)
        print(last_name)
        print(location)
        print(bio)
        print(birth_date)
        # print(user)
        print(user2)
        return user2
        # user.birth_date = self.cleaned_data['birth_date']
        # user = super(Signup_Form, self).save(request)
        # user.phone = self.cleaned_data['phone']
        # return user
