# Generated by Django 5.1.7 on 2025-03-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_grounds'),
    ]

    operations = [
        migrations.CreateModel(
            name='groundSlotsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotId', models.CharField(max_length=50, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('weatherReport', models.CharField(max_length=100, null=True)),
                ('groundName', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'groundSlotsModel',
            },
        ),
    ]
