from django.shortcuts import render
from teach.models import Course_info, Video_save
from django.contrib.auth.models import User
# Create your views here.


def main(request):
    return render(request, 'main.html', {'register': request.user})



def kurslar(request):
    courses = Course_info.objects.all()
    video = Video_save.objects.all()
    user = User.objects.all()
    return render(request, 'kurslar.html', {'courses': courses, 'user': user})    

def videoss(request, pk):
    video = Video_save.objects.get(id=pk)
    x = video.course_id
    Video = Video_save.objects.filter(course_id=x)
    return render(request, 'videos.html', {'video': video, 'Videos': Video})