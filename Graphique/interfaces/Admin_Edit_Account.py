from PyQt5 import QtCore, QtGui, QtWidgets
#from UI.signin import Ui_Signin
from UI.welcome import Ui_Welcome
import sqlite3
from UI.signup_error import Ui_SignupError


class Ui_Admin_Edit_Account(object):

    def on_click_edit(self,text1,text2,text3,text4):
        try :
            conn = sqlite3.connect('Attrition.db')
            c = conn.cursor()
            c.execute("""Update """ + text4 + """_users set password=?,email=?
            where username=? """, (text2,text3,text1))
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
            # msg.setInformativeText("Enter employee id ")
            msg.setWindowTitle("Edit Account")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            msg.show()

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
        self.lineEdit.setGeometry(QtCore.QRect(250, 90, 300, 41))
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 90, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(lambda checked: self.on_click_edit(self.lineEdit_16.text(), self.lineEdit_4.text(), self.lineEdit_3.text(),entreprise))
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(600, 160, 80, 41))
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
        self.label_4.setGeometry(QtCore.QRect(190, 140, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 140, 300, 41))
        self.lineEdit_3.setStyleSheet("border: 2px solid  rgb(9, 26, 52); \n"
"border-radius: 12px;\n"
"padding: 10px 15px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 180, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 190, 300, 41))
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
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.commandLinkButton.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #self.commandLinkButton.clicked.connect(Ui_Signup.on_click_Signin)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 240, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(250, 240, 300, 41))
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

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(190, 37, 250, 20))
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
        #self.pushButton_16.setIcon(icon3)
        self.pushButton_16.setCheckable(False)
        self.pushButton_16.setChecked(False)
        self.pushButton_16.setAutoRepeat(False)
        self.pushButton_16.setAutoExclusive(False)
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_2")

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
        icon3.addPixmap(QtGui.QPixmap("logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon3)

        self.commandLinkButton_3.clicked.connect(Ui_Welcome.on_click_Logout)

        self.commandLinkButton_3.setIconSize(QtCore.QSize(50, 50))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.pushButton_2.clicked.connect(lambda checked: self.on_click_show(entreprise))


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
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Company Name"))
        self.label_2.setText(_translate("MainWindow", "Company Name"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Admin_Edit_Account()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())