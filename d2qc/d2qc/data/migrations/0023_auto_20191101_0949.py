# Generated by Django 2.1.dev20180428173945 on 2019-11-01 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_depth_sigma4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatypename',
            name='data_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_type_names', to='data.DataType'),
        ),
    ]
