from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path('customer-register/', views.customer_register, name='customer_register'),
    path('vendor-register/', views.vendor_register, name='vendor_register'),
    path(
        'login/', auth_views.LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='account/login.html'
        ), name='customer_login'),
    path(
        'logout/', auth_views.LogoutView.as_view(
            template_name='account/index.html'
        ), name='logout'),
    path(
        'ChangePersonalInfo/', views.ChangePersonalInfo, name='change_personal_info'
    ),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='account/reset_password.html'),
         name='reset_password'),
    path('forget-password/', views.forget_password, name='forget_password')

]
