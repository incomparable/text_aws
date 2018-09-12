# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=30, null=True)
    d_age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    place = models.CharField(max_length=50, null=True)
    specification = models.CharField(max_length=50, null=True)
    cabin_no = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)

    contact = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(unique=False, null=True, blank=True, db_index=True)

    class Meta:
        unique_together = ["cabin_no", "email", "contact"]


class Patient(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    d_id = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=30, null=True)
    p_age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    place = models.CharField(max_length=50, null=True)
    problem = models.CharField(max_length=50, null=True)
    birth_date = models.DateField(null=True)
    Doctor_name  = models.CharField(max_length=30, null=True)
    cabin_no = models.IntegerField(null=True)
    
    contact = models.CharField(max_length=30, null=True)
    d_contact = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(unique=False, null=True, blank=True, db_index=True)

    class Meta:
        unique_together = ["cabin_no", "email", "contact"]
