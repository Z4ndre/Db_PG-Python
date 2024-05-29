from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])

window = QWidget(windowTitle='Hello World') # создаём окно с названием hello world
window.show()  # ВАЖНО: т.к. по умолчанию окно скрыто

app.exec()
