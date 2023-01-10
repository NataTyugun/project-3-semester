from PyQt5 import QtCore, QtGui, QtWidgets
import window1
import dialog1


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        Dialog.setStyleSheet("background:rgb(233, 251, 255)")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_dialog2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_dialog2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_dialog2.setObjectName("lineEdit_dialog2")
        self.gridLayout.addWidget(self.lineEdit_dialog2, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(27, -1, 27, -1)
        self.horizontalLayout.setSpacing(52)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lastButton_dialog2 = QtWidgets.QPushButton(Dialog)
        self.lastButton_dialog2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.lastButton_dialog2.setObjectName("lastButton_dialog2")
        self.horizontalLayout.addWidget(self.lastButton_dialog2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton_dialog2 = QtWidgets.QPushButton(Dialog)
        self.closeButton_dialog2.clicked.connect(self.close_dialog)
        self.closeButton_dialog2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.closeButton_dialog2.setObjectName("closeButton_dialog2")
        self.horizontalLayout.addWidget(self.closeButton_dialog2)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WEATHER_RESULT"))
        self.label.setText(_translate("Dialog", "*дата, город*"))
        self.label_2.setText(_translate("Dialog", "ПОГОДА"))
        self.label_3.setText(_translate("Dialog", "*рекомендация одежды*"))
        self.label_4.setText(_translate("Dialog", "пример одежды"))
        self.lastButton_dialog2.setText(_translate("Dialog", "НАЗАД"))
        self.closeButton_dialog2.setText(_translate("Dialog", "ЗАКРЫТЬ"))

        user_date = '23.09.2022'
        user_city = 'Санкт-Петербург'
        recomendation_clouses = 'носки, трусы и тапочки'

        self.label_3.setText(_translate("Dialog", recomendation_clouses))
        user_info = user_date + "  " + user_city
        self.label.setText(_translate("Dialog", user_info))

    def close_dialog(self):
        self.close()
