from django.urls import path
from .views import *



app_name = "user"


urlpatterns = [
    path('signup/', CustomerSignup.as_view(), name='customer-signup'),
    path('login/', CustomerLoginView.as_view(), name='customer-login'),
    
    
    path('customer/<int:customer_id>/edit-profile/', CustomerEditProfileAPI.as_view(), name='customer-edit-profile'),
    path('update-password/<int:customer_id>/', PasswordUpdateView.as_view(), name='update_password'),
    
    
    path('customer/forgot-username/', CustomerForgotUsernameView.as_view(), name='customer-forgot-username'),

    path('forgot-password/', CustomerForgotPasswordView.as_view(), name='customer-forgot-password'),
    path('reset-password/<uidb64>/<token>/', CustomerResetPasswordView.as_view(), name='reset-password'),
    path('page-reset-password/<uidb64>/<token>/', CustomerPasswordResetFormView.as_view(), name='reset-password-form'),

]