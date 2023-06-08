from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import UserSingInForm
from django.contrib.auth.models import User, auth

from django.contrib import messages

class UserLoginInView(View):
    def get(self, request):
        return render(request, 'profile/login.html', locals())


class UserSingInView(View):
    def get(self, request):
        print(request.POST)
        return render(request, 'profile/sing.html', locals())


class Register(View):
    def post(self, request):
        if request.method == "POST":
            first_name = request.POST['first_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Такой пользователь уже существует")
                    return redirect("sing_in")
                else:
                    user = User.objects.create_user(username=username, password=password1, first_name=first_name)
                    user.save()
                    return redirect("login_in")
            else:
                messages.info(request, "Пароли не совподают")
                return redirect("sing_in")
            
            return redirect("homepage")


class Login(View):
    def post(self, request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, "Неправильный пароль или логин")
                return redirect("login_in")
        else:
            messages.info(request, "Ошибка")
            return redirect("login_in")
        

def logout(request):
    auth.logout(request)
    return redirect('homepage')
