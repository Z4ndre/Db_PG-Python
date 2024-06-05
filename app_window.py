import psycopg2
from messageBoxes import show_notification
from connect_to_db import DataBase
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QTableWidget, QTableWidgetItem

db = DataBase()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DB")
        self.setGeometry(100, 100, 1920, 1080)
        # Запретить растягивать окно
        self.create_connect()
        self.create_buttons()
        self.create_combo_box()
        self.create_table_widget()
        self.selected_table = self.get_default_table()
        self.populate_table()

    def create_connect(self):
        self.conn = db.connect_to_Db()

    def create_buttons(self):

        button_1 = QPushButton("Перезаписать процедуры", self)
        button_2 = QPushButton("Перезаписать функции", self)
        button_3 = QPushButton("Перезаписать список таблиц", self)

        button_1.setGeometry(10, 60, 200, 30) # x, y, width, height
        button_2.setGeometry(10, 100, 200, 30)
        button_3.setGeometry(10, 140, 200, 30)

        button_1.clicked.connect(self.procedure_button_clicked)
        button_2.clicked.connect(self.function_button_2_clicked)
        button_3.clicked.connect(self.tables_button_3_clicked)

    def procedure_button_clicked(self):
        db.get_procedures()

    def function_button_2_clicked(self):
        db.get_functions()

    def tables_button_3_clicked(self):
        db.get_tables()

    def create_combo_box(self):
        self.combo_box = QComboBox(self)
        self.combo_box.setGeometry(370, 60, 150, 30)
        self.complation_comboBox('table_list.txt')
        self.combo_box.currentTextChanged.connect(self.on_combo_box_text_changed)

    def complation_comboBox(self, file_path='table_list.txt'):
        with open(file_path, 'r') as fi:
            data = fi.readlines()

        for item in data:
            self.combo_box.addItem(item.strip())

    def create_table_widget(self):
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(0)
        self.table_widget.setRowCount(0)
        self.table_widget.setGeometry(370, 100, 1520, 900)

    def on_combo_box_text_changed(self, text):
        self.selected_table = text
        self.populate_table()

    def get_default_table(self):
        return self.combo_box.currentText()

    def populate_table(self):
        if self.conn is None:
            show_notification("Не удалось установить соединение с базой данных.")
            return

        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT * FROM {self.selected_table}")
            rows = cur.fetchall()
            cur.close()

            self.table_widget.setRowCount(0)
            self.table_widget.setColumnCount(len(rows[0]))

            for i, row in enumerate(rows):
                self.table_widget.insertRow(i)
                for j, data in enumerate(row):
                    item = QTableWidgetItem(str(data))
                    self.table_widget.setItem(i, j, item)

        except psycopg2.Error as e:
            show_notification(f"ERROR: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
