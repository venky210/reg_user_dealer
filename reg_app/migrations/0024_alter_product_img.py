# Generated by Django 5.0.3 on 2024-04-03 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0023_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.URLField(max_length=100),
        ),
    ]