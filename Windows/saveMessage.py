# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveMessage.ui'
#
# Created: Sat Aug 23 18:48:50 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Dialog_SaveMsg(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(250, 100)
        self.save = False
        style = "QDialog {background-color:" \
                " QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161," \
                " stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);}"
        Dialog.setStyleSheet(style)
        self.initLabel(Dialog)
        self.initButtonBox(Dialog)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonAccepted)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def initLabel(self, Dialog):
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 220, 31))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 7, 7);"))
        self.label.setObjectName(_fromUtf8("label"))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        style = "QLabel {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #FF4000, stop: 1 #F57B00);" \
                " top: 5px; border: 1px solid #656565;" \
                " gridline-color: #BAB0A7} "
        self.label.setStyleSheet(_fromUtf8(style))

    def initButtonBox(self, Dialog):
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 60, 176, 27))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        style = "background-color: QLinearGradient(" \
                " x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);"
        self.buttonBox.setStyleSheet(style)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Aviso", None))
        self.label.setText(_translate("Dialog", "Desea guardar los cambios?", None))

    def buttonAccepted(self):
        self.save = True

    def mustSave(self):
        return self.save
