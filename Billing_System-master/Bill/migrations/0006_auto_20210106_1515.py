# Generated by Django 3.1.2 on 2021-01-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0005_auto_20210106_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
