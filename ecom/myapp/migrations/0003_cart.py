# Generated by Django 5.1.4 on 2025-01-15 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.regform')),
            ],
        ),
    ]
