from django.urls import path
from .views import SignUp
from django.contrib.auth import views as auth_views


app_name = 'account'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]