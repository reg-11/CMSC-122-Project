# Generated by Django 3.2.3 on 2021-05-26 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esko_app', '0011_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='post_image',
        ),
    ]
