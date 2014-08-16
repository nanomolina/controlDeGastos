# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Designs/newWindow.ui'
#
# Created: Sat Aug 16 05:29:01 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

COLOR = "#F57B00"

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

class Ui_Dialog_New(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(405, 137)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 144, 17);\n"
"font: 63 20pt \"Ubuntu\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setStyleSheet("color : %s" % COLOR)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.dateEdit_2 = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayout_2.addWidget(self.dateEdit_2)
        self.dateEdit = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setDate(QtCore.QDate(2014, 1, 1))
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Añadir una nueva base de Datos", None))
        self.dateEdit_2.setDisplayFormat(_translate("Dialog", "MMMM", None))
        self.dateEdit.setDisplayFormat(_translate("Dialog", "yyyy", None))

