import sqlite3
import sys
import Treatment_class
import Illness_class
import lang

from src.design.health import Ui_MainWindow
from src.design.add_card import Ui_Dialog_1
from src.design.change_card import Ui_Dialog_2
from PyQt5.QtWidgets import QApplication, QTableWidget, QDialog, QMainWindow, QMenu, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui


class ChangeCard(QDialog, Ui_Dialog_2):  # Изменение уже существующей карты
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.main = parent
        self.setupUi(self)
        self.setWindowTitle(lang.cards_input)
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        self.save_btn.clicked.connect(self.save)
        self.sur_new.setText(self.main.info[1][0])
        self.name_new.setText(self.main.info[2][0])
        self.pat_new.setText(self.main.info[3][0])
        self.bday_new.setText(self.main.info[4][0])

    def save(self):
        self.main.name_new = ''.join(self.name_new.text().strip())
        self.main.sur_new = ''.join(self.sur_new.text().strip())
        self.main.pat_new = ''.join(self.pat_new.text().strip())
        self.main.bday_new = ''.join(self.bday_new.text().strip())
        if self.main.sur_new == '':
            self.label.setText(lang.sur_input)
            return
        if self.main.name_new == '':
            self.label.setText(lang.name_input)
            return
        if self.main.bday_new == '':
            self.label.setText(lang.bday_input)
            return
        variable2 = [self.main.name_new, self.main.sur_new, self.main.pat_new, self.main.bday_new,
                     self.main.id_numb[0]]
        try:
            self.res.execute(
                "UPDATE Patients SET name = ?, surename = ?, patronymic = ?, birthday = ? WHERE id = ?",
                variable2)
        except sqlite3.IntegrityError:
            return
        self.connection.commit()
        self.connection.close()
        self.close()


class AddCard(QDialog, Ui_Dialog_1):  # Создание новой карты пациента
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.main = parent
        self.setupUi(self)
        self.setWindowTitle(lang.cards_input)
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        self.ok_btn.clicked.connect(self.close_win)

    def close_win(self):
        self.main.id_text = ''.join(self.id.text().strip())
        self.main.name_text = ''.join(self.name.text().strip())
        self.main.sur_text = ''.join(self.sur.text().strip())
        self.main.pat_text = ''.join(self.pat.text().strip())
        self.main.bday_text = ''.join(self.bday.text().strip())
        if self.main.id_text == '':
            self.msg.setText(lang.id_input)
            return
        if self.main.sur_text == '':
            self.msg.setText(lang.sur_input)
            return
        if self.main.name_text == '':
            self.msg.setText(lang.name_input)
            return
        if self.main.bday_text == '':
            self.msg.setText(lang.bday_input)
            return
        variable = (
            self.main.id_text, self.main.sur_text, self.main.name_text, self.main.pat_text, self.main.bday_text)
        try:
            self.res.execute("INSERT INTO Patients VALUES(?, ?, ?, ?, ?)", variable)
        except sqlite3.IntegrityError:
            self.msg.setText(lang.copy_id)
            return
        self.connection.commit()
        self.connection.close()
        self.close()


