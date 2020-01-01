# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomePage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import welcomepage

from PyQt5.QtWidgets import QApplication,QMainWindow

class Ui_WelcomePage(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        mainWindow.setFont(font)
        mainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 90, 431, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setCursorPosition(12)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 460, 165, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 340, 350, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.pushButton.clicked.connect(mainWindow.hide)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "欢迎界面"))
        self.lineEdit_2.setText(_translate("mainWindow", "欢迎来到藏香指标评估系统"))
        self.pushButton.setText(_translate("mainWindow", "新建指标体系"))
        self.label.setText(_translate("mainWindow", "请输入指标体系名称："))





if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcomePage = QMainWindow()
    #ui = welcomepage.Ui_WelcomePage()
    #向主窗口上添加控件
    ui.setupUi(welcomePage)
    welcomePage.show()
    sys.exit(app.exec_())
