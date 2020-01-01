import sys
import CalcuateWeight

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calcuateWeight = QWidget()
    ui = CalcuateWeight.Ui_CalcuateWeightForm()
    #向主窗口上添加控件
    ui.setupUi(calcuateWeight)
    calcuateWeight.show()
    sys.exit(app.exec_())