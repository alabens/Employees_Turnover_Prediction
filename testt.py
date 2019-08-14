import sys
from PyQt5.QtWidgets import *

class Window (QWidget):

    def __init__(self):
       super().__init__()
       self.setWindowTitle("Buttons")
       self.setGeometry(50,50,500,500)
       self.UI()

    def UI(self):

        self.text=QLabel("this is a text ",self)
        self.text.move(100,100)
        self.enterButton=QPushButton("Enter",self)
        self.enterButton.move(100,150)
        self.enterButton.clicked.connect(self.enter)
        self.exitButton=QPushButton("Exit",self)
        self.exitButton.move(200, 150)
        self.exitButton.clicked.connect(self.exit)
        self.show()
    def enter (self ):
        self.text.setText("you clicked the enter button")

    def exit(self):
        self.text.setText("you clicked the exit button")
        self.text.resize(150,20)
def main():
    App=QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())
main()