# Generated by Django 5.0.3 on 2024-04-12 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0040_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='password',
        ),
        migrations.RemoveField(
            model_name='category',
            name='username',
        ),
    ]
