# Generated by Django 3.1.2 on 2021-04-23 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bill', '0013_auto_20210116_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemodel',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_name', to='Bill.productmodel'),
        ),
    ]
