# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_1(object):
    def setupUi(self, Dialog_1):
        Dialog_1.setObjectName("Dialog_1")
        Dialog_1.resize(427, 235)
        self.name = QtWidgets.QLineEdit(Dialog_1)
        self.name.setGeometry(QtCore.QRect(90, 110, 211, 20))
        self.name.setObjectName("name")
        self.id = QtWidgets.QLineEdit(Dialog_1)
        self.id.setGeometry(QtCore.QRect(90, 50, 211, 20))
        self.id.setObjectName("id")
        self.id_lbl = QtWidgets.QLabel(Dialog_1)
        self.id_lbl.setGeometry(QtCore.QRect(10, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.id_lbl.setFont(font)
        self.id_lbl.setObjectName("id_lbl")
        self.sur_lbl = QtWidgets.QLabel(Dialog_1)
        self.sur_lbl.setGeometry(QtCore.QRect(10, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sur_lbl.setFont(font)
        self.sur_lbl.setLineWidth(1)
        self.sur_lbl.setObjectName("sur_lbl")
        self.ok_btn = QtWidgets.QPushButton(Dialog_1)
        self.ok_btn.setGeometry(QtCore.QRect(220, 200, 81, 31))
        self.ok_btn.setObjectName("ok_btn")
        self.sur = QtWidgets.QLineEdit(Dialog_1)
        self.sur.setGeometry(QtCore.QRect(90, 80, 211, 20))
        self.sur.setObjectName("sur")
        self.pat = QtWidgets.QLineEdit(Dialog_1)
        self.pat.setGeometry(QtCore.QRect(210, 140, 211, 20))
        self.pat.setObjectName("pat")
        self.Enter_lbl = QtWidgets.QLabel(Dialog_1)
        self.Enter_lbl.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Enter_lbl.setFont(font)
        self.Enter_lbl.setObjectName("Enter_lbl")
        self.name_lbl = QtWidgets.QLabel(Dialog_1)
        self.name_lbl.setGeometry(QtCore.QRect(10, 110, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_lbl.setFont(font)
        self.name_lbl.setObjectName("name_lbl")
        self.fath_lbl = QtWidgets.QLabel(Dialog_1)
        self.fath_lbl.setGeometry(QtCore.QRect(10, 140, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fath_lbl.setFont(font)
        self.fath_lbl.setObjectName("fath_lbl")
        self.fath_lbl_2 = QtWidgets.QLabel(Dialog_1)
        self.fath_lbl_2.setGeometry(QtCore.QRect(10, 170, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fath_lbl_2.setFont(font)
        self.fath_lbl_2.setObjectName("fath_lbl_2")
        self.bday = QtWidgets.QLineEdit(Dialog_1)
        self.bday.setGeometry(QtCore.QRect(130, 170, 211, 20))
        self.bday.setObjectName("bday")
        self.msg = QtWidgets.QLabel(Dialog_1)
        self.msg.setGeometry(QtCore.QRect(0, 210, 201, 16))
        self.msg.setText("")
        self.msg.setObjectName("msg")

        self.retranslateUi(Dialog_1)
        QtCore.QMetaObject.connectSlotsByName(Dialog_1)

    def retranslateUi(self, Dialog_1):
        _translate = QtCore.QCoreApplication.translate
        Dialog_1.setWindowTitle(_translate("Dialog_1", "Form"))
        self.id_lbl.setText(_translate("Dialog_1", "ID карты:"))
        self.sur_lbl.setText(_translate("Dialog_1", "Фамилию:"))
        self.ok_btn.setText(_translate("Dialog_1", "ОК"))
        self.Enter_lbl.setText(_translate("Dialog_1", "Введите:"))
        self.name_lbl.setText(_translate("Dialog_1", "Имя:"))
        self.fath_lbl.setText(_translate("Dialog_1", "Отчество (При наличии):"))
        self.fath_lbl_2.setText(_translate("Dialog_1", "Год Рождения:"))
