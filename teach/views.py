from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate
from .forms import Teach_form, Course_info, Video_save_form
from django.contrib import messages 
from .models import Categoryes, Course_info as Course, Video_save

# Create your views here.


def passcode(request):
    if request.POST:
        passcode = request.POST['passcode']
        if passcode == 'pdp@2021':
            return redirect('teach:teacher')
    return render(request, 'passcode.html', {})


@login_required
def kurslar(request):
    categoryInfo = Categoryes.objects.all()
    courses = Course.objects.filter(user_id=request.user.id)
    form = Course_info()
    if request.POST:
        name = request.POST['name']
        category = request.POST['category']
        about = request.POST['about']
        image = request.FILES['image']
        course = Course(name=name, category_name=category, image=image, about=about, user=request.user)
        course.save()
        return redirect('teach:kurslarim')       
    return render(request, 'kurslarim.html', {'categoryes': categoryInfo, 'courses': courses})      



@login_required
def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    video = Video_save.objects.filter(course_id=pk)

    if request.POST:
        form = Video_save_form(data=request.POST, files=request.FILES)
        name = request.POST['name']
        about = request.POST['about']
        order = request.POST['order']
        image = request.FILES['image']
        video = request.FILES['video']
        Video = Video_save(name=name, about=about, image=image, order=order, video=video, course_id=pk)
        Video.save()
        return redirect('teach:course_detail', pk)
    return render(request, 'course_detail.html', {'course': course,  'videos': video})



