# Generated by Django 3.2.8 on 2022-07-21 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0010_remove_video_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='caption',
            new_name='title',
        ),
    ]
