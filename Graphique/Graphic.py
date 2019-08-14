# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import Logique.account as account
import Logique.employee as emp
import Logique.load_model as pred
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as mpl
from matplotlib import style
import seaborn as sns
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import sqlite3
from datetime import date
import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')


class Ui_Signin(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/authentification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 148, 431, 41))
        self.lineEdit_2.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(162, 117, 151, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 50, 431, 41))
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 211, 69))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_2.setObjectName("label_2")
        ###########################################
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(155, 68, 151, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 100, 431, 41))
        self.lineEdit_5.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
                                      "border-radius: 12px;\n"
                                      "padding: 10px 15px;")
        self.lineEdit_5.setObjectName("lineEdit_5")



        ###########################################


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(460, 210, 121, 41))
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
        icon1.addPixmap(QtGui.QPixmap("img/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.clicked.connect(lambda checked:self.on_click_Login(self.lineEdit_5.text(), self.entrprise_name(),self.lineEdit_2.text())
)
        self.pushButton.setObjectName("pushButton")
        """self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.clicked.connect(Ui_Signin.on_click_Signup)
        self.commandLinkButton.setGeometry(QtCore.QRect(360, 230, 321, 41))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setAutoFillBackground(False)
        self.commandLinkButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        icon = QtGui.QIcon.fromTheme("here")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setChecked(False)
        self.commandLinkButton.setAutoRepeat(False)
        self.commandLinkButton.setAutoExclusive(False)
        self.commandLinkButton.setObjectName("commandLinkButton")"""
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 195, 121, 16))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign in"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your Company Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "********"))
        self.label_2.setText(_translate("MainWindow", "Company Name:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        #self.commandLinkButton.setText(_translate("MainWindow", "Don\'t have an account ? Register from here"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><a href=\"www.gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">send mail</span></a></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Forgot your password ? "))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Enter your username"))
        self.label_5.setText(_translate("MainWindow", "Username:"))


    def entrprise_name(self):
        entreprise=str(self.lineEdit.text())
        return(entreprise)



##################################################
    def on_click_Login(self, text1, text2, text3):
        try:
            #ad.Admin.Add_Admin("fis","fis","1234","fis@global.tn")

            conn = sqlite3.connect('Attrition.db')

            c = conn.cursor()

            c.execute("""select * from Admins""")
            rows = c.fetchall()

            A = text1
            print(A)
            B = text2
            C = text3
            k = 1
            for i in range(len(rows)):
                if (rows[i][1] == A):
                    if (rows[i][2] == C):
                        ui = Ui_Admin_Welcome()
                        ui.setupUi(MainWindow, B)
                        MainWindow.show()
                        k = 0
                    else:

                        ui = Ui_SigninError()
                        ui.setupUi(MainWindow)
                        MainWindow.show()

            n = 1
            if (k == 1):
                c.execute("""select * from """ + str(B) + """_users""")
                rows2 = c.fetchall()
                for j in range(len(rows2)):
                    if (rows2[j][1] == A):
                        if (rows2[j][2] == C):
                            ui = Ui_Welcome()
                            ui.setupUi(MainWindow, B)
                            MainWindow.show()
                            n = 0
                        else:
                            ui = Ui_SigninError()
                            ui.setupUi(MainWindow, B)
                            MainWindow.show()
                if (n == 1):
                    ui = Ui_SigninError()
                    ui.setupUi(MainWindow)
                    MainWindow.show()

            # print(A)
            # print(B)
            c.close()
            conn.commit()
            conn.close()
        except :
            ui = Ui_SigninError()
            ui.setupUi(MainWindow)
            MainWindow.show()


#######################################################################################
############################ welcome ##################################################
#######################################################################################

class Ui_Welcome(object):

    def on_click_Manage(self,entreprise):
        ui = Ui_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Logout(self):
        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_statistics(self,entreprise):
        ui = Ui_Statistics()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()



    def on_click_Predict(self,entreprise):
        ui = Ui_id_predict()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()


    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(50, 30, 201, 191))
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/management.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)
        self.commandLinkButton_2.clicked.connect(lambda checked : Ui_Welcome.on_click_Manage(Ui_Welcome,entreprise))
        self.commandLinkButton_2.setIconSize(QtCore.QSize(180, 180))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(850, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(300, 30, 191, 191))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setText("")
        icon2 = QtGui.QIcon()

        icon2.addPixmap(QtGui.QPixmap("img/prediction_icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon2)
        self.commandLinkButton.setIconSize(QtCore.QSize(170, 170))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.commandLinkButton.clicked.connect(lambda checked : Ui_Welcome.on_click_Predict(Ui_Welcome,entreprise))

#-----------------------------------------------------------------------------------------

        self.commandLinkButton_10 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_10.setGeometry(QtCore.QRect(540, 25, 201, 191))
        self.commandLinkButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_10.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/statistic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_10.setIcon(icon1)
        self.commandLinkButton_10.clicked.connect(lambda checked : Ui_Welcome.on_click_statistics(Ui_Welcome,entreprise))
        self.commandLinkButton_10.setIconSize(QtCore.QSize(180, 180))
        self.commandLinkButton_10.setObjectName("commandLinkButton_2")
#-----------------------------------------------------------------------------------------
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(850, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon3)

        self.commandLinkButton_3.clicked.connect(Ui_Welcome.on_click_Logout)

        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 251, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 180, 251, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(595, 180, 251, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 210, 251, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(325, 210, 251, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 210, 251, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_9.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome"))
        self.label_5.setText(_translate("MainWindow", "Logout"))
        self.label_3.setText(_translate("MainWindow", "MANAGE"))
        self.label_4.setText(_translate("MainWindow", "PREDICT"))
        self.label_6.setText(_translate("MainWindow", "SHOW"))

        self.label_7.setText(_translate("MainWindow", "EMPLOYEES"))
        self.label_8.setText(_translate("MainWindow", "ATTRITION"))
        self.label_9.setText(_translate("MainWindow", "STATISTICS"))




#######################################################################################
############################ manage  ##################################################
#######################################################################################

class Ui_Manage(object):
    def on_click_Back(self,entreprise):
        ui = Ui_Welcome()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Logout(self):
        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Add(self,entreprise):
        ui = Ui_Add()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Delete(self,entreprise):
        ui = Ui_Delete()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Edit(self,entreprise):
        ui = Ui_Edit()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Showall(self,entreprise):
        ui = Ui_Showall()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/management.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(20, 40, 151, 151))
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)

        self.commandLinkButton_2.clicked.connect(lambda checked : Ui_Manage.on_click_Add(Ui_Manage,entreprise))

        self.commandLinkButton_2.setIconSize(QtCore.QSize(140, 140))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(850, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(190, 40, 151, 151))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon2)

        self.commandLinkButton.clicked.connect(lambda checked : Ui_Manage.on_click_Edit(Ui_Manage,entreprise))


        self.commandLinkButton.setIconSize(QtCore.QSize(140, 140))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(850, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon3)
        self.commandLinkButton_3.clicked.connect(Ui_Manage.on_click_Logout)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 170, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(370, 40, 151, 151))
        self.commandLinkButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon4)

        self.commandLinkButton_4.clicked.connect(lambda checked : Ui_Manage.on_click_Delete(Ui_Manage,entreprise))

        self.commandLinkButton_4.setIconSize(QtCore.QSize(140, 140))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 180, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_7.setObjectName("label_7")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(540, 30, 151, 171))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_5.setFont(font)
        self.commandLinkButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/showall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_5.setIcon(icon5)
        self.commandLinkButton_5.setIconSize(QtCore.QSize(150, 150))
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")

        self.commandLinkButton_5.clicked.connect(lambda checked : Ui_Manage.on_click_Showall(Ui_Manage,entreprise))

        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon6)
        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_Manage.on_click_Back(Ui_Manage,entreprise))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Employees"))
        self.label_5.setText(_translate("MainWindow", "Logout"))
        self.label_3.setText(_translate("MainWindow", "ADD EMPLOYEE"))
        self.label_4.setText(_translate("MainWindow", "UPDATE EMPLOYEE"))
        self.label_6.setText(_translate("MainWindow", "DELETE EMPLOYEE"))
        self.label_7.setText(_translate("MainWindow", "SHOW ALL"))

