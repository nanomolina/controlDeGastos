# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Designs/newWindow.ui'
#
# Created: Sat Aug 16 16:41:29 2014
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
        Dialog.resize(406, 189)
        style = "QDialog {background-color:" \
                " QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161," \
                " stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);}"
        Dialog.setStyleSheet(style)
        self.initVerticalLayout(Dialog)
        self.initLabels()
        self.initInputs()
        self.initButtonBox()

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def initVerticalLayout(self, Dialog):
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 382, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

    def initLabels(self):
        self.label1 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label1.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        style = "QLabel {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #FF4000, stop: 1 #F57B00);" \
                " top: 5px; border: 1px solid #656565;" \
                " gridline-color: #BAB0A7} "
        self.label1.setStyleSheet(_fromUtf8(style))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #---label2---
        self.label2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.horizontalLayout.addWidget(self.label2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color : %s" % COLOR)
        #---label3---
        self.label3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.horizontalLayout.addWidget(self.label3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color : %s" % COLOR)
        #---label4---
        self.label4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label4.setObjectName(_fromUtf8("label4"))
        self.horizontalLayout.addWidget(self.label4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color : %s" % COLOR)
        self.verticalLayout.addLayout(self.horizontalLayout)

    def initInputs(self):
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        #---dateEDit1---
        self.dateEdit1 = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit1.setObjectName(_fromUtf8("dateEdit1"))
        self.horizontalLayout_2.addWidget(self.dateEdit1)
        style = "QDateEdit {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);" \
                " padding: 1px; border-style: solid;" \
                " border: 1px solid #656565; border-radius: 5;} " \
                "QDateEdit::up-button {border: 1px solid #656565;} " \
                "QDateEdit::down-button {border: 1px solid #656565;}"
        self.dateEdit1.setStyleSheet(style)
        #---dateEDit1---
        self.dateEdit2 = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit2.setDate(QtCore.QDate(2014, 1, 1))
        self.dateEdit2.setCalendarPopup(False)
        self.dateEdit2.setObjectName(_fromUtf8("dateEdit2"))
        self.horizontalLayout_2.addWidget(self.dateEdit2)
        style = "QDateEdit {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);" \
                " padding: 1px; border-style: solid;" \
                " border: 1px solid #656565; border-radius: 5;} " \
                "QDateEdit::up-button {border: 1px solid #656565;} " \
                "QDateEdit::down-button {border: 1px solid #656565;}"
        self.dateEdit2.setStyleSheet(style)
        #---doubleSpinBox---
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox.setMaximum(10000000.0)
        self.doubleSpinBox.setSingleStep(10.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        style = "QDoubleSpinBox {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);" \
                " padding: 1px; border-style: solid;" \
                " border: 1px solid #656565; border-radius: 5;} " \
                "QDoubleSpinBox::up-button {border: 1px solid #656565;} " \
                "QDoubleSpinBox::down-button {border: 1px solid #656565;}"
        self.doubleSpinBox.setStyleSheet(style)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        #SpaceBar
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)

    def initButtonBox(self):
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        style = "background-color: QLinearGradient(" \
                " x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);"
        self.buttonBox.setStyleSheet(style)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Nuevo", None))
        self.label1.setText(_translate("Dialog", "Añadir una nueva base de Datos", None))
        self.label2.setText(_translate("Dialog", "Mes:", None))
        self.label3.setText(_translate("Dialog", "Año:", None))
        self.label4.setText(_translate("Dialog", "Saldo Inicial:", None))
        self.dateEdit1.setDisplayFormat(_translate("Dialog", "MMMM", None))
        self.dateEdit2.setDisplayFormat(_translate("Dialog", "yyyy", None))
