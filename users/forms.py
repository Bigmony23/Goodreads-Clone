from django import forms
from django.contrib.auth import get_user_model

from users.models import CustomUser


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email', 'password')

    def save(self, commit=True):
        user=super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

# class UserLoginForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','profile_picture')




