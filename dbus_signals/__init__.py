#!/usr/bin/env python
# vim: et ts=4 sw=4


from dbus.mainloop.glib import DBusGMainLoop
from . import services


DBusGMainLoop(set_as_default=True)
_service = services.ModelService()


def connect(model):
    _service.connect(model)
