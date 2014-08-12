#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new2.ui'
#
# Created: Tue Aug  5 03:31:56 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from database import *
import unicodedata

SALARY = 1200
MAXIMUM = 9999.99
COL_PRODUCT = 0
COL_PRICE = 1
COL_DATE = 2
COL_BUYER = 3

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(462, 715)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.db = Database()
        self.initCalendar()
        self.initTableWidget()
        self.initInputs()
        self.initButtons()
        self.initLabels()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.calendarWidget, QtCore.SIGNAL(_fromUtf8("clicked(QDate)")), self.dateTimeEdit.setDate)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.button_accepted)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.tableWidget.scrollToBottom)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.button_rejected)
        QtCore.QObject.connect(self.commandLinkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.save_changes)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def initCalendar(self):
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(5, 30, 448, 172))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.calendarWidget.setGridVisible(True)
        self.today = self.calendarWidget.selectedDate()

    def initTableWidget(self):
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 210, 451, 381))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.rows_added = 0
        self.tableWidget.setColumnCount(4)
        self.rowCount = self.db.get_row_count()
        self.db_products = self.db.get_products()
        self.db_prices = self.db.get_prices()
        self.db_dates = self.db.get_date()
        self.db_buyers = self.db.get_buyer()
        self.tableWidget.setRowCount(self.rowCount)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(COL_PRODUCT, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(COL_PRICE, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(COL_DATE, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(COL_BUYER, item)
        for row in range(self.rowCount):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(row, COL_PRODUCT, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(row, COL_PRICE, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(row, COL_DATE, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(row, COL_BUYER, item)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 590, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

    def initInputs(self):
        self.lineEdit_1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 640, 113, 27))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 640, 62, 27))
        self.doubleSpinBox.setMaximum(MAXIMUM)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(200, 640, 131, 27))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.time_zero = self.dateTimeEdit.time()
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 640, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

    def initButtons(self):
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 670, 185, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(280, 680, 176, 27))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

    def initLabels(self):
        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 610, 350, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName(_fromUtf8("label2"))
        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(160, 610, 350, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label3 = QtGui.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(310, 610, 350, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName(_fromUtf8("label3"))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Control de Gastos", None))
        self.commandLinkButton.setText(_translate("MainWindow", "Guardar Cambios", None))
        self.setColumnName()
        self.uploadingInformation()
        self.addCosts()
        self.label1.setText(_translate("MainWindow", "Inicial: %6.2f" % SALARY, None))
        self.label2.setText(_translate("MainWindow", "Gastos: %6.2f" % self.expense, None))
        self.label3.setText(_translate("MainWindow", "Resto: %6.2f" % self.rest, None))

    def setColumnName(self):
        item = self.tableWidget.horizontalHeaderItem(COL_PRODUCT)
        item.setText(_translate("MainWindow", "Producto", None))
        item = self.tableWidget.horizontalHeaderItem(COL_PRICE)
        item.setText(_translate("MainWindow", "Precio", None))
        item = self.tableWidget.horizontalHeaderItem(COL_DATE)
        item.setText(_translate("MainWindow", "Fecha", None))
        item = self.tableWidget.horizontalHeaderItem(COL_BUYER)
        item.setText(_translate("MainWindow", "Comprador", None))

    def uploadingInformation(self):
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        for row in range(self.rowCount):
            item = self.tableWidget.item(row, COL_PRODUCT)
            item.setText(_translate("MainWindow", self.db_products[row], None))
            item = self.tableWidget.item(row, COL_PRICE)
            item.setText(_translate("MainWindow", self.db_prices[row], None))
            item = self.tableWidget.item(row, COL_DATE)
            item.setText(_translate("MainWindow", self.db_dates[row], None))
            item = self.tableWidget.item(row, COL_BUYER)
            item.setText(_translate("MainWindow", self.db_buyers[row], None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def button_accepted(self):
        self.tableWidget.insertRow(self.rowCount)
        for column in range(4):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(self.rowCount, column, item)
        text1 = self.lineEdit_1.text()
        value = self.doubleSpinBox.value()
        dateTime = self.dateTimeEdit.dateTime()
        dateTime = dateTime.toString("ddd d MMM yyyy hh:mm")
        dateTime = delete_accent(dateTime)
        text2 = self.lineEdit_2.text()
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(self.rowCount, COL_PRODUCT)
        item.setText(_translate("MainWindow", text1, None))
        item = self.tableWidget.item(self.rowCount, COL_PRICE)
        item.setText(_translate("MainWindow", str(value), None))
        item = self.tableWidget.item(self.rowCount, COL_DATE)
        item.setText(_translate("MainWindow", dateTime, None))
        item = self.tableWidget.item(self.rowCount, COL_BUYER)
        item.setText(_translate("MainWindow", text2, None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.rows_added += 1
        self.rowCount += 1
        self.expense += value
        self.rest -= value
        self.label2.setText(_translate("MainWindow", "Gastos: %6.2f" % self.expense, None))
        self.label3.setText(_translate("MainWindow", "Resto: %6.2f" % self.rest, None))

    def button_rejected(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
        self.doubleSpinBox.setValue(0)
        self.calendarWidget.setSelectedDate(self.today)
        self.dateTimeEdit.setDate(self.today)
        self.dateTimeEdit.setTime(self.time_zero)
        item = self.tableWidget.item(0, 0)

    def save_changes(self):
        for row in range(self.rowCount-self.rows_added, self.rowCount):
            item = self.tableWidget.item(row, COL_PRODUCT)
            product = item.text()
            item = self.tableWidget.item(row, COL_PRICE)
            price = item.text()
            item = self.tableWidget.item(row, COL_DATE)
            date = item.text()
            item = self.tableWidget.item(row, COL_BUYER)
            name = item.text()
            self.db.insert_data(str(product), float(price), str(date), str(name))
        self.rows_added = 0

    def addCosts(self):
        self.expense = 0
        for row in range(self.rowCount):
            item = self.tableWidget.item(row, COL_PRICE)
            self.expense += float(item.text())
        self.rest = SALARY - self.expense

def delete_accent(string):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(string)) if unicodedata.category(c) != 'Mn'))
    return s.decode()
