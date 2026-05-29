# from allauth.account.signals import password_reset
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path(
        'forgot-password/',
        forgot_password_view,
        name='forgot_password'
    ),

    path(
        'restore-password/',
        restore_password_view,
        name='restore_password'
    ),
]


