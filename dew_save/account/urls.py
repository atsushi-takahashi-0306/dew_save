from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUp
from .views import Delete_user
from .views import Update_user


app_name = 'account'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete_user/<int:pk>/', Delete_user.as_view(), name='delete'),
    path('update_user/<int:pk>/', Update_user.as_view(), name='update'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'), 
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'), 
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'), 
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
]