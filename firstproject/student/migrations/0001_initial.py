# Generated by Django 3.1.2 on 2020-11-03 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_email', models.CharField(max_length=120, unique=True)),
                ('stud_pwd', models.CharField(max_length=120)),
            ],
        ),
    ]
