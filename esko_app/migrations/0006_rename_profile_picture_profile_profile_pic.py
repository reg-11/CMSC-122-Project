# Generated by Django 3.2.3 on 2021-05-25 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esko_app', '0005_alter_profile_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_picture',
            new_name='profile_pic',
        ),
    ]
