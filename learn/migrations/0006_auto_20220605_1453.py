# Generated by Django 3.2.8 on 2022-06-05 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
