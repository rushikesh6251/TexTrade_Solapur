# Generated by Django 5.1.2 on 2024-11-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
