# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AlphaPlugins
                                 A QGIS plugin
 A plugins to remember
                             -------------------
        begin                : 2013-06-13
        copyright            : (C) 2013 by Alpha Company
        email                : plugins@alpha.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Alpha"


def description():
    return "A plugins to remember"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Alpha Company"

def email():
    return "plugins@alpha.com"

def classFactory(iface):
    # load AlphaPlugins class from file AlphaPlugins
    from alphaplugins import AlphaPlugins
    return AlphaPlugins(iface)
