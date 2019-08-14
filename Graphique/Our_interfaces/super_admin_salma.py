# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'super_admin_salma.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Admin_Salma(object):
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
        icon.addPixmap(QtGui.QPixmap("back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("../../../Desktop/GRAPHICS/UI/unlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-440, 0, 971, 651))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../plan.jpg"))
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
        icon2.addPixmap(QtGui.QPixmap("../salma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salma.setIcon(icon2)
        self.salma.setIconSize(QtCore.QSize(140, 140))
        self.salma.setObjectName("salma")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.commandLinkButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_6.setText("")
        self.commandLinkButton_6.setIcon(icon)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

