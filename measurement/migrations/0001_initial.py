# Generated by Django 5.1.2 on 2024-10-13 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Датчик',
                'verbose_name_plural': 'Датчики',
                'db_table': 'sensors',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.SmallIntegerField(verbose_name='Температура')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurement', to='measurement.sensor')),
            ],
            options={
                'verbose_name': 'Измерение',
                'verbose_name_plural': 'Измерения',
                'db_table': 'measurements',
            },
        ),
    ]
