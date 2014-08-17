#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new2.ui'
#
# Created: Tue Aug  5 03:31:56 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from openWindow import Ui_Dialog_Open
from newWindow import Ui_Dialog_New
from Database.database import Database
import unicodedata, sys

SALARY = 1200
MAXIMUM = 9999.99
COL_PRODUCT = 0
COL_PRICE = 1
COL_DATE = 2
COL_BUYER = 3
ORANGE = "#FF4000"
COLOR = "#F57B00"

try:
    import Icons.application_rc3
except ImportError:
    import Icons.application_rc2

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
        style = "QMainWindow {background-color:" \
                " QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161," \
                " stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);}"
        MainWindow.setStyleSheet(style)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.initToolBar(MainWindow)
        self.db = Database()
        self.initCalendar()
        self.initTableWidget()
        self.initInputs()
        self.initButtons()
        self.initLabels()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.calendarWidget, QtCore.SIGNAL(_fromUtf8("clicked(QDate)")), self.dateTimeEdit.setDate)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.buttonAccepted)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.tableWidget.scrollToBottom)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), self.buttonRejected)
        QtCore.QObject.connect(self.actionNew, QtCore.SIGNAL(_fromUtf8("triggered()")), self.action_new)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), self.action_open)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("triggered()")), self.save_changes)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def action_open(self):
        dialog = QtGui.QDialog()
        dialog.ui = Ui_Dialog_Open()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

        if dialog.ui.accepted():
            db_name = dialog.ui.getNameToOpen()
            self.db = Database(db_name)
            self.uploadTable()
            self.salary = self.db.get_salary()
            self.addCosts()
            self.uploadLabels()

    def action_new(self):
        dialog = QtGui.QDialog()
        dialog.ui = Ui_Dialog_New()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

        if dialog.ui.accepted():
            db_name, value_init = dialog.ui.getDbNameAndValue()
            self.db = Database(db_name)
            self.db.set_salary(value_init)
            self.uploadTable()
            self.salary = self.db.get_salary()
            self.addCosts()
            self.uploadLabels()

    def initToolBar(self, MainWindow):
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        self.toolBar.setStyleSheet("background-color:#2E2E2E;")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionNew = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)

    def initCalendar(self):
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(5, 0, 448, 180))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.calendarWidget.setGridVisible(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calendarWidget.setFont(font)
        style = "background-color: #575756; padding: 1px;" \
                " border-style: solid; border: 1px solid #656565;" \
                " border-radius: 5; color: #363534;" \
                " alternate-background-color: #BDB9B5"
        self.calendarWidget.setStyleSheet(style)
        self.today = self.calendarWidget.selectedDate()

    def initTableWidget(self):
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 190, 451, 370))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        style = "QTableWidget {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);" \
                " top: 5px; border: 1px solid #656565;" \
                " gridline-color: #BAB0A7} " \
                "QHeaderView::section {background-color:" \
                " QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161," \
                " stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);" \
                " color: %s; padding-left: 4px;" \
                " border: 1px solid #6c6c6c;}" \
                "QTableCornerButton::section {" \
                " background: #505050; border: 2px outset #505050;} " \
                "QScrollBar:horizontal {background:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);} " \
                "QScrollBar::vertical {background:" \
                " QLinearGradient( x1: 1, y1: 0, x2: 1, y2: 0," \
                " stop: 0.0 #121212, stop: 0.2 #282828," \
                " stop: 1 #484848);}" % COLOR
        self.tableWidget.setStyleSheet(style)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.rows_added = 0
        self.tableWidget.setColumnCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(COL_PRODUCT, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(COL_PRICE, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(COL_DATE, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(COL_BUYER, item)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 560, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line.setStyleSheet("border: 1px solid #656565")

    def initInputs(self):
        self.lineEdit_1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 610, 113, 27))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        style = "QLineEdit {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);" \
                " padding: 1px; border-style: solid;" \
                " border: 1px solid #656565; border-radius: 5;}"
        self.lineEdit_1.setStyleSheet(style)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 610, 62, 27))
        self.doubleSpinBox.setMaximum(MAXIMUM)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        style = "QDoubleSpinBox {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);" \
                " padding: 1px; border-style: solid;" \
                " border: 1px solid #656565; border-radius: 5;} " \
                "QDoubleSpinBox::up-button {border: 1px solid #656565;} " \
                "QDoubleSpinBox::down-button {border: 1px solid #656565;}"
        self.doubleSpinBox.setStyleSheet(style)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(200, 610, 131, 27))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        style = "QDateTimeEdit {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);" \
                " padding: 1px; border-style: solid;" \
                " border: 1px solid #656565; border-radius: 5;} " \
                "QDateTimeEdit::up-button {border: 1px solid #656565;} " \
                "QDateTimeEdit::down-button {border: 1px solid #656565;}"
        self.dateTimeEdit.setStyleSheet(style)
        self.time_zero = self.dateTimeEdit.time()
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 610, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        style = "QLineEdit {background-color:" \
                " QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);" \
                " padding: 1px; border-style: solid;" \
                " border: 1px solid #656565; border-radius: 5;}"
        self.lineEdit_2.setStyleSheet(style)

    def initButtons(self):
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(280, 645, 176, 27))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        style = "background-color: QLinearGradient(" \
                " x1: 0, y1: 0, x2: 0, y2: 1," \
                " stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #BDB9B5);"
        self.buttonBox.setStyleSheet(style)

    def initLabels(self):
        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 580, 350, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName(_fromUtf8("label2"))
        self.label1.setStyleSheet("color : %s" % COLOR)
        self.label2 = QtGui.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(160, 580, 350, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.label2.setStyleSheet("color : %s" % COLOR)
        self.label3 = QtGui.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(310, 580, 350, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.label3.setStyleSheet("color : %s" % COLOR)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Control de Gastos", None))
        self.setActions()
        self.setColumnName()
        self.uploadTable()
        self.salary = self.db.get_salary()
        self.addCosts()
        self.label1.setText(_translate("MainWindow", "Inicial: %6.2f" % self.salary, None))
        self.label2.setText(_translate("MainWindow", "Gastos: %6.2f" % self.expense, None))
        self.label3.setText(_translate("MainWindow", "Resto: %6.2f" % self.rest, None))

    def setActions(self):
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionOpen.setText(_translate("MainWindow", "&Open", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionNew.setText(_translate("MainWindow", "&New", None))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionSave.setText(_translate("MainWindow", "&Save", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))

    def setColumnName(self):
        item = self.tableWidget.horizontalHeaderItem(COL_PRODUCT)
        item.setText(_translate("MainWindow", "Producto", None))
        item = self.tableWidget.horizontalHeaderItem(COL_PRICE)
        item.setText(_translate("MainWindow", "Precio", None))
        item = self.tableWidget.horizontalHeaderItem(COL_DATE)
        item.setText(_translate("MainWindow", "Fecha", None))
        item = self.tableWidget.horizontalHeaderItem(COL_BUYER)
        item.setText(_translate("MainWindow", "Comprador", None))

    def uploadTable(self):
        self.rowCount = self.db.get_row_count()
        db_products = self.db.get_products()
        db_prices = self.db.get_prices()
        db_dates = self.db.get_date()
        db_buyers = self.db.get_buyer()
        self.tableWidget.setRowCount(self.rowCount)
        for row in range(self.rowCount):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(row, COL_PRODUCT, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(row, COL_PRICE, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(row, COL_DATE, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(row, COL_BUYER, item)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        for row in range(self.rowCount):
            item = self.tableWidget.item(row, COL_PRODUCT)
            item.setText(_translate("MainWindow", db_products[row], None))
            item = self.tableWidget.item(row, COL_PRICE)
            item.setText(_translate("MainWindow", db_prices[row], None))
            item = self.tableWidget.item(row, COL_DATE)
            item.setText(_translate("MainWindow", db_dates[row], None))
            item = self.tableWidget.item(row, COL_BUYER)
            item.setText(_translate("MainWindow", db_buyers[row], None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def buttonAccepted(self):
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

    def buttonRejected(self):
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
        self.rest = self.salary - self.expense

    def uploadLabels(self):
        self.label1.setText(_translate("MainWindow", "Inicial: %6.2f" % self.salary, None))
        self.label2.setText(_translate("MainWindow", "Gastos: %6.2f" % self.expense, None))
        self.label3.setText(_translate("MainWindow", "Resto: %6.2f" % self.rest, None))

def delete_accent(string):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(string)) if unicodedata.category(c) != 'Mn'))
    return s.decode()
