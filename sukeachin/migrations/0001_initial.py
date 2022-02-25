# Generated by Django 2.2.14 on 2021-07-31 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('category_created_date', models.DateTimeField(auto_now_add=True)),
                ('category_updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField(max_length=100)),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sukeachin.Category')),
            ],
        ),
    ]