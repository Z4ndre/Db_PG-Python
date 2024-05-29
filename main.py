import sys

from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)  # Программа PyQt может принимать один или несколько аргументов командной строки.
# Чтобы включить это, вам нужно передать argv из sys модуля в QApplication

window = QWidget(windowTitle='Hello World')  # создаём окно с названием hello world
window.show()  # ВАЖНО: т.к. по умолчанию окно скрыто

sys.exit(app.exec())  # запуск в цикле - event loop
