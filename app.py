import sys
from PyQt4 import QtGui
from new2 import Ui_MainWindow

class App(QtGui.QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
