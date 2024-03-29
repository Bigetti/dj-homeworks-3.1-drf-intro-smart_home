# Generated by Django 5.0.1 on 2024-01-31 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='measurement',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='date_and_time',
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='sensor_id',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor', verbose_name='Sensor'),
        ),
    ]