#################################################################################################
###############################################ADD###############################################
#################################################################################################

class Ui_Add(object):
    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_add(self, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12,
                     text13, text14, text15, text16, text17,text18):

        try :
            emp.Employee.add_Employee(text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12,
                     text13, text14, text15, text16, text17,text18)


            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setFixedSize(500, 500)
            msg.setText("Added successfully")
            msg.setWindowTitle("Add employee")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()

        except:
            # print("exception")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("Can not add this employee ")
            msg.setInformativeText("It can be already added or the id is already token ")
            msg.setWindowTitle("ADD employee")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()




    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.commandLinkButton_3.clicked.connect(Ui_Manage.on_click_Logout)

        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_Add.on_click_Back(Ui_Add,entreprise))

        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(700, 200, 71, 41))
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
        icon3 = QtGui.QIcon()
        #icon3.addPixmap(QtGui.QPixmap("../../../Desktop/GRAPHICS/UI/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(90, 150, 171, 31))
        self.dateEdit.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setProperty("showGroupSeparator", True)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1980, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDate(QtCore.QDate(2010, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(1950, 9, 14))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(1980, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 160, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 130, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 121, 171, 31))
        self.comboBox.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 191, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 181, 171, 31))
        self.comboBox_2.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 191, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_10.setObjectName("label_10")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(410, 91, 171, 31))
        self.dateEdit_2.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.dateEdit_2.setReadOnly(False)
        self.dateEdit_2.setProperty("showGroupSeparator", True)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(1950, 9, 14))
        self.dateEdit_2.setCalendarPopup(False)
        self.dateEdit_2.setDate(QtCore.QDate(2010, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 101, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(280, 161, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_12.setObjectName("label_12")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(410, 151, 171, 31))
        self.spinBox.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(410, 181, 171, 31))
        self.comboBox_4.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 61, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setTabletTracking(False)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(320, 71, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 211, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 221, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(610, 100, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_14.setObjectName("label_14")
########################################################################################################################
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(590, 130, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_19.setObjectName("label_19")

        self.spinBox_19 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_19.setGeometry(QtCore.QRect(660, 120, 171, 31))
        self.spinBox_19.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                     "border-radius: 7px;\n"
                                     "padding: 5px 5px;\n"
                                     "")
        self.spinBox_19.setMaximum(10)
        self.spinBox_19.setSingleStep(1)
        self.spinBox_19.setProperty("value", 1)
        self.spinBox_19.setObjectName("spinBox_19")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(600, 160, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_20.setObjectName("label_20")

        self.spinBox_20 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_20.setGeometry(QtCore.QRect(660, 121, 171, 31))
        self.spinBox_20.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                     "border-radius: 7px;\n"
                                     "padding: 5px 5px;\n"
                                     "")
        self.spinBox_20.setMaximum(10)
        self.spinBox_20.setSingleStep(1)
        self.spinBox_20.setProperty("value", 1)
        self.spinBox_20.setObjectName("spinBox_2")

        self.comboBox_20 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_20.setGeometry(QtCore.QRect(660, 151, 171, 31))
        self.comboBox_20.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                      "border-radius: 7px;\n"
                                      "padding: 5px 5px;\n"
                                      "")
        self.comboBox_20.setObjectName("comboBox_3")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
########################################################################################################################

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(660, 90, 171, 31))
        self.spinBox_2.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.spinBox_2.setMaximum(100000)
        self.spinBox_2.setSingleStep(5)
        self.spinBox_2.setProperty("value", 1000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(270, 130, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_15.setObjectName("label_15")
        self.spinBox_22 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_22.setGeometry(QtCore.QRect(410, 121, 171, 31))
        self.spinBox_22.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                   "border-radius: 7px;\n"
                                   "padding: 5px 5px;\n"
                                   "")
        self.spinBox_22.setObjectName("spinBox_22")
        self.spinBox_22.setMinimum(0)
        self.spinBox_22.setSingleStep(1)



        self.spinBox_21 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_21.setGeometry(QtCore.QRect(410, 209, 171, 31))
        self.spinBox_21.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                     "border-radius: 7px;\n"
                                     "padding: 5px 5px;\n"
                                     "")
        self.spinBox_21.setMaximum(1000)
        self.spinBox_21.setSingleStep(1)
        self.spinBox_21.setProperty("value", 1)
        self.spinBox_21.setObjectName("spinBox_2")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(270, 218, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(590, 70, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_18.setObjectName("label_18")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(660, 60, 171, 31))
        self.comboBox_6.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(390, 20, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_16.setObjectName("label_16")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(410, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                      "border-radius: 7px;\n"
                                      "padding: 5px 5px;\n"
                                      "")
        self.lineEdit_5.setObjectName("lineEdit_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.action(MainWindow, entreprise)

    def action(self, MainWindow, entreprise):
        self.pushButton.clicked.connect(lambda checked: self.on_click_add(self.lineEdit_5.text(),
                                                                          self.lineEdit.text(),
                                                                          self.lineEdit_2.text(),
                                                                          self.comboBox.currentText(),
                                                                          str(self.dateEdit.date().day()) + '/' + str(
                                                                              self.dateEdit.date().month()) + '/' + str(
                                                                              self.dateEdit.date().year()),
                                                                          self.comboBox_2.currentText(),
                                                                          self.lineEdit_3.text(),
                                                                          self.lineEdit_4.text(),
                                                                          str(self.dateEdit_2.date().year()),
                                                                          self.spinBox_22.text(),
                                                                          self.spinBox.text(),
                                                                          self.comboBox_4.currentText(),
                                                                          self.spinBox_21.text(),
                                                                          self.comboBox_6.currentText(),
                                                                          self.spinBox_2.text(),
                                                                          self.spinBox_19.text(),
                                                                          self.comboBox_20.currentText(),
                                                                          str(entreprise)
                                                                          ))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add employee"))
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.label_3.setText(_translate("MainWindow", "First Name"))
        self.label_4.setText(_translate("MainWindow", "Last Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.label_6.setText(_translate("MainWindow", "Date of Birth"))
        self.label_7.setText(_translate("MainWindow", "Sex"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.label_8.setText(_translate("MainWindow", "Status"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Single"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Engaged"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Married"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Divorced"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Widowed"))
        self.label_10.setText(_translate("MainWindow", "Over Time"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.label_11.setText(_translate("MainWindow", "Year of employment"))
        self.label_12.setText(_translate("MainWindow", "Companies Worked"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "No"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Department"))
        self.label_13.setText(_translate("MainWindow", "Department"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Occupation"))
        self.label_9.setText(_translate("MainWindow", "Occupation"))
        self.label_14.setText(_translate("MainWindow", "Salary"))
        #self.spinBox_2.setSuffix(_translate("MainWindow", " Dinars"))
        self.label_15.setText(_translate("MainWindow", "Total Working Years"))


        self.label_17.setText(_translate("MainWindow", "Distance from home"))
        self.label_18.setText(_translate("MainWindow", "Motorized"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "No"))
        self.label_16.setText(_translate("MainWindow", "ID"))
        self.lineEdit_5.setText(_translate("MainWindow", ""))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "ID"))
        self.label_19.setText(_translate("MainWindow", "Job Level"))
        self.label_20.setText(_translate("MainWindow", "Missions"))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "Non-Travel"))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "Travel_Rarely"))
        self.comboBox_20.setItemText(2, _translate("MainWindow", "Travel_Frequently"))
        #self.spinBox_21.setSuffix(_translate("MainWindow", " Km"))





#################################################################################################
#############################################Delete##############################################
#################################################################################################

class Ui_Delete(object):

    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()


    def on_click_delete(self,text1,text2):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        A = text1
        B =str(text2)

        c.execute("select * from " + B + " where Id= " + A)
        rows = c.fetchall()

        if (rows.__len__()==0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500,500)
            msg.setText("Enter a valid ID ")
            msg.setWindowTitle("Delete Account")
            msg.setStandardButtons(QMessageBox.Ok )
            msg.exec_()
            msg.show()
        else:

            try :

                emp.Employee.delete_Employee(text1,text2)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setFixedSize(500,500)
                msg.setText("Deleted successfully" )
                #msg.setInformativeText("Deleted successfully ")
                msg.setWindowTitle("Delete employee")
                msg.setStandardButtons(QMessageBox.Ok )
                msg.exec_()
                msg.show()
            except :
                #print("exception")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setFixedSize(500,500)
                msg.setText("Can not delete this employee ")
               # msg.setInformativeText("Enter employee id ")
                msg.setWindowTitle("Delete employee")
                msg.setStandardButtons(QMessageBox.Ok )
                msg.exec_()
                msg.show()



    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.commandLinkButton_3.clicked.connect(Ui_Delete.on_click_Logout)

        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_Delete.on_click_Back(Ui_Delete,entreprise))

        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(100, 150, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_16.setObjectName("label_16")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(480, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 140, 101, 41))
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
        icon3 = QtGui.QIcon()
        #icon3.addPixmap(QtGui.QPixmap("../../../Desktop/GRAPHICS/UI/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.clicked.connect(lambda checked: self.on_click_delete((self.lineEdit_5.text()), str(entreprise)))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete employee"))
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.label_16.setText(_translate("MainWindow", "ENTER ID OF EMPLYEE TO DELETE"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "id"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))

#######################################################################################
###############################update##################################################
#######################################################################################


class Ui_Edit(object):
    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Enter(self,text1,text2):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        A = text1
        B=str(text2)
        c.execute("""select * from """ + B)
        rows = c.fetchall()
        k=1
        for i in range(len(rows)):
            if (A == str(rows[i][0])):
                self.pushButton.setEnabled(True)
                self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(32, 53, 82);\n"
                                              "border-radius: 12px;\n"
                                              "box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
                                              "box-shadow: 0 5px #666;\n"
                                              "transform: translateY(4px) ;\n"
                                              "")
                k=0
        if(k==1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("this id does not correspond to any employee")
            # msg.setInformativeText("Enter employee id ")
            msg.setWindowTitle("Edit employee")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()
        conn.commit()
        conn.close()


    def on_click_edit(self, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12,
                      text13, text14, text15, text16,text17,text18):


        try:
            emp.Employee.edit_Employee(text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12,
                     text13, text14, text15, text16, text17,text18)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setFixedSize(500,500)
            msg.setText("Updated successfully" )
            #msg.setInformativeText("Deleted successfully ")
            msg.setWindowTitle("Update employee")
            msg.setStandardButtons(QMessageBox.Ok )
            msg.exec_()
            msg.show()
        except :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500,500)
            msg.setText("Can not update this employee ")
           # msg.setInformativeText("Enter employee id ")
            msg.setWindowTitle("Update employee")
            msg.setStandardButtons(QMessageBox.Ok )
            msg.exec_()
            msg.show()





    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/update.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.commandLinkButton_3.clicked.connect(Ui_Edit.on_click_Logout)

        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_Edit.on_click_Back(Ui_Edit,entreprise))

        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(700, 220, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(168, 175, 208);\n"
"border-radius: 12px;\n"
"box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
"box-shadow: 0 5px #666;\n"
"transform: translateY(4px) ;\n"
"")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon3 = QtGui.QIcon()
        self.pushButton.setIcon(icon3)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit.setFont(font)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(90, 180, 171, 31))
        self.dateEdit.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setProperty("showGroupSeparator", True)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1980, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setMaximumDate(QtCore.QDate(2010, 12, 31))
        self.dateEdit.setMinimumDate(QtCore.QDate(1950, 9, 14))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate(1980, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 190, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 160, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 151, 171, 31))
        self.comboBox.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 221, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 211, 171, 31))
        self.comboBox_2.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 221, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_10.setObjectName("label_10")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(410, 121, 171, 31))
        self.dateEdit_2.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.dateEdit_2.setReadOnly(False)
        self.dateEdit_2.setProperty("showGroupSeparator", True)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2010, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setMaximumDate(QtCore.QDate(2050, 12, 31))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(1950, 9, 14))
        self.dateEdit_2.setCalendarPopup(False)
        self.dateEdit_2.setDate(QtCore.QDate(2010, 1, 1))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(270, 131, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(280, 191, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_12.setObjectName("label_12")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(410, 181, 171, 31))
        self.spinBox.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.spinBox.setObjectName("spinBox")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(410, 211, 171, 31))
        self.comboBox_4.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 91, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setTabletTracking(False)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(320, 101, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 241, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 251, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(610, 130, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_14.setObjectName("label_14")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(660, 120, 171, 31))
        self.spinBox_2.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.spinBox_2.setMaximum(100000)
        self.spinBox_2.setSingleStep(5)
        self.spinBox_2.setProperty("value", 1000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(270, 160, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(190, 40, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_16.setObjectName("label_16")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 30, 61, 31))
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
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 30, 81, 31))
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
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda checked: self.on_click_Enter(self.lineEdit_5.text(),entreprise))
        ########################################################################################################################
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(590, 160, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_19.setObjectName("label_19")

        self.spinBox_19 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_19.setGeometry(QtCore.QRect(660, 180, 171, 31))
        self.spinBox_19.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                      "border-radius: 7px;\n"
                                      "padding: 5px 5px;\n"
                                      "")
        self.spinBox_19.setMaximum(10)
        self.spinBox_19.setSingleStep(1)
        self.spinBox_19.setProperty("value", 1)
        self.spinBox_19.setObjectName("spinBox_19")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(600, 190, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_20.setObjectName("label_20")

        self.spinBox_20 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_20.setGeometry(QtCore.QRect(660, 151, 171, 31))
        self.spinBox_20.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                      "border-radius: 7px;\n"
                                      "padding: 5px 5px;\n"
                                      "")
        self.spinBox_20.setMaximum(10)
        self.spinBox_20.setSingleStep(1)
        self.spinBox_20.setProperty("value", 1)
        self.spinBox_20.setObjectName("spinBox_2")

        self.comboBox_20 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_20.setGeometry(QtCore.QRect(660, 181, 171, 31))
        self.comboBox_20.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                       "border-radius: 7px;\n"
                                       "padding: 5px 5px;\n"
                                       "")
        self.comboBox_20.setObjectName("comboBox_3")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        ########################################################################################################################

        self.spinBox_21 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_21.setGeometry(QtCore.QRect(410, 239, 171, 31))
        self.spinBox_21.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                      "border-radius: 7px;\n"
                                      "padding: 5px 5px;\n"
                                      "")
        self.spinBox_21.setMaximum(1000)
        self.spinBox_21.setSingleStep(1)
        self.spinBox_21.setProperty("value", 1)
        self.spinBox_21.setObjectName("spinBox_2")


        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(270, 248, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_17.setObjectName("label_17")

        self.spinBox_22 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_22.setGeometry(QtCore.QRect(410, 151, 171, 31))
        self.spinBox_22.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                      "border-radius: 7px;\n"
                                      "padding: 5px 5px;\n"
                                      "")
        self.spinBox_22.setMinimum(1)
        self.spinBox_22.setSingleStep(1)
        self.spinBox_22.setProperty("value", 1)
        self.spinBox_22.setObjectName("spinBox_2")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(590, 100, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_18.setObjectName("label_18")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(660, 90, 171, 31))
        self.comboBox_6.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.action(MainWindow, entreprise)


    def action(self, MainWindow, entreprise):
        self.pushButton.clicked.connect(lambda checked: self.on_click_edit(self.lineEdit_5.text(), self.lineEdit.text(),
                                                                           self.lineEdit_2.text(),
                                                                           self.comboBox.currentText(),
                                                                           str(
                                                                               self.dateEdit.date().day()) + '/' + str(
                                                                               self.dateEdit.date().month()) + '/' + str(
                                                                               self.dateEdit.date().year()),
                                                                           self.comboBox_2.currentText(),
                                                                           self.lineEdit_3.text(),
                                                                           self.lineEdit_4.text(),
                                                                           str(self.dateEdit_2.date().year()),
                                                                           self.spinBox_22.text(),
                                                                           self.spinBox.text(),
                                                                           self.comboBox_4.currentText(),
                                                                           self.spinBox_21.text(),
                                                                           self.comboBox_6.currentText(),
                                                                           self.spinBox_2.text(),
                                                                           self.spinBox_19.text(),
                                                                           self.comboBox_20.currentText(),
                                                                           str(entreprise)
                                                                           ))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edit employee"))
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.pushButton.setText(_translate("MainWindow", "Edit"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "First Name"))
        self.label_3.setText(_translate("MainWindow", "First Name"))
        self.label_4.setText(_translate("MainWindow", "Last Name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.label_6.setText(_translate("MainWindow", "Date of Birth"))
        self.label_7.setText(_translate("MainWindow", "Sex"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.label_8.setText(_translate("MainWindow", "Status"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Single"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Engaged"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Married"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Divorced"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Widowed"))
        self.label_10.setText(_translate("MainWindow", "Over Time"))
        self.dateEdit_2.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.label_11.setText(_translate("MainWindow", "Year of employment"))
        self.label_12.setText(_translate("MainWindow", "Companies Worked"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "No"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Department"))
        self.label_13.setText(_translate("MainWindow", "Department"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Occupation"))
        self.label_9.setText(_translate("MainWindow", "Occupation"))
        self.label_14.setText(_translate("MainWindow", "Salary"))
        #self.spinBox_2.setSuffix(_translate("MainWindow", " Dinars"))
        self.label_15.setText(_translate("MainWindow", "Total Working Years"))

        self.label_16.setText(_translate("MainWindow", "ENTER ID OF EMPLOYEE TO EDIT"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "id"))
        self.pushButton_2.setText(_translate("MainWindow", "ENTER"))

        self.label_17.setText(_translate("MainWindow", "Distance from home"))
        self.label_18.setText(_translate("MainWindow", "Motorized"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Yes"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "No"))
        self.label_19.setText(_translate("MainWindow", "Job Level"))
        self.label_20.setText(_translate("MainWindow", "Missions"))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "Non-Travel"))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "Travel_Rarely"))
        self.comboBox_20.setItemText(2, _translate("MainWindow", "Travel_Frequently"))
        #self.spinBox_21.setSuffix(_translate("MainWindow", " Km"))


######################################################################################################
#########################################signinError########################################################
#################################################################################################
class Ui_SigninError(object):
    def on_click_Signup(self):

        ui = Ui_Signup()
        ui.setupUi(MainWindow)
        MainWindow.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/authentification.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 148, 431, 41))
        self.lineEdit_2.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
                                        "background-color: rgb(255, 102, 102);\n"

"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(162, 117, 151, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 50, 431, 41))
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
                                    "background-color: rgb(255, 102, 102);\n"
"border-radius: 12px;\n"
"padding: 10px 15px; ")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 40, 211, 69))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_2.setObjectName("label_2")

        ###########################################
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(155, 68, 151, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 100, 431, 41))
        self.lineEdit_5.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
                                      "background-color: rgb(255, 102, 102);\n"

                                      "border-radius: 12px;\n"
                                      "padding: 10px 15px;")
        self.lineEdit_5.setObjectName("lineEdit_5")

        ###########################################

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(460, 210, 121, 41))
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
        icon1.addPixmap(QtGui.QPixmap("img/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.clicked.connect(lambda checked:self.on_click_Login(self.lineEdit_5.text(), self.entrprise_name(),self.lineEdit_2.text()))
        self.pushButton.setObjectName("pushButton")
        """
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.clicked.connect(Ui_SigninError.on_click_Signup)
        self.commandLinkButton.setGeometry(QtCore.QRect(360, 230, 321, 41))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setAutoFillBackground(False)
        self.commandLinkButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        icon = QtGui.QIcon.fromTheme("here")
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setChecked(False)
        self.commandLinkButton.setAutoRepeat(False)
        self.commandLinkButton.setAutoExclusive(False)
        self.commandLinkButton.setObjectName("commandLinkButton")
        """
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 195, 121, 16))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign in"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Or you are not already registered"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Company Name and password are not compatible"))
        self.label_2.setText(_translate("MainWindow", "Company Name:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        #self.commandLinkButton.setText(_translate("MainWindow", "Don\'t have an account ? Register from here"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><a href=\"www.gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">send mail</span></a></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Forgot your password ? "))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Enter your username"))
        self.label_5.setText(_translate("MainWindow", "Username:"))

    def entrprise_name(self):
        entreprise = str(self.lineEdit.text())
        return (entreprise)
##################################################
    def on_click_Login(self, text1, text2, text3):
        try:
            conn = sqlite3.connect('Attrition.db')
            c = conn.cursor()
            c.execute("""select * from Admins""")
            rows = c.fetchall()

            # print(rows)
            A = text1
            print(A)
            B = text2
            C = text3
            k = 1
            for i in range(len(rows)):
                if (rows[i][1] == A):
                    if (rows[i][2] == C):
                        ui = Ui_Admin_Welcome()
                        ui.setupUi(MainWindow, B)
                        MainWindow.show()
                        k = 0
                    else:

                        ui = Ui_SigninError()
                        ui.setupUi(MainWindow)
                        MainWindow.show()

            n = 1
            if (k == 1):
                c.execute("""select * from """ + str(B) + """_users""")
                rows2 = c.fetchall()
                for j in range(len(rows2)):
                    if (rows2[j][1] == A):
                        if (rows2[j][2] == C):
                            ui = Ui_Welcome()
                            ui.setupUi(MainWindow, B)
                            MainWindow.show()
                            n = 0
                        else:
                            ui = Ui_SigninError()
                            ui.setupUi(MainWindow, B)
                            MainWindow.show()
                if (n == 1):
                    ui = Ui_SigninError()
                    ui.setupUi(MainWindow)
                    MainWindow.show()

            # print(A)
            # print(B)
            c.close()
            conn.commit()
            conn.close()
        except :
            ui = Ui_SigninError()
            ui.setupUi(MainWindow)
            MainWindow.show()


###########################################################################################
######################################id_predict###########################################
###########################################################################################
class Ui_id_predict(object):

    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Welcome()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Show(self,id,entreprise):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        A = id
        B=str(entreprise)
        c.execute("""select * from """ + B)
        rows = c.fetchall()
        k=1
        for i in range(len(rows)):
            if (A == str(rows[i][0])):
                k=0
                ui = Ui_Prediction()
                ui.setupUi(MainWindow, id,entreprise)
                MainWindow.show()
        if(k==1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("this id does not correspond to any employee")
            # msg.setInformativeText("Enter employee id ")
            msg.setWindowTitle("Predict employee")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()
        conn.commit()
        conn.close()

    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/prediction icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.commandLinkButton_3.clicked.connect(Ui_Delete.on_click_Logout)

        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)

        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_id_predict.on_click_Back(Ui_id_predict,entreprise))

        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(95, 150, 400, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_16.setObjectName("label_16")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(490, 140, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 140, 135, 41))
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
        icon3 = QtGui.QIcon()
        #icon3.addPixmap(QtGui.QPixmap("../../../Desktop/GRAPHICS/UI/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.clicked.connect(lambda checked: self.on_click_Show((self.lineEdit_5.text()), str(entreprise)))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Predict attrition"))
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.label_16.setText(_translate("MainWindow", "ENTER ID OF EMPLOYEE TO PREDICT"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "id"))
        self.pushButton_2.setText(_translate("MainWindow", "Show results"))


#######################################################################################
####################################showall############################################
#######################################################################################


class Ui_Showall(object):

    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_show(self, text):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()

        A = c.execute("""select * from """ + str(text))

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(A):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.commit()
        conn.close()

    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/showall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-190, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 470, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")

        self.commandLinkButton_3.clicked.connect(lambda checked : Ui_Showall.on_click_Logout(Ui_Showall))

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, -70, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 500, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))

        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_Showall.on_click_Back(Ui_Showall,entreprise))

        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 500, 101, 41))
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
        icon3 = QtGui.QIcon()
       # icon3.addPixmap(QtGui.QPixmap("../../../Desktop/GRAPHICS/UI/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 20, 851, 461))
        self.tableWidget.setStyleSheet("Back-ground color : rgb(228, 228, 228)")
        self.tableWidget.setLineWidth(27)
        self.tableWidget.setMidLineWidth(27)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(17)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, -180, 821, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 500, 141, 41))
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
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setChecked(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 40, 841, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 510, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.action(MainWindow, entreprise)

    def action(self, MainWindow, entreprise):
        self.pushButton_2.clicked.connect(lambda checked: self.on_click_show(entreprise))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show all employees"))
        self.pushButton_2.setText(_translate("MainWindow", "Show all"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sex"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date of Birth"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Occupation"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Departement"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Year of employment"))

        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Total Working Years"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Companies Worked"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Over Time"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Distance from home"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Motorized"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Salary"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Job_Level"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Missions"))
        self.pushButton_3.setText(_translate("MainWindow", "Show Statistics"))
        self.label_5.setText(_translate("MainWindow", "Log out"))


#######################################################################################
###############################res_predict#############################################
#######################################################################################

class Ui_Prediction(object):

    def on_click_Back(self, entreprise):
        ui = Ui_id_predict()
        ui.setupUi(MainWindow, entreprise)
        MainWindow.show()

    def on_click_Logout(self):
        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Show(self,id, entreprise):
        A = str(id)
        B = str(entreprise)
        # print(A,type(A))
        # print(B,type(B))
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        c.execute("select * from " + B + " where Id= " + A)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        return (rows)

    def Predict_res(self,Date,Travel,Dept,Distance,Education,Sex,Level,Status,Salary,NumberCompanies,OverTime,Experience,Embauche):
        curr_year= date.today().year
        Age=int(curr_year) - int(Date[-4:])
        YearsAtCompany=int(curr_year) - int(Embauche)
        employé= np.array([int(Age),pred.TraveltoInt(str(Travel)),pred.DepttoInt(str(Dept)),int(Distance),int(Education),pred.SextoInt(str(Sex)),int(Level),pred.StatustoInt(str(Status)),int(Salary), int(NumberCompanies),pred.OverTimetoInt(str(OverTime)),int(Experience),int(YearsAtCompany)])
        print(pred.predictEmp(employé))
        return (pred.predictEmp(employé))



    def setupUi(self, MainWindow,id,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/prediction icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 460, 61, 71))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_3.clicked.connect(lambda checked : Ui_Prediction.on_click_Logout(Ui_Prediction))

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")

        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_Prediction.on_click_Back(Ui_Prediction,entreprise))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 131, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/employee.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 100, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 130, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 160, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 190, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 230, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 290, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 320, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 350, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 230, 220, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(460, 260, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(460, 290, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(460, 320, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(460, 350, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(250, 420, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(340, 100, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(340, 130, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(280, 160, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(350, 190, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(180, 230, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(190, 260, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(200, 290, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(270, 320, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(260, 350, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(690, 230, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(570, 260, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(640, 290, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(560, 320, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(530, 350, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(480, 420, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(-10, 300, 991, 261))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap("img/arriere.jpg"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(760, 160, 111, 141))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("img/1.jpg"))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(820, 150, 31, 20))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("img/1.jpg"))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(220, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(260, 70, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_38.setObjectName("label_38")

        self.label_52 = QtWidgets.QLabel(self.centralwidget)
        self.label_52.setGeometry(QtCore.QRect(180, 380, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_52.setObjectName("label_52")


        #######################################################
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setGeometry(QtCore.QRect(460, 380, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_51.setObjectName("label_51")

        #################################
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(70, 380, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_50.setObjectName("label_50")
        ################################
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        self.label_53.setGeometry(QtCore.QRect(560, 380, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_53.setObjectName("label_53")





        self.label.raise_()
        self.label_34.raise_()
        self.label_32.raise_()
        self.layoutWidget.raise_()
        self.commandLinkButton_6.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_5.raise_()
        self.commandLinkButton_3.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_18.raise_()
        self.label_33.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.label_50.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.label_53.raise_()


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow,id,entreprise)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow,id,entreprise):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prediction Result"))
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.label_3.setText(_translate("MainWindow", "First Name :"))
        self.label_4.setText(_translate("MainWindow", "Last Name :"))
        self.label_6.setText(_translate("MainWindow", "Sex :"))
        self.label_7.setText(_translate("MainWindow", "Date of Birth :"))
        self.label_8.setText(_translate("MainWindow", "Civil Status :"))
        self.label_9.setText(_translate("MainWindow", "Occupation :"))
        self.label_10.setText(_translate("MainWindow", "Departement :"))
        self.label_11.setText(_translate("MainWindow", "Year of Employement :"))
        self.label_12.setText(_translate("MainWindow", "Total Working Years :"))
        self.label_13.setText(_translate("MainWindow", "N° Companies Worked at :"))
        self.label_14.setText(_translate("MainWindow", "Over Time :"))
        self.label_15.setText(_translate("MainWindow", "Distance from Home :"))
        self.label_16.setText(_translate("MainWindow", "Motorized :"))
        self.label_17.setText(_translate("MainWindow", "Salary :"))
        self.label_18.setText(_translate("MainWindow", "ATTRITION :"))
        self.label_19.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][1])))
        self.label_20.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][2])))
        self.label_21.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][3])))
        self.label_22.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][4])))
        self.label_23.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][5])))
        self.label_24.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][6])))
        self.label_25.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][7])))
        self.label_26.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][8])))
        self.label_27.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][9])))
        self.label_28.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][10])))
        self.label_29.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][11])))
        self.label_30.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][12]+" Km")))
        self.label_31.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][13])))
        self.label_32.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][14]+" Dinars")))


        self.label_33.setText(_translate("MainWindow",str(self.Predict_res(str(self.on_click_Show(str(id),str(entreprise))[0][4]),str(self.on_click_Show(str(id),str(entreprise))[0][16]),
                                         str(self.on_click_Show(str(id), str(entreprise))[0][7]),str(self.on_click_Show(str(id),str(entreprise))[0][12]),
                                         str(self.on_click_Show(str(id), str(entreprise))[0][6]),str(self.on_click_Show(str(id),str(entreprise))[0][3]),
                                         str(self.on_click_Show(str(id), str(entreprise))[0][15]),str(self.on_click_Show(str(id),str(entreprise))[0][5]),
                                         str(self.on_click_Show(str(id), str(entreprise))[0][14]),str(self.on_click_Show(str(id),str(entreprise))[0][10]),
                                         str(self.on_click_Show(str(id), str(entreprise))[0][11]),str(self.on_click_Show(str(id),str(entreprise))[0][9]),
                                         str(self.on_click_Show(str(id), str(entreprise))[0][8])))))
        self.label_37.setText(_translate("MainWindow", "ID :"))
        self.label_38.setText(_translate("MainWindow", str(self.on_click_Show(str(id),str(entreprise))[0][0])))
        self.label_50.setText(_translate("MainWindow", "Job Level :"))
        self.label_51.setText(_translate("MainWindow", "Missions :"))
        self.label_52.setText(_translate("MainWindow", str(self.on_click_Show(str(id), str(entreprise))[0][15])))
        self.label_53.setText(_translate("MainWindow", str(self.on_click_Show(str(id), str(entreprise))[0][16])))



