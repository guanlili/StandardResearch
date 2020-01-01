import sys
import NewIndexSystemDoalog
from ExpertAmount import Ui_ExpertAmountForm

from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QWidget

class Ui_ExpertAmountForm(QWidget):#专家数量
    def __init__(self):
        super(Ui_ExpertAmountForm,self).__init__()
        self.calendars = Ui_ExpertAmountForm()
        self.calendars.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = QDialog()
    expertAmount = Ui_ExpertAmountForm()

    btn = expertAmount.calendars.buttonBox.accepted  # 把功能界面的pushButton专家评价连接到expertEvaluation
    btn.clicked.connect(expertAmount.show)
    ui = NewIndexSystemDoalog.Ui_FuncationForm()
    #向主窗口上添加控件
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())