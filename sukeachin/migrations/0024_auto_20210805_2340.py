# Generated by Django 2.2.14 on 2021-08-05 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sukeachin', '0023_auto_20210805_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-Orderd_date']},
        ),
    ]
