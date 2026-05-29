from django.core.mail import send_mail
from threading import Thread

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from accounts.models import UserRole

class EmailThread(Thread):

    def __init__(self, subject, message, recipient_list):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list
        Thread.__init__(self)

    def run(self):
        send_mail(
            self.subject,
            self.message,
            None,
            self.recipient_list
        )

def send_email_thread(subject, message, recipient_list):
    EmailThread(subject, message, recipient_list).start()


def login_required_custom(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:  # sorov.foydalanuvchi
            return func(request, *args, **kwargs)
        else:
            return redirect(settings.LOGIN_URL)

    return inner


def is_poster(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == UserRole.POSTER:
            return func(request, *args, **kwargs)
        else:
            raise PermissionDenied('Forbidden')

    return inner

def is_moderator(func):
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == UserRole.MODERATOR:
            return func(request, *args, **kwargs)
        else:
            raise PermissionDenied('Forbidden')

    return inner