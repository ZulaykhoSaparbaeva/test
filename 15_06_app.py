from PyQt5.QtWidgets import QMainWindow, QApplication
from calc import *
import sys

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        #Load the ui
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_0.clicked.connect(self.btn0_clicked)
        self.ui.btn_1.clicked.connect(self.btn1_clicked)
        self.ui.btn_2.clicked.connect(self.btn2_clicked)
        self.ui.btn_3.clicked.connect(self.btn3_clicked)
        self.ui.btn_4.clicked.connect(self.btn4_clicked)
        self.ui.btn_5.clicked.connect(self.btn5_clicked)
        self.ui.btn_6.clicked.connect(self.btn6_clicked)
        self.ui.btn_7.clicked.connect(self.btn7_clicked)
        self.ui.btn_8.clicked.connect(self.btn8_clicked)
        self.ui.btn_9.clicked.connect(self.btn9_clicked)

        self.ui.btn_pls.clicked.connect(self.btn_add_clicked)
        self.ui.btn_min.clicked.connect(self.btn_min_clicked)
        self.ui.btn_mul.clicked.connect(self.btn_mul_clicked)
        self.ui.btn_div.clicked.connect(self.btn_div_clicked)
        self.ui.btn_per.clicked.connect(self.btn_per_clicked)
        self.ui.btn_AC.clicked.connect(self.btn_ac_clicked)
        self.ui.btn_abc.clicked.connect(self.btn_abc_clicked)
        self.ui.btn_c.clicked.connect(self.btn_c_clicked)

        self.ui.btn_equ.clicked.connect(self.btn_eq_clicked)


    @staticmethod
    def set_number(self, num):
        if self.ui.labelResult.text()=="0":
            self.ui.labelResult.setText(num)
        else:
            self.ui.labelResult.setText(self.ui.labelResult.text()+num)

    def btn0_clicked(self):
        self.set_number(self, "0")
    def btn1_clicked(self):
        self.set_number(self, "1")
    def btn2_clicked(self):
        self.set_number(self, "2")
    def btn3_clicked(self):
        self.set_number(self, "3")
    def btn4_clicked(self):
        self.set_number(self, "4")
    def btn5_clicked(self):
        self.set_number(self, "5")
    def btn6_clicked(self):
        self.set_number(self, "6")
    def btn7_clicked(self):
        self.set_number(self, "7")
    def btn8_clicked(self):
        self.set_number(self, "8")
    def btn9_clicked(self):
        self.set_number(self, "9")
    def btn_add_clicked(self):
        self.set_number(self, "+")
    def btn_min_clicked(self):
        self.set_number(self, "-")
    def btn_mul_clicked(self):
        self.set_number(self, "*")
    def btn_div_clicked(self):
        self.set_number(self, "/")
    def btn_per_clicked(self):
        x=float(self.ui.labelResult.text())/100
        self.ui.labelResult.clear()
        self.set_number(self, str(x))
    def btn_ac_clicked(self):
        self.ui.labelResult.clear()
    def btn_abc_clicked(self):
        x =(-1)* float(self.ui.labelResult.text())
        self.ui.labelResult.clear()
        self.set_number(self, str(x))
    def btn_c_clicked(self):
        if self.ui.labelResult.text() != "0":
            x=self.ui.labelResult.text()
            x=x[:-1:]
            self.ui.labelResult.clear()
            self.set_number(self, x)


    def btn_eq_clicked(self):
        self.ui.labelResult.setText(str(eval(self.ui.labelResult.text())))


def main():
    app=QApplication(sys.argv)
    window=Window()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()