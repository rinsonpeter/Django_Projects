# Generated by Django 3.1.2 on 2021-01-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0008_auto_20210106_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='bill_number',
            field=models.CharField(max_length=120),
        ),
    ]