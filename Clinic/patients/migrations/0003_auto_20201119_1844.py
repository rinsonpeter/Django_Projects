# Generated by Django 3.1.2 on 2020-11-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20201119_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='user',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
