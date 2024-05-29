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

        # Использование сигналов которые передают данные

        label = QLabel()  # создаём Label
        line_edit = QLineEdit() # создаём виджет строки ввода
        line_edit.textChanged.connect(label.setText) # setText - задаёт текст для label

        layout_2 = QVBoxLayout()
        layout_2.addWidget(label)
        layout_2.addWidget(line_edit)
        self.setLayout(layout_2)

        self.show()

    def button_clicked(self):
        print('Нажал :)')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    sys.exit(app.exec())

'''
Вкратце о важном:

- Сигнал - это особое свойство объекта, которое передается при возникновении события.
- Слот - это вызываемый объект, который может принимать сигнал и реагировать на него соответствующим образом.
- PyQt использует сигналы и слоты для связи событий с вызываемыми объектами.

'''
