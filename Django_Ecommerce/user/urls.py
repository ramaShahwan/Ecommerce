from django.urls import path
from .views import *



app_name = "user"


urlpatterns = [
    path('signup/', CustomerSignup.as_view(), name='customer-signup'),
    path('login/', CustomerLoginView.as_view(), name='customer-login'),
]