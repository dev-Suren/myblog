# Generated by Django 4.0.2 on 2022-04-07 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_comment_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
    ]
