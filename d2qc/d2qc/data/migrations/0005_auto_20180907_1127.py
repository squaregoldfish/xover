# Generated by Django 2.1.dev20180428173945 on 2018-09-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20180829_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='station_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='datatype',
            unique_together=set(),
        ),
    ]