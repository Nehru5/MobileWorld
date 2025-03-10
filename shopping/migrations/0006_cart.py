# Generated by Django 5.1.5 on 2025-02-20 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_alter_product_specification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.userprofile')),
            ],
        ),
    ]
