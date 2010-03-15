#!/usr/bin/env python
# vim: et ts=4 sw=4


DATABASE_ENGINE = "sqlite3"
DATABASE_NAME   = "db.sqlite3"


DBUS_INTERFACE = "com.adammck.dbus_example"
DBUS_PATH      = "/com/adammck/dbus_example"


INSTALLED_APPS = (
    "dbus_signals",
    "dbus_example")
