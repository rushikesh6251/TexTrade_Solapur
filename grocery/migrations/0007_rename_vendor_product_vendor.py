# Generated by Django 5.1.2 on 2024-11-15 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0006_product_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Vendor',
            new_name='vendor',
        ),
    ]
