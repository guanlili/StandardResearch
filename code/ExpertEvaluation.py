# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExpertEvaluation.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExpertEvaluationForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 591, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
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
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(611, 430, 135, 66))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1.1.1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "1.1.2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "1.2.1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "非常不好"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "不好"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "一般"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "非常好"))
        self.pushButton.setText(_translate("Form", "归一化处理"))
        self.pushButton_2.setText(_translate("Form", "返回主界面"))

