from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as sign_out
from django.shortcuts import render, redirect
from authentication.models import Register
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from teach.models import Video_save, Course_info
# Create your views here.


def teach_register(request):
    if request.POST:
        username = request.POST['username']
        surname = request.POST['surname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone = request.POST['phone']
        if not password.__eq__(confirm_password):
            messages.error(request, message='Error password', extra_tags='danger')
        else:
            user = User(username=username, last_name=surname, password=make_password(password), is_staff=1)    
            user.save()
            return redirect('auth:teach_login')
    return render(request, 'teach_reg.html', {})



def teach_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        a = int(1)
        if user and user.is_staff == 1:
            auth_login(request, user)
            return redirect('teach:profile')
        else:
            messages.error(request, message='Wat`s wrong', extra_tags='danger')    
    return render(request, 'teach_login.html', {})






def student_register(request):
    if request.POST:
        password = request.POST.get('password')
        number = request.POST.get('number')
        username = request.POST.get('username')
        user = User(password=make_password(password), username=username)
        user.save()
        register = Register(user=user, phone=number)
        return render(request, 'login.html', {'register': request.user})
    return render(request, 'register.html', {})   


def student_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff == 0:
            auth_login(request, user)
            return redirect('main:kurslar')
        messages.error(request, message='Username or password incorrect !', extra_tags="danger")   
    return render(request, 'login.html', {})     


def logout(request):
    sign_out(request)
    return redirect(reverse_lazy('main:main'))


