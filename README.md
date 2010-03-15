This module provides a nifty interface between Django models (via the
signal dispatcher) and D-Bus. This is handy when more than one process
is interacting with the same database, to avoid polling for changes.

WARNING: This is just a toy (for now). Don't expect it to work.


To see what's going on, monitor the d-bus. I'm only interested in the
signals being emitted by my example app here. Obviously, the interface
and path names are configurable.

    $ dbus-monitor | grep "interface=com.adammck."


In another shell, let's poke around with the database.

    $ ./manage.py shell
    Python 2.6.4 (r264:75706, Jan 25 2010, 08:55:26)
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    
    >>> from dbus_example.models import Person
    >>> Person(name="Adam Mckaig").save()


Meanwhile, back in dbus-monitor...

    signal
      sender=:1.54 -> 
      dest=(null destination)
      path=/com/adammck/dbus_example/Person
      interface=com.adammck.dbus_example.Person
      member=saved
        int32 1


(The single parameter, `1`, is the primary key of the saved object.
There's no particular reason not to include every field of the model;
I just haven't done that yet.)