######################################################################################################
#####################################################################################################
########################Admin_welcome##################################################################
######################################################################################################

class Ui_Admin_Welcome(object):

    def on_click_ManageAccount(self,entreprise):
        ui = Ui_Admin_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Logout(self):
        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_ManageAndPredict(self,entreprise):
        ui = Ui_Welcome()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()


    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(110, 40, 201, 191))
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Manageemploeeadmin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)

        self.commandLinkButton_2.clicked.connect(lambda checked: Ui_Admin_Welcome.on_click_ManageAccount(Ui_Admin_Welcome, entreprise))
        self.commandLinkButton_2.setIconSize(QtCore.QSize(180, 180))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(860, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(445, 40, 191, 191))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/manageadmin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon2)
        self.commandLinkButton.setIconSize(QtCore.QSize(170, 170))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.commandLinkButton.clicked.connect(lambda checked: Ui_Admin_Welcome.on_click_ManageAndPredict(Ui_Admin_Welcome, entreprise))

        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(850, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon3)

        self.commandLinkButton_3.clicked.connect(Ui_Welcome.on_click_Logout)

        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(85, 180, 251, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 180, 280, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 205, 300, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_6.setObjectName("label_6")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(160, -36, 1000, 109))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_20.setObjectName("label_20")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow,entreprise)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow,entreprise):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome"))
        self.label_5.setText(_translate("MainWindow", "Logout"))
        self.label_3.setText(_translate("MainWindow", "MANAGE ACCOUNTS"))
        self.label_4.setText(_translate("MainWindow", "MANAGE EMPLOYEES"))
        self.label_6.setText(_translate("MainWindow", "AND PREDICT ATTRITION"))
        self.label_20.setText(_translate("MainWindow", "Welcome Mr "+ str(entreprise)+"'s ADMIN, you can:"))

