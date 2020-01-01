# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FuncationInterface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FuncationForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.treeWidget = QtWidgets.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(30, 40, 521, 421))
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setFamily(".AppleSystemFallback")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.treeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(614, 403, 111, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(610, 50, 112, 100))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.addBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout_2.addWidget(self.addBtn)
        self.updateBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.updateBtn.setObjectName("updateBtn")
        self.verticalLayout_2.addWidget(self.updateBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.deleteBtn.setObjectName("deleteBtn")
        self.verticalLayout_2.addWidget(self.deleteBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)
        # 添加节点

    def addNode(self):
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0, '新节点')
        node.setText(1, '新值')

    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        item.setText(0, '修改节点')
        item.setText(1, '值已经被修改')

    def deleteNode(self):
        print('删除节点')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "指标"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "标准实施保障"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Form", "标准发布"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("Form", "推广形式"))
        self.treeWidget.topLevelItem(0).child(0).child(1).setText(0, _translate("Form", "标准获取时间"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Form", "标准宣惯"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("Form", "标准问题反馈"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("Form", "政策引导"))
        self.treeWidget.topLevelItem(0).child(4).setText(0, _translate("Form", "标准质量"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("Form", "标准实施过程"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("Form", "生产制造企业"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("Form", "检测机构"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("Form", "销售企业"))
        self.treeWidget.topLevelItem(1).child(3).setText(0, _translate("Form", "消费者"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("Form", "标准实施效果"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("Form", "质量状况"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("Form", "社会效益"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("Form", "经济效益"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.setText(_translate("Form", "计算权重"))
        self.pushButton.setText(_translate("Form", "专家评价"))
        self.pushButton_2.setText(_translate("Form", "计算结果"))
        self.pushButton_3.setText(_translate("Form", "返回"))
        self.addBtn.setText(_translate("Form", "添加节点"))
        self.updateBtn.setText(_translate("Form", "修改节点"))
        self.deleteBtn.setText(_translate("Form", "删除节点"))

import sys
import FuncationInterface

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    function = QWidget()
    ui = FuncationInterface.Ui_FuncationForm()
    #向主窗口上添加控件
    ui.setupUi(function)
    function.show()
    sys.exit(app.exec_())


