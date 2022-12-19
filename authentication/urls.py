from unicodedata import name
from django.urls import path
from .views import  student_register,  student_login, logout, teach_register, teach_login
app_name = 'auth'
urlpatterns = [
    path('teach_register/', teach_register, name='teach_register'),
    path('teach_login/', teach_login, name='teach_login'),
    path('student_register/', student_register, name='student_register'),
    path('student_login/', student_login, name='student_login'),
    path('logout/', logout, name='logout'),

]