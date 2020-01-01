import sys
import WelcomePage

from PyQt5.QtWidgets import QApplication,QMainWindow



if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcomePage = QMainWindow()
    ui = WelcomePage.Ui_WelcomePage()
    #向主窗口上添加控件
    ui.setupUi(welcomePage)
    welcomePage.show()
    sys.exit(app.exec_())
