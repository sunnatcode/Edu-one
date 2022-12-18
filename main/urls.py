from django.urls import path
from .views import kurslar, main, videoss
app_name = 'main'
urlpatterns = [
    path('kurslar/', kurslar, name='kurslar'),
    path('', main, name='main'),
    path('videos/<int:pk>/', videoss, name='videoss')
]