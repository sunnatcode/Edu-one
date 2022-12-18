# Generated by Django 4.0.1 on 2022-02-15 13:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0003_course_info_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AddField(
            model_name='video_save',
            name='post',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]