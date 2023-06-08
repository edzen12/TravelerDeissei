from django.urls import path

from .views import UserLoginInView, UserSingInView, Register, Login, logout

urlpatterns = [
    path('login-in/', UserLoginInView.as_view(), name='login_in'),
    path('register/', Register.as_view(), name='register'),
    path('auth-login/', Login.as_view(), name="login"),
    path('sing-in/', UserSingInView.as_view(), name='sing_in'),
    path('logout/', logout, name='logout'),
]
