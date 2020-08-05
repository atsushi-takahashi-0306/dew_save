from django.urls import path
from .views import SignUp
from django.contrib.auth import views as auth_views
from .views import Delete_user
from .views import Update_user


app_name = 'account'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('delete_user/<int:pk>/', Delete_user.as_view(), name='delete'),
    path('update_user/<int:pk>/', Update_user.as_view(), name='update'),
]