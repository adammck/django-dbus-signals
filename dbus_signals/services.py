#!/usr/bin/env python
# vim: et ts=4 sw=4


import dbus
import dbus.service
from django.db.models import signals
from django.conf import settings


class ServiceBase(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName(self.interface, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, self.path)


def connect(model):
    name      = model.__name__
    cls_name  = "%sService" % (name)
    interface = "%s.%s"     % (settings.DBUS_INTERFACE, name)
    path      = "%s/%s"     % (settings.DBUS_PATH, name)

    # we can't use lambda functions inline, because the python-dbus api
    # uses the __name__ of the method as the dbus signal name. what.
    def saved(self, pk): return None
    def deleted(self, pk): return None

    # generate the class
    cls = type(cls_name, (ServiceBase,), {
        "saved":     saved,
        "deleted":   deleted,
        "interface": interface,
        "path":      path
    })

    # decorate the signal methods, to turn them into dbus signal emitters
    # this seems wrong, but the python-dbus api doesn't appear to provide
    # any way to do this without using the decorator.
    cls.saved   = dbus.service.signal(interface, signature="i")(cls.saved)
    cls.deleted = dbus.service.signal(interface, signature="i")(cls.deleted)

    # we're done building the class, so instantiate it once.
    service = cls()

    # hook up the django signal handlers, to fire the dbus signals
    signals.post_save.connect(lambda **kwargs: service.saved(kwargs["instance"].pk), weak=False, sender=model)
    signals.post_delete.connect(lambda **kwargs: service.deleted(kwargs["instance"].pk), weak=False, sender=model)
