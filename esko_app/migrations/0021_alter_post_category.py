# Generated by Django 3.2.3 on 2021-05-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esko_app', '0020_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('sell', 'sell'), ('find', 'find'), ('services', 'services/rent'), ('swap', 'swap')], max_length=8),
        ),
    ]
