# Generated by Django 5.1.2 on 2024-11-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0002_remove_vendor_business_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
