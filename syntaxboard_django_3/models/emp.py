# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=9, blank=True, null=True)
    mgr = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    commission = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    deptno = models.ForeignKey('Dept', models.DO_NOTHING, db_column='deptno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp'
