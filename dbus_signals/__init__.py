#!/usr/bin/env python
# vim: et ts=4 sw=4


from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)


def connect(model):
    from . import services
    services.connect(model)
