# Generated by Django 4.0.2 on 2022-03-18 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_profile_is_verified_remove_profile_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='user_profile'),
        ),
    ]
