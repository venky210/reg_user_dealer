# Generated by Django 5.0.3 on 2024-04-12 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0041_remove_category_password_remove_category_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
