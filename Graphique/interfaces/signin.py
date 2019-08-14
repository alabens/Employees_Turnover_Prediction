# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from UI.signup import Ui_Signup
from UI.welcome import Ui_Welcome
from UI.manage_employee import Ui_Manage
from UI.signin_error import Ui_SigninError
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Signin(object):
    def on_click_Signup(self):

        ui = Ui_Signup()
        ui.setupUi(MainWindow)
        MainWindow.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ic_real_name_authentication_527859.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 109, 411, 41))
        self.lineEdit_2.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 79, 151, 109))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 50, 411, 41))
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(460, 180, 121, 41))
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
        self.pushButton.clicked.connect(self.on_click_Login)
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.clicked.connect(self.on_click_Signup)
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 160, 121, 16))
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
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "********"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your Company Name"))
        self.label_2.setText(_translate("MainWindow", "Company Name:"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.commandLinkButton.setText(_translate("MainWindow", "Don\'t have an account ? Register from here"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p><a href=\"www.gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">send mail</span></a></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Forgot your password ? "))
##################################################
    def on_click_Login(self):
        conn = sqlite3.connect('PCD.db')
        c = conn.cursor()
        # c.execute("""insert into Entreprise values ('sofrecom','sofrecom','sof.kharrat@ensi-uma.tn')""")
        c.execute("""select * from Entreprise""")
        rows = c.fetchall()
        A = self.lineEdit.text()
        B = self.lineEdit_2.text()
        #print(A)
        #print(B)
        k=1
        for i in range(len(rows)):
            if (A == rows[i][0]) and (B == rows[i][1]):
                #print("nkl")
                ui = Ui_Welcome()
                ui.setupUi(MainWindow)
                MainWindow.show()
                k=0
        if(k==1):
            ui = Ui_SigninError()
            ui.setupUi(MainWindow)
            MainWindow.show()
        c.execute("drop table ALA")
        c.execute("delete from entreprise where NomEnt='ALA'")



        conn.commit()
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Signin()
    ui.setupUi(MainWindow)
    #ui.action(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

