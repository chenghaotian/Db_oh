from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import center


class Stats(object):

    def __init__(self):
        self.ui = QUiLoader().load('untitled.ui')
        self.ui.plainTextEdit.document().setMaximumBlockCount(100)
        self.ui.pushButton.clicked.connect(self.main_go)
        self.tw = "0"
        self.et = "0"
        self.tn = "0"
        self.st = "0"

    def main_go(self):
        text = self.ui.lineEdit.text()
        type_dict = {
            "二": 0,
            "八": 1,
            "十": 2,
            "十六": 3
        }
        list_re = center.main(text, type_dict[self.ui.buttonGroup.checkedButton().text()])

        if list_re[4]:
            self.tw = list_re[0]
            self.et = list_re[1]
            self.tn = list_re[2]
            self.st = list_re[3]
            self.ui.plainTextEdit.appendPlainText(
                f"-----------------------\n"
                f"[输出]: 二进制: {self.tw}\n"
                f"[输出]: 八进制: {self.et}\n"
                f"[输出]: 十进制: {self.tn}\n"
                f"[输出]: 十六进制: {self.st}"
            )
        else:
            self.ui.plainTextEdit.appendPlainText("[错误]: 请检查输入内容")


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
