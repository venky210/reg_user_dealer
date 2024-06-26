# Generated by Django 5.0.3 on 2024-03-31 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0015_alter_customuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('dealer', 'Dealer')], default='user', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
