# Generated by Django 3.2.3 on 2021-05-21 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_alter_profile_model_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_model',
            name='profile_pic',
            field=models.ImageField(upload_to='images'),
        ),
    ]
