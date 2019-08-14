from PyQt5 import QtCore, QtGui, QtWidgets
import Logique.admin as ad
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class Ui_Admin_Connexion(object):
    def on_click_ala(self):
        ui = Ui_Admin_Ala()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_salma(self):
        ui = Ui_Admin_Salma()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Ala = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Ala.setGeometry(QtCore.QRect(70, 110, 121, 141))
        self.Ala.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ala.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ala.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ala.setIcon(icon)
        self.Ala.setIconSize(QtCore.QSize(160, 160))
        self.Ala.setObjectName("Ala")
        self.Ala.clicked.connect(lambda checked:Ui_Admin_Connexion.on_click_ala(Ui_Admin_Connexion))
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(80, 20, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_19.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(140, 70, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_20.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_20.setObjectName("label_20")
        self.salma = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.salma.setGeometry(QtCore.QRect(230, 110, 131, 141))
        self.salma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.salma.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/salma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salma.setIcon(icon1)
        self.salma.setIconSize(QtCore.QSize(140, 160))
        self.salma.setObjectName("salma")
        self.salma.clicked.connect(lambda checked:Ui_Admin_Connexion.on_click_salma(Ui_Admin_Connexion))

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(280, 260, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_18.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_18.setObjectName("label_18")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-440, 0, 971, 651))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setObjectName("label")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(120, 260, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_17.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_17.setObjectName("label_17")
        self.label.raise_()
        self.Ala.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.salma.raise_()
        self.label_18.raise_()
        self.label_17.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADMIN"))
        self.label_19.setText(_translate("MainWindow", "HELLO ALA/SALMA"))
        self.label_20.setText(_translate("MainWindow", "Connect As :"))
        self.label_18.setText(_translate("MainWindow", "SALMA"))
        self.label_17.setText(_translate("MainWindow", "ALA"))


########################################################################################################################
class Ui_Admin_Ala(object):
    def on_click_connexion(self):
        ui = Ui_Admin_Welcome()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_back(self):

        ui = Ui_Admin_Connexion()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(10, 0, 51, 51))
        self.commandLinkButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_7.setIcon(icon)
        self.commandLinkButton_7.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_7.setObjectName("commandLinkButton_7")
        self.commandLinkButton_7.clicked.connect(lambda checked:Ui_Admin_Ala.on_click_back(Ui_Admin_Ala))
        self.Ala = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Ala.setGeometry(QtCore.QRect(170, 30, 121, 141))
        self.Ala.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Ala.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/ala.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Ala.setIcon(icon1)
        self.Ala.setIconSize(QtCore.QSize(160, 160))
        self.Ala.setObjectName("Ala")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(100, 190, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_17.setObjectName("label_17")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-430, 0, 971, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(190, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon2 = QtGui.QIcon()
        self.pushButton.setIcon(icon2)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda checked:Ui_Admin_Ala.on_click_connexion(Ui_Admin_Ala))

        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 51, 51))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setText("")
        self.commandLinkButton_6.setIcon(icon)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.commandLinkButton_6.clicked.connect(lambda checked:Ui_Admin_Ala.on_click_back(Ui_Admin_Ala))

        self.label.raise_()
        self.lineEdit_4.raise_()
        self.commandLinkButton_7.raise_()
        self.Ala.raise_()
        self.label_17.raise_()
        self.pushButton.raise_()
        self.commandLinkButton_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADMIN"))
        self.label_17.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
