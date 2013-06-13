# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AlphaPluginsDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_alphaplugins import Ui_AlphaPlugins
# create the dialog for zoom to point


class AlphaPluginsDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_AlphaPlugins()
        self.ui.setupUi(self)
        
        helloButton = self.ui.helloPushButton
        QtCore.QObject.connect(helloButton, QtCore.SIGNAL('clicked()'),
                               self.showHelloWorld)
                               
    def showHelloWorld(self):
        self.ui.helloLineEdit.setText('Hello World')
