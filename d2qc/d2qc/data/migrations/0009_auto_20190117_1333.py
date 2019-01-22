# Generated by Django 2.1.dev20180428173945 on 2019-01-17 13:33

from django.db import migrations
import os
from d2qc.data.glodap.glodap import Glodap
from glodap.util.data_type_dict import DataTypeDict
from d2qc.data.models import DataType

def add_glodap_identifiers(apps, schema_editor):
    for var in DataTypeDict:
        type_, created = DataType.objects.get_or_create(original_label=var)
        type_.identifier = DataTypeDict[var]
        type_.save()

class Migration(migrations.Migration):
    dependencies = [
        ('data', '0008_auto_20190115_1525'),
    ]

    operations = [
        migrations.RunPython(add_glodap_identifiers),
    ]