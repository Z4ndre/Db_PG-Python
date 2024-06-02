from connect_to_db import DataBase
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

db = DataBase()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DB")
        self.setGeometry(100, 100, 600, 400)
        self.create_buttons()

    def create_buttons(self):
        layout = QVBoxLayout()

        button = QPushButton("Перезаписать процедуры", self)
        button_2 = QPushButton("Перезаписать функции", self)

        layout.addWidget(button)
        layout.addWidget(button_2)

        self.setLayout(layout)

        button.clicked.connect(self.procedure_button_clicked)
        button_2.clicked.connect(self.function_button_2_clicked)

    def procedure_button_clicked(self):
        db.get_procedures()

    def function_button_2_clicked(self):
        db.get_functions()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
