# Generated by Django 5.1.7 on 2025-03-25 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_groundslotsmodel_slottimings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groundslotsmodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='groundslotsmodel',
            name='slotId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
