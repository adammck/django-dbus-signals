#!/usr/bin/env python
# vim: et ts=4 sw=4


import dbus
import dbus.service
from django.db.models import signals
from django.conf import settings


INTERFACE = settings.DBUS_INTERFACE
PATH = settings.DBUS_PATH


class ModelService(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName(INTERFACE, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, PATH)
   
         
    def connect(self, model):
        signals.post_save.connect(self._post_save, sender=model)
        signals.post_delete.connect(self._post_delete, sender=model)


    def _post_save(self, sender, instance, **kwargs):
        self.saved(sender.__name__.lower(), instance.pk)

    @dbus.service.signal(INTERFACE, signature="si")
    def saved(self, model_name, pk):
        pass


    def _post_delete(self, sender, instance, **kwargs):
        self.deleted(sender.__name__.lower(), instance.pk)

    @dbus.service.signal(INTERFACE, signature="si")
    def deleted(self, model_name, pk):
        pass
