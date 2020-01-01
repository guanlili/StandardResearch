from PyQt5.Qt import *

import sys

app = QApplication(sys.argv)




window =QWidget()
window.setWindowTitle("社会我礼哥")
window.resize(500,500)
window.move(400,200)

label = QLabel(window)
label.setText("hello")
label.move(200,200)




window.show()

sys.exit(app.exec())


#0 导入需要的包和模块
#我们的代码到时候的执行方式，右击，执行  命令行python代码名称
