from django.shortcuts import render
from teach.models import Course_info as Course, Video_save
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='student:student')
def course_video(request, pk):
    video = Video_save.objects.filter(course_id=pk)
    course = Course.objects.get(id=pk)
    user = User.objects.get(id=course.user_id)
    return render(request, 'course_video.html', {'videos': video, 'course': course, 'user': user})