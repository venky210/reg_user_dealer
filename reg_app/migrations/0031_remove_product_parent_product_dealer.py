# Generated by Django 5.0.3 on 2024-04-03 15:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0030_alter_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='parent',
        ),
        migrations.AddField(
            model_name='product',
            name='dealer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]