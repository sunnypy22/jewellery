from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as djangoview
from . import views

urlpatterns = [
    path('account/', views.account, name="account"),
    path('address/', views.address, name="address"),
    path('signup/', views.signup, name="signup"),
    path('signin/', djangoview.LoginView.as_view(template_name='account/signin.html'), name='signin'),
    path('logout/', djangoview.LogoutView.as_view(), name='logout'),
    # Reset Password
    path('password-change/', djangoview.PasswordChangeView.as_view(template_name='account/change_password.html'),
         name='password_change'),
    path('password_change/done/',
         djangoview.PasswordChangeDoneView.as_view(template_name='account/password_changed_done.html'),
         name='password_change_done'),
    # Forgot Password
    path('password-reset/',
         djangoview.PasswordResetView.as_view(template_name='account/password_reset.html',
                                              subject_template_name='account/password_reset_subject.txt',
                                              email_template_name='account/password_reset_email.html'),
         name='password_reset'),
    path('password-reset/done/',
         djangoview.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done', ),
    path('password-reset-confirm/<uidb64>/<token>/',
         djangoview.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         djangoview.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
]
