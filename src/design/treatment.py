# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treatment.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_2(object):
    def setupUi(self, Form_2):
        Form_2.setObjectName("Form_2")
        Form_2.resize(520, 690)
        self.gridLayoutWidget = QtWidgets.QWidget(Form_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(4, 0, 511, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.deltrt_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.deltrt_btn.setObjectName("deltrt_btn")
        self.gridLayout.addWidget(self.deltrt_btn, 2, 2, 1, 1)
        self.chngtrt_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.chngtrt_btn.setObjectName("chngtrt_btn")
        self.gridLayout.addWidget(self.chngtrt_btn, 2, 4, 1, 1)
        self.chstrt_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.chstrt_btn.setObjectName("chstrt_btn")
        self.gridLayout.addWidget(self.chstrt_btn, 0, 1, 1, 1)
        self.showtrt_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.showtrt_btn.setObjectName("showtrt_btn")
        self.gridLayout.addWidget(self.showtrt_btn, 2, 3, 1, 1)
        self.addtrt_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.addtrt_btn.setObjectName("addtrt_btn")
        self.gridLayout.addWidget(self.addtrt_btn, 2, 1, 1, 1)
        self.srchtrt_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.srchtrt_btn.setObjectName("srchtrt_btn")
        self.gridLayout.addWidget(self.srchtrt_btn, 0, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 3)
        self.trt_table = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.trt_table.setObjectName("trt_table")
        self.trt_table.setColumnCount(2)
        self.trt_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.trt_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.trt_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.trt_table.setHorizontalHeaderItem(1, item)
        self.trt_table.horizontalHeader().setDefaultSectionSize(245)
        self.gridLayout.addWidget(self.trt_table, 4, 1, 1, 5)
        self.label_msg = QtWidgets.QLabel(Form_2)
        self.label_msg.setGeometry(QtCore.QRect(0, 650, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_msg.setFont(font)
        self.label_msg.setText("")
        self.label_msg.setObjectName("label_msg")

        self.retranslateUi(Form_2)
        QtCore.QMetaObject.connectSlotsByName(Form_2)

    def retranslateUi(self, Form_2):
        _translate = QtCore.QCoreApplication.translate
        Form_2.setWindowTitle(_translate("Form_2", "Form"))
        self.deltrt_btn.setText(_translate("Form_2", "Удалить данные"))
        self.chngtrt_btn.setText(_translate("Form_2", "Изменть данные"))
        self.chstrt_btn.setText(_translate("Form_2", "ID"))
        self.showtrt_btn.setText(_translate("Form_2", "Показать всё"))
        self.addtrt_btn.setText(_translate("Form_2", "Добавить лекарство"))
        self.srchtrt_btn.setText(_translate("Form_2", "Искать"))
        self.lineEdit.setText(_translate("Form_2", "1"))
        item = self.trt_table.verticalHeaderItem(0)
        item.setText(_translate("Form_2", "1"))
        item = self.trt_table.horizontalHeaderItem(0)
        item.setText(_translate("Form_2", "ID карты"))
        item = self.trt_table.horizontalHeaderItem(1)
        item.setText(_translate("Form_2", "Лекарство"))
