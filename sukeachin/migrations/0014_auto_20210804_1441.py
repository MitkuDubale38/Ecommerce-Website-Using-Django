# Generated by Django 2.2.14 on 2021-08-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sukeachin', '0013_auto_20210804_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
