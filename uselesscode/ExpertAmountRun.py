import sys
import ExpertAmount

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    expertAmountForm = QWidget()
    ui = ExpertAmount.Ui_ExpertAmountForm()
    #向主窗口上添加控件
    ui.setupUi(expertAmountForm)
    expertAmountForm.show()
    sys.exit(app.exec_())


