# Generated by Django 4.0.2 on 2022-03-13 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]