# Generated by Django 5.0.3 on 2024-03-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0006_remove_customuser_role_alter_customuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dealer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.BooleanField(default=False),
        ),
    ]
