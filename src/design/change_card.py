# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_2(object):
    def setupUi(self, Dialog_2):
        Dialog_2.setObjectName("Dialog_2")
        Dialog_2.resize(413, 221)
        self.sur_new = QtWidgets.QLineEdit(Dialog_2)
        self.sur_new.setGeometry(QtCore.QRect(80, 30, 211, 20))
        self.sur_new.setObjectName("sur_new")
        self.pat_new = QtWidgets.QLineEdit(Dialog_2)
        self.pat_new.setGeometry(QtCore.QRect(200, 90, 211, 20))
        self.pat_new.setObjectName("pat_new")
        self.bday_lbl = QtWidgets.QLabel(Dialog_2)
        self.bday_lbl.setGeometry(QtCore.QRect(0, 120, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bday_lbl.setFont(font)
        self.bday_lbl.setObjectName("bday_lbl")
        self.sur_lbl = QtWidgets.QLabel(Dialog_2)
        self.sur_lbl.setGeometry(QtCore.QRect(0, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sur_lbl.setFont(font)
        self.sur_lbl.setLineWidth(1)
        self.sur_lbl.setObjectName("sur_lbl")
        self.name_new = QtWidgets.QLineEdit(Dialog_2)
        self.name_new.setGeometry(QtCore.QRect(80, 60, 211, 20))
        self.name_new.setObjectName("name_new")
        self.name_lbl = QtWidgets.QLabel(Dialog_2)
        self.name_lbl.setGeometry(QtCore.QRect(0, 60, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_lbl.setFont(font)
        self.name_lbl.setObjectName("name_lbl")
        self.bday_new = QtWidgets.QLineEdit(Dialog_2)
        self.bday_new.setGeometry(QtCore.QRect(120, 120, 211, 20))
        self.bday_new.setObjectName("bday_new")
        self.Enter_lbl = QtWidgets.QLabel(Dialog_2)
        self.Enter_lbl.setGeometry(QtCore.QRect(0, 0, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Enter_lbl.setFont(font)
        self.Enter_lbl.setObjectName("Enter_lbl")
        self.fath_lbl = QtWidgets.QLabel(Dialog_2)
        self.fath_lbl.setGeometry(QtCore.QRect(0, 90, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fath_lbl.setFont(font)
        self.fath_lbl.setObjectName("fath_lbl")
        self.save_btn = QtWidgets.QPushButton(Dialog_2)
        self.save_btn.setGeometry(QtCore.QRect(160, 150, 91, 41))
        self.save_btn.setObjectName("save_btn")
        self.label = QtWidgets.QLabel(Dialog_2)
        self.label.setGeometry(QtCore.QRect(0, 190, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_2)
        QtCore.QMetaObject.connectSlotsByName(Dialog_2)

    def retranslateUi(self, Dialog_2):
        _translate = QtCore.QCoreApplication.translate
        Dialog_2.setWindowTitle(_translate("Dialog_2", "Dialog"))
        self.bday_lbl.setText(_translate("Dialog_2", "Год Рождения:"))
        self.sur_lbl.setText(_translate("Dialog_2", "Фамилию:"))
        self.name_lbl.setText(_translate("Dialog_2", "Имя:"))
        self.Enter_lbl.setText(_translate("Dialog_2", "Введите:"))
        self.fath_lbl.setText(_translate("Dialog_2", "Отчество (При наличии):"))
        self.save_btn.setText(_translate("Dialog_2", "Сохранить"))
