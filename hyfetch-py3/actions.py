#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def build():
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")
    pisitools.dodoc("CONTRIBUTING.md", "LICENSE.md", "README.md")
