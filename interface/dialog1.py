from PyQt5 import QtCore, QtGui, QtWidgets
import window1
import dialog2

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        Dialog.setStyleSheet("background-color: rgb(225, 252, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("text-decoration: underline;\n"
"color: rgb(85, 0, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)
        self.lineEdit_dialog1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_dialog1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(85, 85, 255);")
        self.lineEdit_dialog1.setObjectName("lineEdit_dialog1")
        self.gridLayout.addWidget(self.lineEdit_dialog1, 2, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.workButton = QtWidgets.QPushButton(Dialog)
        self.workButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(57, 39, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.workButton.setObjectName("workButton")
        self.gridLayout.addWidget(self.workButton, 6, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(29, -1, 24, -1)
        self.horizontalLayout.setSpacing(39)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lastButton_dialog1 = QtWidgets.QPushButton(Dialog)
        self.lastButton_dialog1.setMouseTracking(False)
        self.lastButton_dialog1.setTabletTracking(False)
        self.lastButton_dialog1.setStyleSheet("color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.lastButton_dialog1.setAutoExclusive(False)
        self.lastButton_dialog1.setDefault(False)
        self.lastButton_dialog1.setFlat(False)
        self.lastButton_dialog1.setObjectName("lastButton_dialog1")
        self.horizontalLayout.addWidget(self.lastButton_dialog1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.nextButton_dialog1 = QtWidgets.QPushButton(Dialog)
        self.nextButton_dialog1.setStyleSheet("color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.nextButton_dialog1.setObjectName("nextButton_dialog1")
        self.horizontalLayout.addWidget(self.nextButton_dialog1)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 5)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setStyleSheet("color: rgb(225, 252, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\natalie\\boy (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.radioButton_2.setIcon(icon)
        self.radioButton_2.setIconSize(QtCore.QSize(30, 30))
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 4, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem1, 7, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 0, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 3)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setStyleSheet("color: rgb(225, 252, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:\\Users\\User\\Desktop\\natalie\\girl (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.radioButton.setIcon(icon1)
        self.radioButton.setIconSize(QtCore.QSize(30, 30))
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 4, 1, 1, 1)
        self.walkButton = QtWidgets.QPushButton(Dialog)
        self.walkButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(57, 39, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.walkButton.setIconSize(QtCore.QSize(20, 20))
        self.walkButton.setObjectName("walkButton")
        self.gridLayout.addWidget(self.walkButton, 6, 0, 1, 1)
        self.sportButton = QtWidgets.QPushButton(Dialog)
        self.sportButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(57, 39, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.sportButton.setIconSize(QtCore.QSize(20, 20))
        self.sportButton.setObjectName("sportButton")
        self.gridLayout.addWidget(self.sportButton, 6, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ПОЛЬЗОВАТЕЛЬСКАЯ ИНФОРМАЦИЯ"))
        self.label_3.setText(_translate("Dialog", "ПОЛ"))
        self.workButton.setText(_translate("Dialog", "дела"))
        self.lastButton_dialog1.setText(_translate("Dialog", "НАЗАД"))
        self.nextButton_dialog1.setText(_translate("Dialog", "ПРОДОЛЖИТЬ"))
        self.label_2.setText(_translate("Dialog", "ДАТА"))
        self.radioButton_2.setText(_translate("Dialog", "м"))
        self.label_4.setText(_translate("Dialog", "ДЕЯТЕЛЬНОСТЬ"))
        self.radioButton.setText(_translate("Dialog", "ж"))
        self.walkButton.setText(_translate("Dialog", "прогулка"))
        self.sportButton.setText(_translate("Dialog", "спорт"))
