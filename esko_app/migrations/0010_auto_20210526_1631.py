# Generated by Django 3.2.3 on 2021-05-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esko_app', '0009_rename_user_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
