# Generated by Django 2.0.7 on 2025-04-23 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20250422_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=20),
        ),
    ]
