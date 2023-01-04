#pyuic5 C:\Users\User\Desktop\natalie\dialog1.ui -o C:\Users\User\Desktop\natalie\dialog1.py

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import dialog2 # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QDialog, dialog2.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле интерфейс.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        #Добавляем функциональность в наше Python GUI приложение


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