#########################################################################################
###################################Admin_manage#########################################
###############################################################################

class Ui_Admin_Manage(object):
    def on_click_Back(self,entreprise):
        ui = Ui_Admin_Welcome()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Logout(self):
        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Add(self,entreprise):
        ui = Ui_Admin_Add_Account()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Delete(self,entreprise):
        ui = Ui_Admin_Delete()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Edit(self,entreprise):
        ui = Ui_Admin_Edit_Account()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Showall(self,entreprise):
        ui = Ui_Admin_Showall()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/management.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(20, 40, 151, 151))
        self.commandLinkButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Admin_Add_Employee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon1)

        self.commandLinkButton_2.clicked.connect(
            lambda checked: Ui_Admin_Manage.on_click_Add(Ui_Admin_Manage, entreprise))

        self.commandLinkButton_2.setIconSize(QtCore.QSize(140, 140))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(860, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(190, 40, 151, 151))
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/Admin_update_Employee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon2)

        self.commandLinkButton.clicked.connect(
            lambda checked: Ui_Admin_Manage.on_click_Edit(Ui_Admin_Manage, entreprise))

        self.commandLinkButton.setIconSize(QtCore.QSize(140, 140))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(850, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon3)
        #        self.commandLinkButton_3.clicked.connect(Ui_Manage.on_click_Logout)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 170, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(370, 40, 151, 151))
        self.commandLinkButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/Admin_delete_employee.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon4)

        self.commandLinkButton_4.clicked.connect(
            lambda checked: Ui_Admin_Manage.on_click_Delete(Ui_Admin_Manage, entreprise))

        self.commandLinkButton_4.setIconSize(QtCore.QSize(140, 140))
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 180, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 190, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_7.setObjectName("label_7")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(560, 30, 151, 171))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.commandLinkButton_5.setFont(font)
        self.commandLinkButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_5.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/Admin_show_employeeAccount.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_5.setIcon(icon5)
        self.commandLinkButton_5.setIconSize(QtCore.QSize(150, 150))
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")

        self.commandLinkButton_5.clicked.connect(
            lambda checked: Ui_Admin_Manage.on_click_Showall(Ui_Admin_Manage, entreprise))

        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon6)
        self.commandLinkButton_6.clicked.connect(
            lambda checked: Ui_Admin_Manage.on_click_Back(Ui_Admin_Manage, entreprise))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Account"))
        self.label_5.setText(_translate("MainWindow", "Logout"))
        self.label_3.setText(_translate("MainWindow", "ADD ACCOUNT"))
        self.label_4.setText(_translate("MainWindow", "UPDATE ACCOUNT"))
        self.label_6.setText(_translate("MainWindow", "DELETE ACCOUNT"))
        self.label_7.setText(_translate("MainWindow", "SHOW ALL ACCOUNTS"))
