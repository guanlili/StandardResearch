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


