import sys

from PyQt6.QtWidgets import QApplication, QWidget


class MainWindow(QWidget):  # создаём класс MainWindow который наследуется от QWidget
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Hello World')
        self.show()


if __name__ == '__main__':  # если программа выполняется напрямую - будет работать, а если импортировано как
    # модуль, код в этом блоке выполняться не будет
    app = QApplication(sys.argv)    # создаём объект
    window = MainWindow()   # создаём экземпляр класса
    sys.exit(app.exec())    # запускаем цикл событий

'''
Вкратце важная информация:
- Каждое приложение PyQt имеет один и только один QApplication объект. 
QApplication Объект содержит цикл событий.

- Цикл обработки событий управляет всеми событиями приложения PyQt. 
Он непрерывно проверяет очередь событий и пересылает события их обработчикам.

- Вызовите app.exec(), чтобы запустить цикл событий.

- Используйте QMainWindow для создания главного окна приложения PyQt и 
вызова show() метода для отображения окна на экране.
'''

