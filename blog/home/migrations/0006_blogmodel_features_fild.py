# Generated by Django 4.0.2 on 2022-02-23 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='features_fild',
            field=models.BooleanField(default=False),
        ),
    ]
