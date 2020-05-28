from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        user.username = data.get('username')
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.birth_date = data['birth_date']
        user.location = data['location']
        user.bio = data['bio']
        user.photo = data['photo']
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user
