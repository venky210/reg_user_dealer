# Generated by Django 5.0.3 on 2024-04-02 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_app', '0018_remove_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('qty', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.ImageField(upload_to='')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reg_app.product')),
            ],
        ),
    ]
