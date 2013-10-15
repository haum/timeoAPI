MongoDB Schema
==============

Yep. I know. MongoDB works on a schema-less paradigm. But, you know, i think that cool be cool for developpers to have
some sort of reference about where to find content in MongoDB collections....

If you don't like it, don't use this ref. But I will.

Station
=======

::

    {
        code: timeo code (str),
        name: name of station (str),
        coords: [lat, lon] ([str])
    }

Line
====

::

    {
        code: line number (str)
        A: {
            terminus: timeo code (str)
            stations: [code, code, ...] ([str])
           }
        R: {
            terminus: timeo code (str)
            stations: [code, code, ...] ([str])
           }
    }

Inserts has to be done on full service hours to be accurate. 
