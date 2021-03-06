#!/usr/bin/env python

# Copyright (C) 2007-2008 Christian Dywan <christian at twotoasts dot de>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# See the file COPYING for the full license text.

import sys

if len(sys.argv) < 2:
    print 'No arguments supplied.'
    sys.exit(1)

if sys.argv[1] == 'check':
    print 'Checking module dependencies...'
    try:
        import os, stat, time, gobject, md5
        import optparse, subprocess, fnmatch, pygtk
        pygtk.require('2.0')
        import gtk, gtk.glade
        import xdg.Mime # optional
        import dbus # optional
    except ImportError, msg:
        module = str(msg).split()[-1]
        if not module in ('xdg.Mime', 'dbus'):
            print '...Error: The required module %s is missing.' % module
            sys.exit(1)
        else:
            print 'Warning: The optional module %s is missing.' % module
    except AssertionError, msg:
        print '...Error: You need pyGtk 2.0.'
        sys.exit(1)
    print '...OK'
elif sys.argv[1] == 'build':
    import py_compile
    py_compile.compile(sys.argv[2] + '.py')
