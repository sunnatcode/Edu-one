from django.urls import path
from .views import   kurslar, course_detail,   passcode
from django.views.generic.base import TemplateView
app_name = 'teach'

urlpatterns = [
    path('kurslarim/', kurslar, name='kurslarim'),
    path('course_detail/<int:pk>/', course_detail, name='course_detail'),
    path('passcode/', passcode, name='passcode'),

    path('teacher/', TemplateView.as_view(template_name='teacher.html'), name='teacher'),
    path('profile', TemplateView.as_view(template_name='profile.html'), name='profile'),
    
]