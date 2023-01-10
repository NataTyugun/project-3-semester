#pyuic5 C:\Users\User\Desktop\natalie\dialog1.ui -o C:\Users\User\Desktop\natalie\dialog1.py

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import window1# Это наш конвертированный файл дизайна
import dialog1
import dialog2


class App(QtWidgets.QDialog, dialog2.Ui_Dialog2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        #self.nextButton_window1.pressed.connect(self.first)

        #self.nextButton_dialog1.pressed.connect(self.second)
        #self.walkButton.pressed.connect(self.walking)
        #self.sportButton.pressed.connect(self.sportic)
        #self.workButton.pressed.connect(self.working)
        #self.radioButton.toggled.connect(self.radio)
        #self.radioButton_2.toggled.connect(self.radio)

        self.lastButton_dialog2.pressed.connect(self.third)



    def first(self):
        user_city = self.lineEdit_firstwindow.text()
        print(user_city)

        self.nextButton_window1.clicked.connect(self.button_clicked) # та же хрень, что и ниже
 # неработающая хрень с переключением окон
    def button_clicked(self):
        dialog = Ui_Dialog1(self)
        dialog.axec_()

    def second(self):
        user_date = self.lineEdit_dialog1.text()
        print(user_date)

    def walking(self):
        user_activity = 'прогулка'
        print(user_activity)

    def sportic(self):
        user_activity = 'спорт'
        print(user_activity)

    def working(self):
        user_activity = 'ежедневные дела'
        print(user_activity)

    def radio(self):
        radioButton = self.radioButton.sender()
        radioButton_2 = self.radioButton_2.sender()
        if radioButton.isChecked():
            user_gender = radioButton.text()
            print(user_gender)
        elif radioButton_2.isChecked() :
            user_gender = radioButton.text()
            print(user_gender)

    def third(self):

        user_date = '23.09.2022'
        user_city = 'Санкт-Петербург'
        recomendation_clouses = 'носки, трусы и тапочки'


        self.label_3.setText(_translate("Dialog", recomendation_clouses))
        user_info = user_date + '  ' + user_city
        self.label.setText(_translate("Dialog", user_info))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