class HealthCard(QMainWindow, Ui_MainWindow):  # Главное окно почти полностью сделано
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Медицинские карты')
        self.connection = sqlite3.connect('Health_cards.sqlite')
        self.res = self.connection.cursor()
        menu = QMenu()
        menu.addAction('ID', self.action1)
        menu.addAction('Имя', self.action2)
        menu.addAction('Фамилия', self.action3)
        menu.addAction('Отчество', self.action4)
        menu.addAction('Год рождения', self.action5)
        self.chs_btn.setMenu(menu)
        self.srch_btn.clicked.connect(self.card_search)
        self.chng_btn.clicked.connect(self.card_change)
        self.show_btn.clicked.connect(self.card_show)
        self.del_btn.clicked.connect(self.card_delete)
        self.add_btn.clicked.connect(self.card_add)
        self.ill_btn.clicked.connect(self.card_ill)
        self.trt_btn.clicked.connect(self.card_trt)
        self.db = 'id'
        self.mem = 0
        self.card_show()
        self.info = []
        self.Trt = Treatment_class.TreatmentCard()
        self.Ill = Illness_class.IllnessCard()

    def action1(self):
        self.chs_btn.setText('ID')
        self.db = 'id'

    def action2(self):
        self.chs_btn.setText('Имя')
        self.db = 'name'

    def action3(self):
        self.chs_btn.setText('Фамилия')
        self.db = 'surename'

    def action4(self):
        self.chs_btn.setText('Отчество')
        self.db = 'patronymic'

    def action5(self):
        self.chs_btn.setText('Год Рождения')
        self.db = 'birthday'

    def card_ill(self):  # Открытие формы с болезнями
        self.Ill.show()

    def card_trt(self):  # Открытие формы с лечением
        self.Trt.show()

    def card_add(self):  # Открытие диалогового окна создания карты
        self.add_card = AddCard(self)
        self.add_card.show()

    def card_change(self):  # Открытие диалогового окна изменения карты
        self.info = []
        self.row_numb = list(set([i.row() for i in self.cards_table.selectedItems()]))
        self.id_numb = [self.cards_table.item(i, 0).text() for i in self.row_numb]
        for j in range(5):
            self.info.append([self.cards_table.item(i, j).text() for i in self.row_numb])
        if len(self.id_numb) == 0:
            self.statusBar().showMessage(lang.takecard)
            return
        self.change_card = ChangeCard(self)
        self.change_card.show()

    def card_delete(self):  # Удаление выбранных карт
        rows = list(set([i.row() for i in self.cards_table.selectedItems()]))
        ids = [self.cards_table.item(i, 0).text() for i in rows]
        if len(ids) > 1:
            self.statusBar().showMessage(lang.maxdel_card)
            return
        if len(ids) > 0:
            sure = QMessageBox.question(
                self, '', "Действительно удалить карту с ID " + ",".join(ids),
                QMessageBox.Yes, QMessageBox.No)
            if sure == QMessageBox.Yes:
                self.res.execute("DELETE FROM Patients WHERE id IN (" + ", ".join(
                    '?' * len(ids)) + ")", ids)
        else:
            self.statusBar().showMessage(lang.del_card)
            return
        # удаление всех диагнозов и лекарств удаленного пациента
        ill = self.res.execute("SELECT id FROM Illness WHERE name_id = ?", ids).fetchall()
        cure = self.res.execute("SELECT id FROM Treat WHERE name_id = ?", ids).fetchall()
        for elem in ill:
            self.res.execute("DELETE FROM Illness WHERE id = ?", (elem[0],))
        for elem in cure:
            self.res.execute("DELETE FROM Treat WHERE id = ?", (elem[0],))
        self.connection.commit()
        self.card_show()

    def card_search(self):  # Поиск карт по параметрам
        if self.db == 'id' or self.db == 'birthday':
            try:
                result = self.res.execute(
                    f"SELECT * FROM Patients WHERE {self.db} = {self.lineEdit.text()}").fetchall()
            except sqlite3.OperationalError:
                return
        else:
            try:
                result = self.res.execute(
                    f"SELECT * FROM Patients WHERE {self.db} LIKE '{self.lineEdit.text().capitalize()}%'").fetchall()
            except sqlite3.OperationalError:
                return
        if not result:
            self.statusBar().showMessage(lang.nocardinfo)
            return
        else:
            self.cards_table.setRowCount(len(result))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.cards_table.setItem(i, j, QTableWidgetItem(str(val)))

    def card_show(self):  # Показать все карты
        result = self.res.execute("SELECT * FROM Patients").fetchall()
        self.cards_table.setRowCount(len(result))
        self.cards_table.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.cards_table.setItem(i, j, QTableWidgetItem(str(val)))

    def closeEvent(self, event):
        self.connection.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HealthCard()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
