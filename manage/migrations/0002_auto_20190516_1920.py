# Generated by Django 2.2.1 on 2019-05-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='humidity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='light',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='temperature',
            field=models.IntegerField(),
        ),
    ]
