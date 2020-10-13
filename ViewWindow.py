import sys
from PyQt5.QtWidgets import QApplication , QWidget, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5 import QtGui 
from Palindrome import isPalindrome

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Max not double substring'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QLineEdit(self)
        self.textbox.move(200, 70)
        self.textbox.resize(280,40)

        self.execButton=QPushButton('Find',self)
        self.execButton.setToolTip('Execute button')
        self.execButton.move(200,120)
        self.execButton.clicked.connect(self.on_click)

        self.outputPosLabel=QLabel(self)
        self.outputPosLabel.move(200,145)
        self.outputPosLabel.resize(200,40)
        self.outputPosLabel.setFont(QtGui.QFont("Times", 14, QtGui.QFont.Bold))
        self.outputPosLabel.setText("Is palindrome: ")

        self.outputLabel=QLabel(self)
        self.outputLabel.move(200,160)
        self.outputLabel.resize(200,40)
        self.outputLabel.setFont(QtGui.QFont("Times", 12))

        self.show()

    def on_click(self):
        if self.textbox.text()=="":
            QMessageBox.question(self,"app message","Empty input error",QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.outputLabel.setText(str(isPalindrome(self.textbox.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
   
