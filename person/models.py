#!/usr/bin/env python
# vim: et ts=4 sw=4


from django.db import models


class Person(models.Model):
    name   = models.CharField("First Name", max_length=30)
    height = models.IntegerField("Height (cm)", null=True, blank=True)
    weight = models.IntegerField("Weight (kg)", null=True, blank=True)
