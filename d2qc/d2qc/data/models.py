from django.db import models
from django.forms import ModelForm


class DataSet(models.Model):
    class Meta:
        db_table = 'd2qc_data_sets'
        indexes = [
            models.Index(fields=['min_lat', 'max_lat', 'min_lon', 'max_lon']),
        ]
    id = models.AutoField(primary_key=True)
    expocode = models.CharField(max_length=255)
    is_reference = models.BooleanField(default=False)
    min_lat = models.DecimalField(max_digits=10, decimal_places=8, null=False)
    max_lat = models.DecimalField(max_digits=10, decimal_places=8, null=False)
    min_lon = models.DecimalField(max_digits=11, decimal_places=8, null=False)
    max_lon = models.DecimalField(max_digits=11, decimal_places=8, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class DataType(models.Model):
    class Meta:
        db_table = 'd2qc_data_types'
        unique_together = ('identifier', 'original_label')
    id = models.AutoField(primary_key=True)
    data_unit = models.ForeignKey(
        'DataUnit',
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )
    identifier = models.CharField(max_length=20, default='', blank=True)
    prefLabel = models.CharField(max_length=255, default='', blank=True)
    altLabel = models.CharField(max_length=255, default='', blank=True)
    definition = models.CharField(max_length=255, default='', blank=True)
    original_label = models.CharField(max_length=20, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class DataUnit(models.Model):
    class Meta:
        db_table = 'd2qc_data_units'
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=20, default='', blank=True)
    prefLabel = models.CharField(max_length=255, default='', blank=True)
    altLabel = models.CharField(max_length=255, default='', blank=True)
    definition = models.CharField(max_length=255, default='', blank=True)
    original_label = models.CharField(max_length=20, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class DataPoint(models.Model):
    class Meta:
        db_table = 'd2qc_data_points'
        indexes = [
            models.Index(fields=['depth']),
            models.Index(fields=['latitude', 'longitude']),
        ]
    id = models.AutoField(primary_key=True)
    data_set = models.ForeignKey('DataSet', related_name='points', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    depth = models.DecimalField(max_digits=8, decimal_places=3)
    unix_time_millis = models.BigIntegerField()
    station_number = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class DataValue(models.Model):
    class Meta:
        db_table = 'd2qc_data_values'
    id = models.AutoField(primary_key=True)
    data_point = models.ForeignKey('DataPoint', related_name='values', on_delete=models.CASCADE)
    data_type = models.ForeignKey('DataType', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=19, decimal_places=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        if int(float(self.value)) != -999:
            super(DataValue, self).save(*args, **kwargs)
