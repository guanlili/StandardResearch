import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QColorDialog, QFontDialog, QPushButton, \
                            QHBoxLayout, QVBoxLayout
#这两种对话框分别可以让用户进行颜色和字体选择。两者用法相似，所以就放在一起讲了：



class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.text_edit = QTextEdit(self)                 # 1

        self.color_btn = QPushButton('Color', self)      # 2
        self.font_btn = QPushButton('Font', self)
        self.color_btn.clicked.connect(lambda: self.open_dialog_func(self.color_btn))
        self.font_btn.clicked.connect(lambda: self.open_dialog_func(self.font_btn))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.color_btn)
        self.h_layout.addWidget(self.font_btn)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.text_edit)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def open_dialog_func(self, btn):
        if btn == self.color_btn:                        # 3
            color = QColorDialog.getColor()
            if color.isValid():
                self.text_edit.setTextColor(color)
        else:                                            # 4
            font, ok = QFontDialog.getFont()
            if ok:
                self.text_edit.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
'''1. QTextEdit控件用于显示文本颜色和字体变化；

    2. 实例化两个按钮分别用于打开颜色对话框和字体对话框，然后进行信号和槽的连接；

    3. 如果是color_btn被按下的话，则调用QColorDialog的getColor()方法显示颜色对话框，
    当选择一种颜色后其十六进制的值会保存在color变量中，但如果点击对话框中的取消(Cancel)按钮的话，则color为无效值。
    通过isValid()方法判断color是否有效，若有效的话则通过setTextColor()方法设置QTextEdit的文本颜色；

    4. 如果是font_btn被按下的话，则调用QFontDialog的getFont()方法显示字体对话框，该方法返回两个值，
    分别为QFont和bool值，如果用户选择了一种字体并按下确定(Ok)的话，则font保存所选择的QFont值，
    并且ok为True。若按下取消(Cancel)的话，则bool为False。当ok为True时，调用setFont()方法设置QTextEdit的文本字体。
'''