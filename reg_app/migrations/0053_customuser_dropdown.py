# Generated by Django 5.0.3 on 2024-04-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0052_remove_product_approved_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dropdown',
            field=models.CharField(blank=True, choices=[('Address', 'Address'), ('city', 'city'), ('pincode', 'pincode'), ('mobile_no', 'mobile_no')], max_length=20, null=True),
        ),
    ]
