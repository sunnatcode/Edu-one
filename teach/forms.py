
from django.forms import ModelForm
from .models import Teach_register, Course_info, Video_save


class Teach_form(ModelForm):
    class Meta:
        model = Teach_register
        fields = '__all__'

class Course_info(ModelForm):
    class Meta:
        model = Course_info
        fields = '__all__'


class Video_save_form(ModelForm):
    class Meta:
        model = Video_save
        fields  = '__all__'


