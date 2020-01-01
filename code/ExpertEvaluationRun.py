import sys
import ExpertEvaluation

from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    expertEvaluationForm = QWidget()
    ui = ExpertEvaluation.Ui_ExpertEvaluationForm()
    #向主窗口上添加控件
    ui.setupUi(expertEvaluationForm)
    expertEvaluationForm.show()
    sys.exit(app.exec_())


