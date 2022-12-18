from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
from teach.utils.main_utils import choises

# Create your models here.





class Categoryes(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)


class Teach_register(models.Model):
    username = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    phone = models.IntegerField()


class Uploads(models.Model):
    original_name = models.CharField(max_length=300)
    content_type = models.CharField(max_length=200)
    new_name = models.CharField(max_length=200)
    path = models.CharField(max_length=500)
    code = models.CharField(max_length=200, unique=True)
    size = models.IntegerField()

    class Meta:
        db_table = 'uploads'



class Course_info(models.Model):
    from .utils import choises
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category_name = models.CharField(max_length=200, choices=choises())
    image = models.ImageField(upload_to='media/uploads/')
    about = models.CharField(max_length=200)         


class Video_save(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/uploads/')
    order = models.IntegerField()
    course_id = models.IntegerField()
    video = models.FileField(upload_to='media/uploads/')