from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .forms import ForgotPasswordForm, RestorePasswordForm
from .models import Code
from .utils import send_email_thread


def forgot_password_view(request):

    form = ForgotPasswordForm()

    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']

            user = User.objects.filter(username=username).first()

            if user:

                code = Code.objects.create(user=user)

                subject = "Parolni tiklash"
                message = f"Code: {code.code}"

                send_email_thread(
                    subject,
                    message,
                    [user.email]
                )

                return redirect('restore_password')

    context = {
        'form': form
    }

    return render(request, 'forgot_password.html', context)

def restore_password_view(request):

    form = RestorePasswordForm()

    if request.method == 'POST':
        form = RestorePasswordForm(request.POST)

        if form.is_valid():

            user = form.cleaned_data['user']
            new_password = form.cleaned_data['new_password']
            code = form.cleaned_data['code']

            user.set_password(new_password)
            user.save()

            Code.objects.filter(code=code).delete()

            return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'restore_password.html', context)

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )
        login(request, user)
        return redirect('book_list')

    return render(request, 'account/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('book_list')

    return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

