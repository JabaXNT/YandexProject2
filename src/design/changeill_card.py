# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeill_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(360, 130)
        self.diag_lbl = QtWidgets.QLabel(Dialog)
        self.diag_lbl.setGeometry(QtCore.QRect(10, 5, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diag_lbl.setFont(font)
        self.diag_lbl.setObjectName("diag_lbl")
        self.diag_id = QtWidgets.QLineEdit(Dialog)
        self.diag_id.setGeometry(QtCore.QRect(90, 5, 261, 20))
        self.diag_id.setObjectName("diag_id")
        self.saveIll_btn = QtWidgets.QPushButton(Dialog)
        self.saveIll_btn.setGeometry(QtCore.QRect(140, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveIll_btn.setFont(font)
        self.saveIll_btn.setObjectName("saveIll_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 110, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.diag_new = QtWidgets.QLineEdit(Dialog)
        self.diag_new.setGeometry(QtCore.QRect(90, 40, 261, 20))
        self.diag_new.setObjectName("diag_new")
        self.diag_lbl_2 = QtWidgets.QLabel(Dialog)
        self.diag_lbl_2.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diag_lbl_2.setFont(font)
        self.diag_lbl_2.setObjectName("diag_lbl_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.diag_lbl.setText(_translate("Dialog", "Id пациента:"))
        self.saveIll_btn.setText(_translate("Dialog", "Сохранить"))
        self.diag_lbl_2.setText(_translate("Dialog", "Диагноз:"))