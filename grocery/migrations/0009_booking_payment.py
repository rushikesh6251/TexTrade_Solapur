# Generated by Django 5.1.6 on 2025-02-21 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0008_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='grocery.payment'),
        ),
    ]
