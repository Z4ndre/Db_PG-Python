import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QT Сигналы и слоты')

        button = QPushButton('Нажми меня')
        # В общем случае синтаксис для подключения сигнала к слоту:
        # sender_object.signal_name.connect(receiver_object.slot_name)
        button.clicked.connect(self.button_clicked)

        # также можно передавать сигнал к слоту через аргумент, пример:
        # button = QPushButton('Click me', clicked=self.button_clicked)

        layout = QVBoxLayout()  # помещаем кнопку в окно используя вертикальную рамку
        self.setLayout(layout)

        layout.addWidget(button)
        self.show()

        def button_clicked(self):
            print('Нажал :)')

if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MainWindow()

        sys.exit(app.exec())