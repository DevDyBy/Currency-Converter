import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtGui import QIcon

from currency_converter import CurrencyConverter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 582)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #22222e\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 381, 131))
        self.frame.setStyleSheet("background-color: rgb(235, 47, 47)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 191, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/astronomy_earth_galaxy_planet_space_system_universe_icon_156881 (1).png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(-30, 50, 131, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/astronomy_moon_galaxy_planet_space_system_universe_icon_156880.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(140, 40, 101, 91))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("currency-exchange_88297 (2).png"))
        self.label_4.setObjectName("label_4")
        self.currency = QtWidgets.QLineEdit(self.centralwidget)
        self.currency.setGeometry(QtCore.QRect(60, 140, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.currency.setFont(font)
        self.currency.setStyleSheet("border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 39, 0, 255), stop:0.204545 rgba(255, 122, 39, 255), stop:0.630682 rgba(255, 39, 43, 255), stop:1 rgba(255, 99, 9, 255));\n"
"border-radius: 30;\n"
"color: white;")
        self.currency.setText("")
        self.currency.setToolTip("")
        self.currency.setPlaceholderText('Из валюты:')
        self.currency.setToolTip("Доступные валюты:\n  USD, RUB, EUR,\n  CHF, GBP, JPY,\n  UAH, KZT, BYN,\n  TRY, CNY, AUD,\n  CAD, PLN.")
        self.currency.setAlignment(QtCore.Qt.AlignCenter)
        self.currency.setObjectName("currency")
        self.amout = QtWidgets.QLineEdit(self.centralwidget)
        self.amout.setGeometry(QtCore.QRect(60, 220, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.amout.setFont(font)
        self.amout.setStyleSheet("border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 39, 0, 255), stop:0.204545 rgba(255, 122, 39, 255), stop:0.630682 rgba(255, 39, 43, 255), stop:1 rgba(255, 99, 9, 255));\n"
"border-radius: 30;\n"
"color: white;")
        self.amout.setText("")
        self.amout.setPlaceholderText('Сколько у меня есть:')
        self.amout.setAlignment(QtCore.Qt.AlignCenter)
        self.amout.setObjectName("amout")
        self.currency1 = QtWidgets.QLineEdit(self.centralwidget)
        self.currency1.setGeometry(QtCore.QRect(60, 300, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.currency1.setFont(font)
        self.currency1.setStyleSheet("border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 39, 0, 255), stop:0.204545 rgba(255, 122, 39, 255), stop:0.630682 rgba(255, 39, 43, 255), stop:1 rgba(255, 99, 9, 255));\n"
"border-radius: 30;\n"
"color: white;")
        self.currency1.setText("")
        self.currency1.setPlaceholderText('В валюту: ')
        self.currency1.setToolTip("Доступные валюты:\n  USD, RUB, EUR,\n  CHF, GBP, JPY,\n  UAH, KZT, BYN,\n  TRY, CNY, AUD,\n  CAD, PLN.")
        self.currency1.setAlignment(QtCore.Qt.AlignCenter)
        self.currency1.setObjectName("currency1")
        self.amout2 = QtWidgets.QLineEdit(self.centralwidget)
        self.amout2.setGeometry(QtCore.QRect(60, 380, 270, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.amout2.setFont(font)
        self.amout2.setStyleSheet("border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 39, 0, 255), stop:0.204545 rgba(255, 122, 39, 255), stop:0.630682 rgba(255, 39, 43, 255), stop:1 rgba(255, 99, 9, 255));\n"
"border-radius: 30;\n"
"color: white;")
        self.amout2.setText("")
        self.amout2.setPlaceholderText('Сколько я получу:')
        self.amout2.setAlignment(QtCore.Qt.AlignCenter)
        self.amout2.setObjectName("amout2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 470, 231, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(" QPushButton {\n"
"     color: black;\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.846636, y2:0.909, stop:0 rgba(237, 46, 0, 255), stop:0.278409 rgba(255, 48, 79, 255), stop:0.494318 rgba(255, 25, 23, 255), stop:0.965909 rgba(255, 111, 41, 255));      \n"
"     border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(192, 84, 0, 255), stop:0.323864 rgba(201, 30, 66, 255), stop:0.784091 rgba(255, 57, 59, 255), stop:1 rgba(255, 153, 84, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0,       x2:0.846636, y2:0.909, stop:0 rgba(237, 46, 0, 255), stop:0.278409 rgba(255, 48, 79, 255), stop:0.494318 rgba(255, 25, 23, 255), stop:0.965909 rgba(255, 111, 41, 255));\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setToolTip("Нажмите на эту \nкнопку, чтобы\nсконвертировать\nвалюту.")
        self.pushButton.clicked.connect(self.converter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 530, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 385, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def converter(self):
        c = CurrencyConverter()
        currency = self.currency.text()
        currency1 = self.currency1.text()
        amout = int(self.amout.text())

        amout2 = round(c.convert(amout, '%s' % (currency), '%s' % (currency1)), 2)

        self.amout2.setText(str(amout2))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Currency Converter"))
        self.label.setText(_translate("MainWindow", "КОНВЕРТЕР ВАЛЮТ"))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРОВАТЬ!"))
        self.label_5.setText(_translate("MainWindow", "By Haltteon"))         


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
