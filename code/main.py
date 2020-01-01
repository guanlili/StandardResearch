from WelcomePage import Ui_WelcomePage
from FuncationInterface import Ui_FuncationForm
from CalcuateWeight import Ui_CalcuateWeightForm
from ExpertEvaluation import Ui_ExpertEvaluationForm
from JudgmentMatrix import Ui_JudgmentMatrixForm


from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QWidget
import sys

class WelcomePage(QMainWindow):#欢迎界面
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_WelcomePage()
        self.main_ui.setupUi(self)


class FuncationInterface(QWidget):#功能界面
    def __init__(self):
        super(FuncationInterface,self).__init__()
        self.calendars = Ui_FuncationForm()
        self.calendars.setupUi(self)


class CalcuateWeight(QWidget):#计算权重，专家1-11
    def __init__(self):
        super(CalcuateWeight,self).__init__()
        self.calendars = Ui_CalcuateWeightForm()
        self.calendars.setupUi(self)

class JudgmentMatrix(QWidget):#点击专家进入判断矩阵界面
    def __init__(self):
        super(JudgmentMatrix,self).__init__()
        self.calendars = Ui_JudgmentMatrixForm()
        self.calendars.setupUi(self)


class ExpertAmount(QWidget):#专家数量
    def __init__(self):
        super(ExpertAmount,self).__init__()
        self.calendars = Ui_ExpertAmountForm()
        self.calendars.setupUi(self)

class ExpertEvaluation(QWidget):#专家评价fuzzy
    def __init__(self):
        super(ExpertEvaluation,self).__init__()
        self.calendars = Ui_ExpertEvaluationForm()
        self.calendars.setupUi(self)


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = WelcomePage()
    funcationInterface = FuncationInterface()
    calcuateWeight = CalcuateWeight()
    expertEvaluation = ExpertEvaluation()
    judgmentMatrix = JudgmentMatrix()

    #通过按钮将两个窗体关联
    btn = window.main_ui.pushButton
    btn.clicked.connect(funcationInterface.show)#把主窗口的pushButton新建指标体系 连接到funcationInterface

    btn = funcationInterface.calendars.pushButton_4#把功能界面的pushButton_4计算权重连接到calcuateWeight
    btn.clicked.connect(calcuateWeight.show)

    btn = calcuateWeight.calendars.pushButton_4#把计算权重的pushButton专家1连接到expertAmount专家数量
    btn.clicked.connect(judgmentMatrix.show)

    btn = funcationInterface.calendars.pushButton  # 把功能界面的pushButton专家评价连接到expertEvaluation
    btn.clicked.connect(expertEvaluation.show)

    btn = funcationInterface.calendars.pushButton  # 把功能界面的pushButton专家评价连接到expertEvaluation
    btn.clicked.connect(expertEvaluation.show)



    #显示
    window.show()
    sys.exit(app.exec_())
