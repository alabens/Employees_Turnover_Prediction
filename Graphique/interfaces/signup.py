# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from UI.signin import Ui_Signin
from UI.welcome import Ui_Welcome
import sqlite3
from UI.signup_error import Ui_SignupError
from logique.EntrepriseDAO import Entreprise

class Ui_Signup(object):

    def on_click_Signin(self):

        ui = Ui_Signin()
        ui.setupUi(MainWindow)
        MainWindow.show()


    def on_click_Register(self):
        conn = sqlite3.connect('PCD.db')
        c = conn.cursor()
        c.execute("""select * from Entreprise""")
        rows = c.fetchall()
        #print(rows)
        A = self.lineEdit.text()
        B = self.lineEdit_4.text()
        C = self.lineEdit_3.text()
        D = self.lineEdit_5.text()
        k = 1
        for i in range(len(rows)):
            if ((A == rows[i][0]) or (B != D) or (A == "") or (B == "") or (C == "") or (D == "") or (C == rows[i][2])):
                k=0
        if (k == 0):
            ui = Ui_SignupError()
            ui.setupUi(MainWindow)
            MainWindow.show()
        else:
            c.execute("""insert into Entreprise (NomEnt,PwdEnt,MailEnt) values (?,?,?)""", (A, B, C))
            c.execute("""CREATE TABLE """ + A + """(
                                   Id integer primary key AUTOINCREMENT,
                                   Firt_Name text NOT NULL,
                                   Last_Name text NOT NULL,
                                   Sexe text NOT NULL,
                                   BirthDay date NOT NULL,
                                   Status text NOT NULL,
                                   occupation text NOT NULL,
                                   Departement text NOT NULL,
                                   years_of_employement text NOT NULL,
                                   Type_of_contract text NOT NULL,
                                   Years_Experience text NOT NULL,
                                   Over_Time text NOT NULL,
                                   Distance_from_home text NOT NULL,
                                   Motoriezed text NOT NULL,
                                   salary text NOT NULL)""")
            ui = Ui_Welcome()
            ui.setupUi(MainWindow)
            MainWindow.show()

            #c.execute("SELECT name FROM sqlite_master WHERE type='table';")
           # print(c.fetchall())

        conn.commit()
        c.close()
        conn.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("signup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label.setPixmap(QtGui.QPixmap("turnover1.jpg"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 20, 561, 41))
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.on_click_Register)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(440, 230, 121, 41))
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
        icon1.addPixmap(QtGui.QPixmap("unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 70, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 70, 561, 41))
        self.lineEdit_3.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 110, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 120, 561, 41))
        self.lineEdit_4.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 41, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon2)
        self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton.clicked.connect(Ui_Signup.on_click_Signin)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(220, 170, 561, 41))
        self.lineEdit_5.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label.raise_()
        self.layoutWidget.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_4.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.lineEdit_4.raise_()
        self.commandLinkButton.raise_()
        self.label_3.raise_()
        self.lineEdit_5.raise_()
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Sign up"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Company Name"))
        self.label_2.setText(_translate("MainWindow", "Company Name"))
        self.pushButton.setText(_translate("MainWindow", "Register"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "xxx@yyy.zzz"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "At least 8 characters"))
        self.commandLinkButton.setText(_translate("MainWindow", " "))
        self.label_3.setText(_translate("MainWindow", "Confirm your Password"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Must be compatible"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Signup()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

