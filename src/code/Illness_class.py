from PyQt5.QtWidgets import QApplication, QTableWidget, QDialog, QWidget, QMenu, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui

import sqlite3
import sys
import lang
from src.design.illness import Ui_Form_1
from src.design.add_ill import Ui_Dialog_3
from src.design.changeill_card import Ui_Dialog


class ChangeIll(QDialog, Ui_Dialog):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.main = parent
        self.setupUi(self)
        self.setWindowTitle(lang.cards_input)
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        self.saveIll_btn.clicked.connect(self.save)
        self.diag_new.setText(self.main.infoill[0])
        self.diag_id.setText(self.main.id_numb[0])

    def save(self):
        self.main.dialogIll_new = ''.join(self.diag_new.text().strip())
        self.main.dialogID_new = ''.join(self.diag_id.text().strip())
        if self.main.dialogIll_new == '':
            self.label.setText(lang.diag_input)
            return
        if self.main.dialogID_new == '':
            self.label.setText(lang.id_input)
            return
        variables = [self.main.dialogID_new, self.main.dialogIll_new, self.main.illres[0][0]]
        self.res.execute("UPDATE Illness SET name_id = ?, illness = ? WHERE id = ?", variables)
        self.label.setText('')
        self.connection.commit()
        self.connection.close()
        self.close()


class AddIll(QDialog, Ui_Dialog_3):  # Добавление диагноза в БД пациента
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.main = parent
        self.setWindowTitle('Добавьте диагноз')
        self.setupUi(self)
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        self.okIll_btn.clicked.connect(self.save_ill)
        self.flag = True

    def save_ill(self):
        self.flag = True
        self.main.idIll = ''.join(self.id.text().strip())
        self.main.dialogIll = ''.join(self.diag.text().strip())
        if self.main.idIll == '':
            self.label.setText(lang.id_input)
            return
        if self.main.dialogIll == '':
            self.label.setText(lang.diag_input)
            return
        result = self.res.execute("SELECT id FROM Patients").fetchall()
        try:
            for elem in result:
                if int(self.main.idIll) == int(elem[0]):
                    self.flag = False
                    break
        except ValueError:
            self.label.setText(lang.correctid_input)
        if self.flag:
            self.label.setText(lang.noid_input)
            return
        variables = [self.main.idIll, self.main.dialogIll]
        self.res.execute("INSERT INTO Illness(name_id, illness) VALUES(?, ?)", variables)
        self.label.setText('')
        self.connection.commit()
        self.connection.close()
        self.close()


class IllnessCard(QWidget, Ui_Form_1):  # БД с болезнями пациентов
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('История болезни')
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        menu = QMenu()
        menu.addAction('ID', self.action1)
        menu.addAction('Болезнь', self.action2)
        self.chsill_btn.setMenu(menu)
        self.chngill_btn.clicked.connect(self.ill_change)
        self.addill_btn.clicked.connect(self.ill_add)
        self.srchill_btn.clicked.connect(self.ill_search)
        self.showill_btn.clicked.connect(self.ill_show)
        self.delill_btn.clicked.connect(self.ill_delete)
        self.lest = []
        self.infill = []
        self.row_numb = []
        self.id_numb = []
        self.db = 'name_id'
        self.ill_add = 0
        self.change_card = 0
        self.ill_show()

    def action1(self):
        self.chsill_btn.setText('ID')
        self.db = 'name_id'

    def action2(self):
        self.chsill_btn.setText('Болезнь')
        self.db = 'illness'

    def ill_add(self):
        self.ill_add = AddIll(self)
        self.ill_add.show()

    def ill_change(self):
        self.row_numb = list(set([i.row() for i in self.ill_table.selectedItems()]))
        self.id_numb = [self.ill_table.item(i, 0).text() for i in self.row_numb]
        self.infill = [self.ill_table.item(i, 1).text() for i in self.row_numb]
        try:
            self.lest = self.id_numb[0], self.infill[0]
        except IndexError:
            self.label_msg.setText(lang.takecard)
            return
        self.illness = self.res.execute("SELECT id FROM Illness WHERE name_id = ? AND illness = ?",
                                        self.bruh).fetchall()
        if len(self.id_numb) == 0:
            self.label_msg.setText(lang.takecard)
            return
        self.change_card = ChangeIll(self)
        self.label_msg.setText('')
        self.change_card.show()

    def ill_delete(self):
        rows = list(set([i.row() for i in self.ill_table.selectedItems()]))
        ids = [self.ill_table.item(i, 0).text() for i in rows]
        ibs = [self.ill_table.item(i, 1).text() for i in rows]
        if len(ids) > 1:
            self.label_msg.setText(lang.maxdel_card)
            return
        result = ids + ibs
        if len(result) == 0:
            self.label_msg.setText(lang.del_card)
            return
        use = self.res.execute("SELECT id FROM Illness WHERE name_id = ? AND illness = ?", result).fetchall()
        if len(ids) > 0:
            sure = QMessageBox.question(
                self, '', "Действительно удалить карту?", QMessageBox.Yes, QMessageBox.No)
            if sure == QMessageBox.Yes:
                self.res.execute("DELETE FROM Illness WHERE id = ?", use[0])
                self.label_msg.setText('')
        self.connection.commit()
        self.ill_show()

    def ill_search(self):  # Поиск карт по параметрам
        if self.db == 'name_id':
            try:
                result = self.res.execute(
                    f"SELECT name_id, illness FROM Illness WHERE {self.db} = {self.lineEdit.text()}").fetchall()
            except sqlite3.OperationalError:
                return
        else:
            try:
                result = self.res.execute(
                    f"SELECT name_id, illness FROM Illness "
                    f"WHERE {self.db} LIKE '{self.lineEdit.text().capitalize()}%'").fetchall()
            except sqlite3.OperationalError:
                return
        if not result:
            self.label_msg.setText(lang.nocardinfo)
            return
        else:
            self.ill_table.setRowCount(len(result))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.ill_table.setItem(i, j, QTableWidgetItem(str(val)))

    def ill_show(self):
        result = self.res.execute("SELECT name_id, illness FROM Illness").fetchall()
        self.ill_table.setRowCount(len(result))
        self.ill_table.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.ill_table.setItem(i, j, QTableWidgetItem(str(val)))