########################################################################################################################
class Ui_Admin_Salma(object):
    def on_click_connexion(self):
        ui = Ui_Admin_Welcome()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_back(self):

        ui = Ui_Admin_Connexion()
        ui.setupUi(MainWindow)
        MainWindow.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.commandLinkButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_7.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_7.setIcon(icon)
        self.commandLinkButton_7.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_7.setObjectName("commandLinkButton_7")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 180, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(180, 230, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon1 = QtGui.QIcon()
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda checked:Ui_Admin_Salma.on_click_connexion(Ui_Admin_Salma))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-440, 0, 971, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setObjectName("label")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(90, 190, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_17.setObjectName("label_17")
        self.salma = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.salma.setGeometry(QtCore.QRect(150, 30, 131, 141))
        self.salma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.salma.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/salma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salma.setIcon(icon2)
        self.salma.setIconSize(QtCore.QSize(140, 160))
        self.salma.setObjectName("salma")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setText("")
        self.commandLinkButton_6.setIcon(icon)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.commandLinkButton_6.clicked.connect(lambda checked:Ui_Admin_Salma.on_click_back(Ui_Admin_Salma))

        self.label.raise_()
        self.commandLinkButton_7.raise_()
        self.lineEdit_4.raise_()
        self.pushButton.raise_()
        self.label_17.raise_()
        self.salma.raise_()
        self.commandLinkButton_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADMIN"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.label_17.setText(_translate("MainWindow", "Password"))

########################################################################################################################

class Ui_Admin_Welcome(object):
    def on_click_add(self):
        ui = Ui_Admin_Add()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_edit(self):

        ui = Ui_Admin_Edit()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_delete(self):

        ui = Ui_Admin_Delete()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Logout(self):

        ui = Ui_Admin_Connexion()
        ui.setupUi(MainWindow)
        MainWindow.show()

    



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-450, 0, 971, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setObjectName("label")


        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(380, 260, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.clicked.connect(lambda checked:Ui_Admin_Welcome.on_click_Logout(Ui_Admin_Welcome))

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 290, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 200, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton_4.setInputMethodHints(QtCore.Qt.ImhNone)
        icon2 = QtGui.QIcon()
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(130, 50, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton.setIcon(icon2)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda checked:Ui_Admin_Welcome.on_click_add(Ui_Admin_Welcome))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 100, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda checked:Ui_Admin_Welcome.on_click_delete(Ui_Admin_Welcome))

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 150, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda checked:Ui_Admin_Welcome.on_click_edit(Ui_Admin_Welcome))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADMIN"))
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.pushButton_4.setText(_translate("MainWindow", "Open Application"))
        self.pushButton.setText(_translate("MainWindow", "ADD Admin"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete Admin"))
        self.pushButton_3.setText(_translate("MainWindow", "Edit Admin"))

########################################################################################################################
class Ui_Admin_Add(object):
    def on_click_add(self,entreprise,username,password,email):
        try :
            ad.Admin.Add_Admin(entreprise,username,password,email)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setFixedSize(500, 500)
            msg.setText("Added successfully")
            msg.setWindowTitle("Add Admin")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("Can not add this Admin")
            msg.setInformativeText("It can be already added or the id is already token ")
            msg.setWindowTitle("ADD Admin")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()

    def on_click_back(self):

        ui = Ui_Admin_Welcome()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Logout(self):

        ui = Ui_Admin_Connexion()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-440, 0, 971, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setObjectName("label")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setTabletTracking(False)
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(125, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_21.setObjectName("label_21")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.commandLinkButton_6.clicked.connect(lambda checked:Ui_Admin_Add.on_click_back(Ui_Admin_Add))

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(98, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_20.setObjectName("label_20")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(60, 60, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_18.setObjectName("label_18")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setTabletTracking(False)
        self.lineEdit_7.setAutoFillBackground(False)
        self.lineEdit_7.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(380, 260, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.clicked.connect(lambda checked:Ui_Admin_Welcome.on_click_Logout(Ui_Admin_Welcome))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(220, 220, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon2 = QtGui.QIcon()
        self.pushButton.setIcon(icon2)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")

        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(90, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_19.setObjectName("label_19")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setTabletTracking(False)
        self.lineEdit_8.setAutoFillBackground(False)
        self.lineEdit_8.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 290, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")

        self.pushButton.clicked.connect(lambda checked:Ui_Admin_Add.on_click_add(Ui_Admin_Add,str(self.lineEdit_5.text()),
                                        str(self.lineEdit_6.text()),str(self.lineEdit_7.text()),str(self.lineEdit_8.text())))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_21.setText(_translate("MainWindow", "Email"))
        self.label_20.setText(_translate("MainWindow", "Password"))
        self.label_18.setText(_translate("MainWindow", "Company Name"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.label_19.setText(_translate("MainWindow", "User Name"))
        self.label_5.setText(_translate("MainWindow", "Log out"))


########################################################################################################################
class Ui_Admin_Edit(object):
    def on_click_edit(self,entreprise,username,password,email):
        try :
            ad.Admin.Edit_Admin(entreprise,username,password,email)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setFixedSize(500, 500)
            msg.setText("Edited successfully")
            msg.setWindowTitle("Edit Admin")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("Can not edit this Admin")

            msg.setWindowTitle("EDIT Admin")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()


    def on_click_back(self):

        ui = Ui_Admin_Welcome()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Logout(self):

        ui = Ui_Admin_Connexion()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-440, 0, 971, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setObjectName("label")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setTabletTracking(False)
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(125, 140, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_21.setObjectName("label_21")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.commandLinkButton_6.clicked.connect(lambda checked:Ui_Admin_Edit.on_click_back(Ui_Admin_Edit))

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(98, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_20.setObjectName("label_20")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(170, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(60, 60, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_18.setObjectName("label_18")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(170, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setTabletTracking(False)
        self.lineEdit_7.setAutoFillBackground(False)
        self.lineEdit_7.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(380, 260, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.clicked.connect(lambda checked:Ui_Admin_Welcome.on_click_Logout(Ui_Admin_Welcome))

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(220, 220, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon2 = QtGui.QIcon()
        self.pushButton.setIcon(icon2)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(90, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_19.setObjectName("label_19")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(170, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setTabletTracking(False)
        self.lineEdit_8.setAutoFillBackground(False)
        self.lineEdit_8.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 290, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")

        self.pushButton.clicked.connect(lambda checked:Ui_Admin_Edit.on_click_edit(Ui_Admin_Edit,str(self.lineEdit_5.text()),
                                        str(self.lineEdit_6.text()),str(self.lineEdit_7.text()),str(self.lineEdit_8.text())))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADMIN"))
        self.label_21.setText(_translate("MainWindow", "Email"))
        self.label_20.setText(_translate("MainWindow", "Password"))
        self.label_18.setText(_translate("MainWindow", "Company Name"))
        self.pushButton.setText(_translate("MainWindow", "Edit"))
        self.label_19.setText(_translate("MainWindow", "User Name"))
        self.label_5.setText(_translate("MainWindow", "Log out"))

########################################################################################################################

class Ui_Admin_Delete(object):
    def on_click_delete(self,entreprise):

        try :
            ad.Admin.Delete_Admin(entreprise)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setFixedSize(500, 500)
            msg.setText("Deleted successfully")
            msg.setWindowTitle("Delete Admin")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("Can not delete this Admin")

            msg.setWindowTitle("Delete Admin")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()

    def on_click_back(self):

        ui = Ui_Admin_Welcome()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Logout(self):

        ui = Ui_Admin_Connexion()
        ui.setupUi(MainWindow)
        MainWindow.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-440, 0, 971, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setObjectName("label")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(120, 80, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_18.setObjectName("label_18")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(180, 140, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(32, 53, 82);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon = QtGui.QIcon()
        self.pushButton.setIcon(icon)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon1)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.commandLinkButton_6.clicked.connect(lambda checked:Ui_Admin_Delete.on_click_back(Ui_Admin_Delete))

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 100, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 290, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(380, 260, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon2)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.clicked.connect(lambda checked:Ui_Admin_Welcome.on_click_Logout(Ui_Admin_Welcome))

        self.label.raise_()
        self.label_18.raise_()
        self.pushButton.raise_()
        self.lineEdit_5.raise_()
        self.label_5.raise_()
        self.commandLinkButton_6.raise_()
        self.commandLinkButton_3.raise_()
        self.pushButton.clicked.connect(lambda checked:Ui_Admin_Delete.on_click_delete(Ui_Admin_Delete,str(self.lineEdit_5.text())))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 438, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ADMIN"))
        self.label_18.setText(_translate("MainWindow", "Enter Company Name to delete"))
        self.pushButton.setText(_translate("MainWindow", "Delete"))
        self.label_5.setText(_translate("MainWindow", "Log out"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Admin_Connexion()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

