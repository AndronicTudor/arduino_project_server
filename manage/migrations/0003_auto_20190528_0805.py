# Generated by Django 2.2.1 on 2019-05-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0002_auto_20190516_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='lat',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='lon',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]
