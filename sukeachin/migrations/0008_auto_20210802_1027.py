# Generated by Django 2.2.14 on 2021-08-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sukeachin', '0007_auto_20210802_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_specification',
            field=models.TextField(blank=True),
        ),
    ]