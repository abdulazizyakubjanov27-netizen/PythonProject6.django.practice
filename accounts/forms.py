from django.contrib.auth import authenticate
from accounts.models import User
from django import forms
from django.utils import timezone

from .models import Code


class RegisterForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 're_password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError("Passwords don't match")
        self.cleaned_data.pop('re_password')
        return self.cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            **self.cleaned_data
        )
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError("User not found")

        return {'user': user}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=150)

# Restore Password Form

class RestorePasswordForm(forms.Form):
    code = forms.IntegerField()
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        code = cleaned_data.get('code')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        code_obj = Code.objects.filter(code=code).first()

        if not code_obj:
            raise forms.ValidationError("Code noto'g'ri")

        if code_obj.expired_date < timezone.now():
            raise forms.ValidationError("Code eskirgan")

        if new_password != confirm_password:
            raise forms.ValidationError("Parollar bir xil emas")

        cleaned_data['user'] = code_obj.user

        return cleaned_data
