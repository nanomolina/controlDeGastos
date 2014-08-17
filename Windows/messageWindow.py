# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Designs/messageWindow.ui'
#
# Created: Sun Aug 17 04:59:30 2014
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

class Ui_Dialog_Message(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(280, 90)
        style = "QDialog {background-color:" \
                " QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161," \
                " stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);}"
        Dialog.setStyleSheet(style)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(15, 10, 250, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 7, 7);"))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Aviso", None))
        self.label.setText(_translate("Dialog", "Ya existe una Base de Datos \n"
"    con el mismo nombre   !!!", None))

