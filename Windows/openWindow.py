# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created: Fri Aug 15 21:30:13 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from os import getcwd, listdir
from os.path import join, isfile

DB_PATH = "Database/.Database"
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

class Ui_Dialog_Open(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(243, 397)
        self.initLayout(Dialog)
        self.listdb = []
        self.initLabel()
        self.initListWidget()
        self.initButtonBox()


        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def initLayout(self, Dialog):
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 371))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))  

    def initLabel(self):
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setStyleSheet("color : %s" % COLOR)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.verticalLayout.addWidget(self.label)

    def initListWidget(self):
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        current_path = getcwd()
        db_path = join(current_path, DB_PATH)
        listOfdir = listdir(db_path)
        for file_ in listOfdir:
            dirOfFile = join(db_path, file_)
            if isfile(dirOfFile) and ".db" in file_:
                file_ , trash = file_.split(".db")
                item = QtGui.QListWidgetItem()
                self.listWidget.addItem(item)
                self.listdb.append(file_)

    def initButtonBox(self):
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Abrir", None))
        self.label.setText(_translate("Dialog", "Bases de Datos", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        counter = 0
        for file_ in self.listdb:
            item = self.listWidget.item(counter)
            item.setText(_translate("Form", file_, None))
            counter += 1
        self.listWidget.setSortingEnabled(__sortingEnabled)

