# Generated by Django 5.0.3 on 2024-04-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0037_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='password',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]