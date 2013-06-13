# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_alphaplugins.ui'
#
# Created: Thu Jun 13 10:24:16 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_AlphaPlugins(object):
    def setupUi(self, AlphaPlugins):
        AlphaPlugins.setObjectName(_fromUtf8("AlphaPlugins"))
        AlphaPlugins.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(AlphaPlugins)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.helloLineEdit = QtGui.QLineEdit(AlphaPlugins)
        self.helloLineEdit.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.helloLineEdit.setObjectName(_fromUtf8("helloLineEdit"))
        self.helloPushButton = QtGui.QPushButton(AlphaPlugins)
        self.helloPushButton.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.helloPushButton.setObjectName(_fromUtf8("helloPushButton"))
        self.layerLineEdit = QtGui.QLineEdit(AlphaPlugins)
        self.layerLineEdit.setGeometry(QtCore.QRect(10, 120, 331, 20))
        self.layerLineEdit.setObjectName(_fromUtf8("layerLineEdit"))
        self.layerLabel = QtGui.QLabel(AlphaPlugins)
        self.layerLabel.setGeometry(QtCore.QRect(10, 100, 46, 13))
        self.layerLabel.setObjectName(_fromUtf8("layerLabel"))
        self.loadLayerPushButton = QtGui.QPushButton(AlphaPlugins)
        self.loadLayerPushButton.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.loadLayerPushButton.setObjectName(_fromUtf8("loadLayerPushButton"))
        self.openFilePushButton = QtGui.QPushButton(AlphaPlugins)
        self.openFilePushButton.setGeometry(QtCore.QRect(350, 120, 31, 23))
        self.openFilePushButton.setObjectName(_fromUtf8("openFilePushButton"))

        self.retranslateUi(AlphaPlugins)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AlphaPlugins.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AlphaPlugins.reject)
        QtCore.QMetaObject.connectSlotsByName(AlphaPlugins)

    def retranslateUi(self, AlphaPlugins):
        AlphaPlugins.setWindowTitle(_translate("AlphaPlugins", "AlphaPlugins", None))
        self.helloPushButton.setText(_translate("AlphaPlugins", "Click Me", None))
        self.layerLabel.setText(_translate("AlphaPlugins", "Layer", None))
        self.loadLayerPushButton.setText(_translate("AlphaPlugins", "Load Layer", None))
        self.openFilePushButton.setText(_translate("AlphaPlugins", "...", None))

