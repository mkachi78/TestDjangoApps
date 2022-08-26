from django.urls import path
from UserAdmin.views import login_request

urlpatterns = [
    path('login/', login_request, name='UserLogin')
]