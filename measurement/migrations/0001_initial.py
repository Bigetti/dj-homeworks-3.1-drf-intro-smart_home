# Generated by Django 5.0.1 on 2024-01-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.IntegerField(verbose_name='Number of Sensor')),
                ('temperature', models.IntegerField(verbose_name='Temperature')),
                ('date_and_time', models.DateTimeField(verbose_name='Date and time of measuring')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Naimenovanie')),
                ('description', models.TextField(blank=True, null=True, verbose_name='place description')),
            ],
        ),
    ]
