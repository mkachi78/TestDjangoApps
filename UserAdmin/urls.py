from django.contrib.auth.views import LogoutView
from django.urls import path
from UserAdmin.views import *

urlpatterns = [
    path('login/', login_request, name='UserLogin'),
    path('register/', register, name='UserRegister'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='UserLogout')
]