# Generated by Django 4.2.4 on 2023-12-08 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_baseuser_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='pin',
        ),
    ]
