from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from allauth.account.forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
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


class Signup_Form(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super(Signup_Form, self).__init__(*args, **kwargs)
    #     self.fields['first_name'] = forms.CharField(required=True)
    #     self.fields['last_name'] = forms.CharField(required=True)
    #     # self.fields['location'] = forms.CharField(required=True)
    #     # self.fields['bio'] = forms.CharField(required=True)
    #     # self.fields['birth_date'] = forms.CharField(required=True)

    # class Meta:
    #     model = User
    #     fields = ('user12', 'location', 'birth_date')

    # first_name = forms.CharField(max_length=20, widget=forms.TextInput(
    #     attrs={"class": "input_text", }), required=True,)
    # last_name = forms.CharField(max_length=30, widget=forms.TextInput(
    #     attrs={"class": "input_text", }), required=True,)
    birth_date = forms.DateField(widget=forms.TextInput(
        attrs={"id": "date", "type": "date"}), required=True, )
    # location = forms.CharField(max_length=30, widget=forms.TextInput(
    #     attrs={"class": "input_text", }), required=True,)
    # bio = forms.CharField(max_length=30, widget=forms.TextInput(
    #     attrs={"class": "input_text", }), required=True,)

    # class Meta:
    #     model = User
    #     exclude = [" "]

    # def signup(self, request, user):
    #     # user.first_name = self.cleaned_data['first_name']
    #     # user.last_name = self.cleaned_data['last_name']
    #     # # user.save()
    #     # up = user.profile
    #     user.save()
    #     user.username = self.cleaned_data['username']
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.birth_date = self.cleaned_data['birth_date']
    #     user.location = self.cleaned_data['location']
    #     user.bio = self.cleaned_data['bio']
    #     user.save()
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',
                  'bio', 'location', 'birth_date', 'sifra', 'photo')
        widgets = {'sifra': forms.TextInput(
            attrs={'data-mask': "S0S 0S0"})}

    def signup(self, request, user):
        pass
    # username = self.cleaned_data['username'],
        # first_name = self.cleaned_data['first_name'],
        # last_name = self.cleaned_data['last_name'],
        # location = self.cleaned_data['location'],
        # bio = self.cleaned_data['bio'],
        # birth_date = self.cleaned_data['birth_date']
        # user = super(Signup_Form, self).save(request)
        # user2 = User.objects.create(
        #     user12=user, location=location, birth_date=birth_date)
        # user2.save()
        # print(username)
        # print(first_name)
        # print(last_name)
        # print(location)
        # print(bio)
        # print(birth_date)
        # # print(user)
        # # print(user)
        # return user2
        # user.birth_date = self.cleaned_data['birth_date']
        # user = super(Signup_Form, self).save(request)
        # user.phone = self.cleaned_data['phone']
        # return user
