# Generated by Django 3.2.3 on 2021-05-26 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esko_app', '0008_alter_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
    ]
