# Generated by Django 5.0.3 on 2024-03-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0004_customuser_dealer_customuser_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='dealer',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'User')], default=True, max_length=20),
        ),
    ]
