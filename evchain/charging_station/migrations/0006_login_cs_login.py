# Generated by Django 4.2.4 on 2023-11-05 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charging_station', '0005_charging_station_join_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='cs_login',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='charging_station.charging_station'),
        ),
    ]
