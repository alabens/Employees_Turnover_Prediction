# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prediction.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 565)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Desktop/GRAPHICS/UI/ic_real_name_authentication_527859.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.label.setPixmap(QtGui.QPixmap("turnover1.jpg"))
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
        icon1.addPixmap(QtGui.QPixmap("logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap("back_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon2)
        self.commandLinkButton_6.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 131, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("employee.png"))
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
        self.label_12.setGeometry(QtCore.QRect(70, 350, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(460, 230, 101, 21))
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
        self.label_18.setGeometry(QtCore.QRect(250, 420, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(9, 26, 52);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(340, 100, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(340, 130, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(280, 160, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(350, 190, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(180, 230, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(190, 260, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(200, 290, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(270, 320, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(230, 350, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(570, 230, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(570, 260, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(640, 290, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(560, 320, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color:rgb(228, 27, 35);")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(530, 350, 201, 21))
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
        self.label_34.setPixmap(QtGui.QPixmap("arriere.jpg"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(760, 160, 111, 141))
        self.label_35.setText("")
        self.label_35.setPixmap(QtGui.QPixmap("1.jpg"))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(820, 150, 31, 20))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap("1.jpg"))
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
        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(380, 0, 51, 51))
        self.commandLinkButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_7.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("precedent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_7.setIcon(icon3)
        self.commandLinkButton_7.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_7.setObjectName("commandLinkButton_7")
        self.commandLinkButton_8 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_8.setGeometry(QtCore.QRect(480, 0, 51, 51))
        self.commandLinkButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.commandLinkButton_8.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_8.setIcon(icon4)
        self.commandLinkButton_8.setIconSize(QtCore.QSize(40, 40))
        self.commandLinkButton_8.setObjectName("commandLinkButton_8")
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
        self.commandLinkButton_7.raise_()
        self.commandLinkButton_8.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 21))
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
        self.label_5.setText(_translate("MainWindow", "Log out"))
        self.label_3.setText(_translate("MainWindow", "First Name :"))
        self.label_4.setText(_translate("MainWindow", "Last Name :"))
        self.label_6.setText(_translate("MainWindow", "Sex :"))
        self.label_7.setText(_translate("MainWindow", "Date of Birth :"))
        self.label_8.setText(_translate("MainWindow", "Civil Status :"))
        self.label_9.setText(_translate("MainWindow", "Occupation :"))
        self.label_10.setText(_translate("MainWindow", "Departement :"))
        self.label_11.setText(_translate("MainWindow", "Year of Employement :"))
        self.label_12.setText(_translate("MainWindow", "Type of Contract :"))
        self.label_13.setText(_translate("MainWindow", "Experience :"))
        self.label_14.setText(_translate("MainWindow", "Over Time :"))
        self.label_15.setText(_translate("MainWindow", "Distance from Home :"))
        self.label_16.setText(_translate("MainWindow", "Motorized :"))
        self.label_17.setText(_translate("MainWindow", "Salary :"))
        self.label_18.setText(_translate("MainWindow", "ATTRITION :"))
        self.label_19.setText(_translate("MainWindow", "Prénom"))
        self.label_20.setText(_translate("MainWindow", "Nom"))
        self.label_21.setText(_translate("MainWindow", "Sexe"))
        self.label_22.setText(_translate("MainWindow", "Date de naissance"))
        self.label_23.setText(_translate("MainWindow", "Etat civil"))
        self.label_24.setText(_translate("MainWindow", "Occcupation"))
        self.label_25.setText(_translate("MainWindow", "Département"))
        self.label_26.setText(_translate("MainWindow", "Année d\'embauche"))
        self.label_27.setText(_translate("MainWindow", "Type de contrat"))
        self.label_28.setText(_translate("MainWindow", "Expérience"))
        self.label_29.setText(_translate("MainWindow", "Temps supplémentaire"))
        self.label_30.setText(_translate("MainWindow", "Distance"))
        self.label_31.setText(_translate("MainWindow", "Motorisé"))
        self.label_32.setText(_translate("MainWindow", "Salaire"))
        self.label_33.setText(_translate("MainWindow", "Attrition"))
        self.label_37.setText(_translate("MainWindow", "ID :"))
        self.label_38.setText(_translate("MainWindow", "Identifiant"))

import testt_rc
