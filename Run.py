from UI.Main3 import Ui_MainWindow
from UI import Main3
from PyQt4 import QtCore, QtGui  # @UnusedImport
import sys
class run():
    def start(self):
     self.ex=Ui_MainWindow()
     self.ex.show()



if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    r=run()
    r.start()
    sys.exit(app.exec_())
