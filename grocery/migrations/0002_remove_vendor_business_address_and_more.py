# Generated by Django 5.1.2 on 2024-11-09 12:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='business_address',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='business_name',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='contact_number',
        ),
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='vendor',
            name='is_vendor',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