########################################################################################################################
##########################################Admin_Add_Account#############################################################
########################################################################################################################

class Ui_Admin_Add_Account(object):

    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Admin_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_add_Account(self,entreprise,text2, text3,text4,text5):
        if (text3 == text5):
            try :
                account.Account.Add_Account(entreprise, text2, text3, text4)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setFixedSize(500, 500)
                msg.setText("Added successfully")
                msg.setWindowTitle("Add Account")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                msg.show()
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setFixedSize(500, 500)
                msg.setText("Can not add this account ")
                msg.setInformativeText("It can be already added or the username is already token")
                msg.setWindowTitle("ADD Account")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                msg.show()
        else :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("Error ")
            msg.setInformativeText("Passwords are incompatible")
            msg.setWindowTitle("ADD Account")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()



    def setupUi(self, MainWindow,entreprise):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(931, 565)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/signup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            MainWindow.setWindowIcon(icon)
            MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
            self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
            self.layoutWidget.setObjectName("layoutWidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
            self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
            self.label.setAutoFillBackground(False)
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
            self.label.setScaledContents(True)
            self.label.setWordWrap(True)
            self.label.setOpenExternalLinks(True)
            self.label.setObjectName("label")
            ####
            self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_6.setGeometry(QtCore.QRect(225, 30, 400, 41))
            self.lineEdit_6.setTabletTracking(False)
            self.lineEdit_6.setAutoFillBackground(False)
            self.lineEdit_6.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
                                          "border-radius: 12px;\n"
                                          "padding: 10px 15px;")
            #####

            self.label_6 = QtWidgets.QLabel(self.centralwidget)
            self.label_6.setGeometry(QtCore.QRect(120, 30, 141, 51))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.label_6.setFont(font)
            self.label_6.setStyleSheet("color: rgb(9, 26, 52);")
            self.label_6.setObjectName("label_2")
            ####

            self.pushButton = QtWidgets.QPushButton(self.centralwidget)

            self.pushButton.setEnabled(True)
            self.pushButton.setGeometry(QtCore.QRect(360, 240, 100, 41))
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
            # icon1.addPixmap(QtGui.QPixmap("unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon1)
            self.pushButton.setCheckable(False)
            self.pushButton.setChecked(False)
            self.pushButton.setAutoRepeat(False)
            self.pushButton.setAutoExclusive(False)
            self.pushButton.setDefault(True)
            self.pushButton.setFlat(False)
            self.pushButton.setObjectName("pushButton")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(162, 80, 51, 51))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.label_4.setFont(font)
            self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
            self.label_4.setObjectName("label_4")
            self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_3.setGeometry(QtCore.QRect(225, 80, 400, 41))
            self.lineEdit_3.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
                                          "border-radius: 12px;\n"
                                          "padding: 10px 15px;")
            self.lineEdit_3.setObjectName("lineEdit_3")
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setGeometry(QtCore.QRect(130, 125, 100, 61))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.label_5.setFont(font)
            self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
            self.label_5.setObjectName("label_5")
            self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_4.setGeometry(QtCore.QRect(225, 130, 400, 41))
            self.lineEdit_4.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
                                          "border-radius: 12px;\n"
                                          "padding: 10px 15px;")
            self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
            self.lineEdit_4.setObjectName("lineEdit_4")
            self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
            self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 41, 51))
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.commandLinkButton.setIcon(icon2)
            self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

            self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
            self.commandLinkButton.setObjectName("commandLinkButton")
            self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.commandLinkButton.clicked.connect(lambda checked: Ui_Admin_Add_Account.on_click_Back(Ui_Admin_Add_Account,entreprise))
            self.pushButton.clicked.connect(lambda checked: self.on_click_add_Account(str(entreprise),self.lineEdit_6.text(), self.lineEdit_4.text(), self.lineEdit_3.text(),self.lineEdit_5.text()))
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(62, 180, 200, 51))
            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.label_3.setFont(font)
            self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
            self.label_3.setObjectName("label_3")
            self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_5.setGeometry(QtCore.QRect(225, 180, 400, 41))
            self.lineEdit_5.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
                                          "border-radius: 12px;\n"
                                          "padding: 10px 15px;")
            self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
            self.lineEdit_5.setObjectName("lineEdit_5")
            self.label.raise_()
            self.layoutWidget.raise_()
            self.pushButton.raise_()
            self.label_4.raise_()
            self.lineEdit_3.raise_()

            self.label_6.raise_()
            self.lineEdit_6.raise_()
            self.label_5.raise_()
            self.lineEdit_4.raise_()
            self.commandLinkButton.raise_()
            self.label_3.raise_()
            self.lineEdit_5.raise_()

            self.label_9 = QtWidgets.QLabel(self.centralwidget)
            self.label_9.setGeometry(QtCore.QRect(855, 500, 71, 41))
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setItalic(False)
            font.setWeight(75)
            self.label_9.setFont(font)
            self.label_9.setStyleSheet("color: rgb(9, 26, 52);")
            self.label_9.setObjectName("label_9")

            self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
            self.commandLinkButton_3.setGeometry(QtCore.QRect(850, 460, 61, 61))
            self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.commandLinkButton_3.setText("")
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.commandLinkButton_3.setIcon(icon3)

            self.commandLinkButton_3.clicked.connect(lambda checked: Ui_Admin_Add_Account.on_click_Logout(Ui_Admin_Add_Account))

            self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
            self.commandLinkButton_3.setObjectName("commandLinkButton_3")

            MainWindow.setCentralWidget(self.centralwidget)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "Add Account"))
            self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "User Name"))
            self.label_6.setText(_translate("MainWindow", " Username:"))

            self.pushButton.setText(_translate("MainWindow", "Register"))
            self.label_4.setText(_translate("MainWindow", "Email:"))
            self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "xxx@yyy.zzz"))
            self.label_5.setText(_translate("MainWindow", "Password:"))
            self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "At least 8 characters"))
            self.commandLinkButton.setText(_translate("MainWindow", " "))
            self.label_3.setText(_translate("MainWindow", "Confirm Password:"))
            self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Must be compatible"))
            self.label_9.setText(_translate("MainWindow", "Logout"))

