import sys
import JudgmentMatrix

from PyQt5.QtWidgets import QApplication,QWidget



if __name__ == '__main__':
    app = QApplication(sys.argv)
    judgmentMatrix = QWidget()
    ui = JudgmentMatrix.Ui_JudgmentMatrixForm()
    #向主窗口上添加控件
    ui.setupUi(judgmentMatrix)
    judgmentMatrix.show()
    sys.exit(app.exec_())
