from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)