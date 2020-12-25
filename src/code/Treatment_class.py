from PyQt5.QtWidgets import QApplication, QTableWidget, QDialog, QWidget, QMenu, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui

import sqlite3
import sys
import lang
from src.design.treatment import Ui_Form_2
from src.design.add_trt import Ui_Dialog_4
from src.design.changetrt_card import Ui_Dialog


class ChangeTrt(QDialog, Ui_Dialog):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.main = parent
        self.setupUi(self)
        self.setWindowTitle(lang.cards_input)
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        self.saveTrt_btn.clicked.connect(self.save)
        self.cure_new.setText(self.main.treatment[0])
        self.cure_id.setText(self.main.id_numb[0])

    def save(self):
        self.main.cureTrt_new = ''.join(self.cure_new.text().strip())
        self.main.cureID_new = ''.join(self.cure_id.text().strip())
        if self.main.cureTrt_new == '':
            self.label.setText(lang.treat_input)
            return
        if self.main.cureID_new == '':
            self.label.setText(lang.id_input)
            return
        variables = [self.main.cureID_new, self.main.cureTrt_new, self.main.treatments[0][0]]
        self.res.execute("UPDATE Treat SET name_id = ?, medication = ? WHERE id = ?", variables)
        self.label.setText('')
        self.connection.commit()
        self.connection.close()
        self.close()


class AddTrt(QDialog, Ui_Dialog_4):  # Добавление лекарства в БД пациента
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.main = parent
        self.setupUi(self)
        self.setWindowTitle('Добавьте лекарство')
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        self.okTrt_btn.clicked.connect(self.save_trt)
        self.flag = True

    def save_trt(self):
        self.flag = True
        self.main.idTrt = ''.join(self.id.text().strip())
        self.main.cureTrt = ''.join(self.cure.text().strip())
        if self.main.idTrt == '':
            self.label.setText(lang.id_input)
            return
        if self.main.cureTrt == '':
            self.label.setText(lang.treat_input)
            return
        result = self.res.execute("SELECT id FROM Patients").fetchall()
        try:
            for elem in result:
                if int(self.main.idTrt) == int(elem[0]):
                    self.flag = False
                    break
        except ValueError:
            self.label.setText(lang.correctid_input)
        if self.flag:
            self.label.setText(lang.noid_input)
            return
        variable3 = [self.main.idTrt, self.main.cureTrt]
        self.res.execute("INSERT INTO Treat(name_id, medication) VALUES(?, ?)", variable3)
        self.label.setText('')
        self.connection.commit()
        self.connection.close()
        self.close()


class TreatmentCard(QWidget, Ui_Form_2):  # История лечения пациента (хз когда доделаю)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Лечение')
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        menu = QMenu()
        menu.addAction('ID', self.action1)
        menu.addAction('Лекарство', self.action2)
        self.chstrt_btn.setMenu(menu)
        self.deltrt_btn.clicked.connect(self.trt_delete)
        self.chngtrt_btn.clicked.connect(self.trt_change)
        self.srchtrt_btn.clicked.connect(self.trt_search)
        self.showtrt_btn.clicked.connect(self.trt_show)
        self.addtrt_btn.clicked.connect(self.trt_add)
        self.lest = []
        self.row_numb = []
        self.informant = []
        self.trt_add = 0
        self.change_card = 0
        self.id_numb = []
        self.db = 'name_id'
        self.trt_show()

    def action1(self):
        self.chstrt_btn.setText('ID')
        self.db = 'name_id'

    def action2(self):
        self.chstrt_btn.setText('Лекарство')
        self.db = 'medication'

    def trt_add(self):
        self.trt_add = AddTrt(self)
        self.trt_add.show()

    def trt_change(self):
        self.row_numb = list(set([i.row() for i in self.trt_table.selectedItems()]))
        self.id_numb = [self.trt_table.item(i, 0).text() for i in self.row_numb]
        self.treatment = [self.trt_table.item(i, 1).text() for i in self.row_numb]
        try:
            self.lest = self.id_numb[0], self.treatment[0]
        except IndexError:
            self.label_msg.setText(lang.takecard)
            return
        self.treatments = self.res.execute("SELECT id FROM Treat WHERE name_id = ? AND medication = ?",
                                           self.lest).fetchall()
        if len(self.id_numb) == 0:
            self.label_msg.setText(lang.takecard)
            return
        self.change_card = ChangeTrt(self)
        self.label_msg.setText('')
        self.change_card.show()

    def trt_delete(self):
        rows = list(set([i.row() for i in self.trt_table.selectedItems()]))
        ids = [self.trt_table.item(i, 0).text() for i in rows]
        ibs = [self.trt_table.item(i, 1).text() for i in rows]
        if len(ids) > 1:
            self.label_msg.setText(lang.maxdel_card)
            return
        result = ids + ibs
        if len(result) == 0:
            self.label_msg.setText(lang.del_card)
            return
        use = self.res.execute("SELECT id FROM Treat WHERE name_id = ? AND medication = ?", result).fetchall()
        if len(ids) > 0:
            sure = QMessageBox.question(
                self, '', "Действительно удалить карту?", QMessageBox.Yes, QMessageBox.No)
            if sure == QMessageBox.Yes:
                self.res.execute("DELETE FROM Treat WHERE id = ?", use[0])
                self.label_msg.setText('')
        self.connection.commit()
        self.trt_show()

    def trt_search(self):  # Поиск карт по параметрам
        if self.db == 'name_id':
            try:
                result = self.res.execute(
                    f"SELECT name_id, medication FROM Treat WHERE {self.db} = {self.lineEdit.text()}").fetchall()
            except sqlite3.OperationalError:
                return
        else:
            result = self.res.execute(
                f"SELECT name_id, medication FROM Treat"
                f" WHERE {self.db} LIKE '{self.lineEdit.text().capitalize()}%'").fetchall()
        if not result:
            self.label_msg.setText(lang.nocardinfo)
            return
        else:
            self.trt_table.setRowCount(len(result))
            self.label_msg.setText('')
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.trt_table.setItem(i, j, QTableWidgetItem(str(val)))

    def trt_show(self):
        result = self.res.execute("SELECT name_id, medication FROM Treat").fetchall()
        self.trt_table.setRowCount(len(result))
        self.trt_table.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.trt_table.setItem(i, j, QTableWidgetItem(str(val)))
