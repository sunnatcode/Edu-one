
from django.urls import path
from django.views.generic.base import TemplateView
from .views import course_video
app_name = 'student'
urlpatterns = [
    path('student', TemplateView.as_view(template_name='student.html'), name='student'),
    path('course_video/<int:pk>/', course_video, name='course_video'),
]