########################################################################################################################
########################################Admin_edit######################################################################
########################################################################################################################


class Ui_Admin_Edit_Account(object):

    def on_click_Logout(self):
        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Admin_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()


    def on_click_Enter(self,text1,text2):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        A = text1
        B=str(text2)
        c.execute("select * from " + B +"_users")
        rows = c.fetchall()
        k=1
        for i in range(len(rows)):
            if (A == str(rows[i][0])):
                self.pushButton.setEnabled(True)
                self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgb(32, 53, 82);\n"
                                              "border-radius: 12px;\n"
                                              "box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
                                              "box-shadow: 0 5px #666;\n"
                                              "transform: translateY(4px) ;\n"
                                              "")
                k=0
        if(k==1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("this username does not correspond to any account")
            msg.setWindowTitle("Edit Account")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()
        conn.commit()
        conn.close()

    def on_click_edit(self,text1,text2,text3,entreprise):
        try :
            account.Account.Edit_Account(text1, text2,text3,entreprise)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setFixedSize(500, 500)
            msg.setText("Updated successfully")
            msg.setWindowTitle("Edit Accout")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500, 500)
            msg.setText("Can not edit this account ")
            msg.setWindowTitle("Edit Account")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()



    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/signup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda checked: self.on_click_edit(self.lineEdit_16.text(), self.lineEdit_4.text(), self.lineEdit_3.text(),str(entreprise)))
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(600, 150, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(168, 175, 208);\n"
                                      "border-radius: 12px;\n"
                                      "box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
                                      "box-shadow: 0 5px #666;\n"
                                      "transform: translateY(4px) ;\n"
                                      "")
        self.pushButton.setInputMethodHints(QtCore.Qt.ImhNone)
        icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap("unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 100, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 100, 300, 41))
        self.lineEdit_3.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 140, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 150, 300, 41))
        self.lineEdit_4.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 41, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon2)
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.clicked.connect(lambda checked: Ui_Admin_Edit_Account.on_click_Back(Ui_Admin_Edit_Account, entreprise))

        self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #self.commandLinkButton.clicked.connect(Ui_Signup.on_click_Signin)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 200, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 200, 300, 41))
        self.lineEdit_5.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label.raise_()
        self.layoutWidget.raise_()

        self.pushButton.raise_()
        self.label_4.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.lineEdit_4.raise_()
        self.commandLinkButton.raise_()
        self.label_3.raise_()
        self.lineEdit_5.raise_()

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(200, 37, 250, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_16.setObjectName("label_16")

        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setGeometry(QtCore.QRect(450, 30, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setTabletTracking(False)
        self.lineEdit_16.setAutoFillBackground(False)
        self.lineEdit_16.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
                                      "border-radius: 7px;\n"
                                      "padding: 5px 5px;\n"
                                      "")
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")

        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setEnabled(True)
        self.pushButton_16.setGeometry(QtCore.QRect(560, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"
                                        "border-radius: 12px;\n"
                                        "box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);\n"
                                        "box-shadow: 0 5px #666;\n"
                                        "transform: translateY(4px) ;\n"
                                        "")
        self.pushButton_16.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_16.clicked.connect(lambda checked: self.on_click_Enter(self.lineEdit_16.text(),entreprise))
        self.pushButton_16.setCheckable(False)
        self.pushButton_16.setChecked(False)
        self.pushButton_16.setAutoRepeat(False)
        self.pushButton_16.setAutoExclusive(False)
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(860, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_9.setObjectName("label_9")

        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(855, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon3)

        self.commandLinkButton_3.clicked.connect(Ui_Welcome.on_click_Logout)

        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edit Account"))

        self.pushButton.setText(_translate("MainWindow", "Edit"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "xxx@yyy.zzz"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "At least 8 characters"))
        self.commandLinkButton.setText(_translate("MainWindow", " "))
        self.label_3.setText(_translate("MainWindow", "Confirm Password"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Must be compatible"))
        self.label_16.setText(_translate("MainWindow", "ENTER USERNAME OF ACCOUNT TO EDIT"))
        self.lineEdit_16.setPlaceholderText(_translate("MainWindow", "username"))
        self.pushButton_16.setText(_translate("MainWindow", "ENTER"))
        self.label_9.setText(_translate("MainWindow", "Logout"))

########################################################################################################################
########################################Admin_delete####################################################################
########################################################################################################################
class Ui_Admin_Delete(object):

    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Admin_Manage()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()


    def on_click_delete(self,text1,entreprise):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        A = str(text1)
        B = str(entreprise)
        c.execute("""select * from """+entreprise+"_users where username= '" + A+"'")
        rows = c.fetchall()
        if (rows.__len__()==0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setFixedSize(500,500)
            msg.setText("Enter a valid username ")
            msg.setWindowTitle("Delete Account")
            msg.setStandardButtons(QMessageBox.Ok )
            msg.exec_()
            msg.show()
        else :
            try :
                account.Account.Delete_Account(text1,entreprise)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setFixedSize(500,500)
                msg.setText("Deleted successfully" )
                msg.setWindowTitle("Delete Account")
                msg.setStandardButtons(QMessageBox.Ok )
                msg.exec_()
                msg.show()
            except :
                #print("exception")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setFixedSize(500,500)
                msg.setText("Can not delete this account ")
                msg.setWindowTitle("Delete Account")
                msg.setStandardButtons(QMessageBox.Ok )
                msg.exec_()
                msg.show()



    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.commandLinkButton_3.clicked.connect(Ui_Delete.on_click_Logout)

        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_Admin_Delete.on_click_Back(Ui_Admin_Delete,entreprise))

        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(55, 150, 480, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_16.setObjectName("label_16")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(530, 140, 100, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setTabletTracking(False)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("border: 1.5px solid  rgb(9, 26, 52); \n"
"border-radius: 7px;\n"
"padding: 5px 5px;\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(645, 140, 101, 41))
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
        icon3 = QtGui.QIcon()
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.clicked.connect(lambda checked: self.on_click_delete((self.lineEdit_5.text()), str(entreprise)))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Delete Account"))
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.label_16.setText(_translate("MainWindow", "ENTER USERNAME OF ACCOUNT TO DELETE"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Username"))
        self.pushButton_2.setText(_translate("MainWindow", "Delete"))

########################################################################################################################
############################################Admin_showALL###############################################################
########################################################################################################################

class Ui_Admin_Showall(object):

    def on_click_Logout(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Admin_Welcome()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_show(self, entreprise):

        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()

        A = c.execute("""select * from """ + str(entreprise)+"_users")

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(A):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.commit()
        conn.close()

    def setupUi(self, MainWindow,entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/showall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-190, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/plan.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 470, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")

        self.commandLinkButton_3.clicked.connect(lambda checked : Ui_Admin_Delete.on_click_Logout(Ui_Admin_Delete))

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, -70, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 500, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))

        self.commandLinkButton_6.clicked.connect(lambda checked : Ui_Admin_Delete.on_click_Back(Ui_Admin_Delete,entreprise))

        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 500, 101, 41))
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
        icon3 = QtGui.QIcon()
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(265, 20, 355, 461))
        self.tableWidget.setStyleSheet("Back-ground color : rgb(228, 228, 228)")
        self.tableWidget.setLineWidth(27)
        self.tableWidget.setMidLineWidth(27)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)


        self.pushButton_2.clicked.connect(lambda checked: Ui_Admin_Showall.on_click_show(self,entreprise))

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, -180, 821, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 510, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show all Accounts"))
        self.pushButton_2.setText(_translate("MainWindow", "Show all"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "UserName"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Log out"))

########################################################################################################################
#########################################statistics#####################################################################
########################################################################################################################
########################################################################################################################
#########################################statistics#####################################################################
########################################################################################################################


class Ui_Statistics(object):
    def on_click_Logout(self):
        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()

    def on_click_Back(self,entreprise):
        ui = Ui_Welcome()
        ui.setupUi(MainWindow,entreprise)
        MainWindow.show()

    def on_click_Age(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.Age, data.Attrition).plot(kind='bar', fontsize=5)
        plt.title('Attrition with Age')
        plt.xlabel('Age')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Age')
        plt.show()

    def on_click_yearsSinceLastPromotion(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.YearsSinceLastPromotion, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Years Since Last Promotion')
        plt.xlabel('Job Level')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Years Since Last Promotion')
        plt.savefig('Attrition with Years Since Last Promotion')
        plt.show()


    def on_click_JobLevel(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.JobLevel, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Job Level')
        plt.xlabel('Job Level')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Job Level')
        plt.show()


    def on_click_BusinessTravel(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.BusinessTravel, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Business Travel')
        plt.xlabel('Business Travel')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Business Travel')
        plt.show()

    def on_click_MeritalStatus(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.MaritalStatus, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Marital Status')
        plt.xlabel('Marital Status')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Marital Status')
        plt.show()


    def on_click_Gender(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.Gender, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Gender')
        plt.xlabel('Gender')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Gender')
        plt.show()

    def on_click_TotalWorkingYears(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.TotalWorkingYears, data.Attrition).plot(kind='bar', fontsize=8)
        plt.title('Attrition with Total Working Years')
        plt.xlabel('Total Working Years')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Total Working Years')
        plt.show()


    def on_click_yearsAtCompany(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.YearsAtCompany, data.Attrition).plot(kind='bar', fontsize=8)
        plt.title('Attrition with Years At Company')
        plt.xlabel('Years At Company')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Years At Company')
        plt.show()


    def on_click_OverTime(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.OverTime, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Over Time')
        plt.xlabel('Over Time')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Over Time')
        plt.show()


    def on_click_DistanceFromHome(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.DistanceFromHome, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Distance From Home')
        plt.xlabel('Distance From Home')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Distance From Home')
        plt.show()


    def on_click_Motorized(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.Motorized, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Motorized')
        plt.xlabel('Motorized')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Motorized')
        plt.show()


    def on_click_NumCompaniesWorked(self):
        data = pd.read_csv('IBM.csv')
        pd.crosstab(data.NumCompaniesWorked, data.Attrition).plot(kind='bar', fontsize=10)
        plt.title('Attrition with Number Companies Worked')
        plt.xlabel('Number Companies Worked')
        plt.xticks(rotation=360)
        plt.ylabel('Frequency of Attrition')
        plt.savefig('Attrition with Number Companies Worked')
        plt.show()


    def setupUi(self, MainWindow, entreprise):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 570)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/statistic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-180, 0, 1200, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setWhatsThis("")
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 500, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(840, 460, 61, 61))
        self.commandLinkButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon1)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(10, 0, 41, 51))
        self.commandLinkButton_6.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(48, 36, 637, 229))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(32, 53, 82);\n"

                                      "")
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"

                                        "")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 2, 1, 1)
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"

                                        "")
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"

                                        "")
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 3, 1, 1)
        self.pushButton_10.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(32, 53, 82);\n"

                                         "")
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"

                                        "")
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"

                                        "")
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 0, 1, 1)
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"

                                        "")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 3, 1, 1)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"

                                        "")
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 3, 1, 1, 1)
        self.pushButton_12.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(32, 53, 82);\n"

                                         "")
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 3, 3, 1, 1)
        self.pushButton_11.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "background-color: rgb(32, 53, 82);\n"

                                         "")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)

        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 2, 1, 1)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(32, 53, 82);\n"

                                        )

        self.pushButton.clicked.connect(lambda checked: self.on_click_Age())
        self.pushButton_2.clicked.connect(lambda checked: self.on_click_Gender())
        self.pushButton_5.clicked.connect(lambda checked: self.on_click_MeritalStatus())
        self.pushButton_7.clicked.connect(lambda checked: self.on_click_TotalWorkingYears())
        self.pushButton_10.clicked.connect(lambda checked: self.on_click_JobLevel())
        self.pushButton_6.clicked.connect(lambda checked: self.on_click_yearsAtCompany())
        self.pushButton_9.clicked.connect(lambda checked: self.on_click_NumCompaniesWorked())
        self.pushButton_3.clicked.connect(lambda checked: self.on_click_yearsAtCompany())
        self.pushButton_12.clicked.connect(lambda checked: self.on_click_DistanceFromHome())
        self.pushButton_11.clicked.connect(lambda checked: self.on_click_BusinessTravel())
        self.pushButton_4.clicked.connect(lambda checked: self.on_click_Motorized())
        self.pushButton_8.clicked.connect(lambda checked: self.on_click_OverTime())
        self.commandLinkButton_3.clicked.connect(lambda checked: Ui_Statistics.on_click_Logout(self))
        self.commandLinkButton_6.clicked.connect(lambda checked: Ui_Statistics.on_click_Back(self,entreprise))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 937, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Show statistics"))
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.label_2.setText(_translate("MainWindow", "Statistics referenced to :"))
        self.pushButton.setText(_translate("MainWindow", "Age"))
        self.pushButton_2.setText(_translate("MainWindow", "Sexe"))
        self.pushButton_7.setText(_translate("MainWindow", "Total Years Working"))
        self.pushButton_5.setText(_translate("MainWindow", "Status"))
        self.pushButton_10.setText(_translate("MainWindow", "Job Level"))
        self.pushButton_6.setText(_translate("MainWindow", "Years at company"))
        self.pushButton_9.setText(_translate("MainWindow", "Num Companies Worked"))
        self.pushButton_8.setText(_translate("MainWindow", "Over Time"))
        self.pushButton_3.setText(_translate("MainWindow", "Years at company"))
        self.pushButton_12.setText(_translate("MainWindow", "Distance From Home"))
        self.pushButton_11.setText(_translate("MainWindow", "Business Travel"))
        self.pushButton_4.setText(_translate("MainWindow", "Motorized"))



if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Signin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

