# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys  # @UnusedImport
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTimer
from UI.Modify2 import Ui_ModifyForm
from UI.Watch2 import Ui_Form2
from UI.Watch3 import Ui_Form3
from UI.Search import Ui_Search
from UI.Watch import Ui_Form  # @UnusedImport
from Controller.Controller import control
from Controller import Controller
from Controller.File import File
from UI.Book_View import Ui_Book_Watch
from UI.web import Ui_web
from UI.modify4 import Ui_modify4
try:
    _fromUtf8 = QtCore.QString.fromUtf8  # @UndefinedVariable
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.alpha=255
        self.bk=Ui_Book_Watch()
        self.bx=Ui_modify4(self.bk)
        self.gx=Ui_web()
        self.cx=Ui_Form2()
        self.dx=Ui_Search()
        self.fx=Ui_Form3()

        self.setupUi(self)

        


    def disable(self,item,opt):
        if opt == True:
            item.setStyleSheet(_fromUtf8("color: rgb(177, 177, 177);"))
            item.setDisabled(True)
        else:
            item.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
            item.setEnabled(True)

    def web(self):
        Controller.control.opened['gx']=1
        self.gx.show()
    def watch(self):
        Controller.control.opened['cx']=1
        
        self.cx.show()

    def new(self):
        control.rCarte.cr=[]
        control.rClient.cl=[]
        control.rImprumut.im=[]
        self.bk.update_watch(self.bk.listView)
    def save(self):
        self.fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save',filter='*.be')
        self.f=File()
        self.f.save(self.fileName)
    def open(self):
        self.fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open',filter='*.be')
        self.f=File()
        self.f.open(self.fileName)
        self.bk.update_watch(self.bk.listView)

    def show_Modify(self):
        Controller.control.opened['bx']=1
        
        self.bx.show()

    def show_Search(self):
        Controller.control.opened['dx']=1
        
        self.dx.show()
        
    def show_stat(self):
        Controller.control.opened['fx']=1
        
        self.fx.listWidget.clear()
        self.fx.show()
    def show_Book_View(self):
        Controller.control.opened['bk']=1
        self.bk.update_watch(self.bk.listView)

        self.bk.show()
               
    def closeEvent(self,QCloseEvent):
        if Controller.control.opened['bx']==1:
            self.bx.close()
        if Controller.control.opened['dx']==1:
            self.dx.close()
        if Controller.control.opened['fx']==1:
            self.fx.close()
        if Controller.control.opened['cx']==1:
            self.cx.close()
        if Controller.control.opened['gx']==1:
            self.gx.close()
        if Controller.control.opened['bk']==1:
            self.bk.close()
        if Controller.control.opened['window']==1:
            self.dx.window.close()
         
        return super().closeEvent(QCloseEvent) 

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(603, 407)
        MainWindow.setFixedSize(603,407)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);\n"
"QMenuBar { background-color:  rgb(58, 58, 58) }\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 140, 511, 21))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.MainLabel = QtGui.QLabel(self.centralwidget)
        self.MainLabel.setGeometry(QtCore.QRect(100, 30, 281, 61))
        self.MainLabel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(45)
        font.setBold(False)
        font.setWeight(50)
        self.MainLabel.setFont(font)
        self.MainLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.MainLabel.setTextFormat(QtCore.Qt.RichText)
        self.MainLabel.setScaledContents(False)
        self.MainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MainLabel.setWordWrap(False)
        self.MainLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)


    

        self.MainLabel.setObjectName(_fromUtf8("MainLabel"))
        self.MainPhoto = QtGui.QLabel(self.centralwidget)
        self.MainPhoto.setGeometry(QtCore.QRect(390, 30, 101, 61))
        self.MainPhoto.setStyleSheet(_fromUtf8(""))
        self.MainPhoto.setText(_fromUtf8(""))
        self.MainPhoto.setPixmap(QtGui.QPixmap(_fromUtf8("f:/book.png")))
        self.MainPhoto.setScaledContents(True)
        self.MainPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.MainPhoto.setObjectName(_fromUtf8("MainPhoto"))
        self.Modify = QtGui.QPushButton(self.centralwidget)
        self.Modify.setGeometry(QtCore.QRect(40, 220, 151, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(24)
        self.Modify.setFont(font)
        self.Modify.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Modify.setIconSize(QtCore.QSize(16, 16))
        self.Modify.setFlat(False)
        self.Modify.setObjectName(_fromUtf8("Modify"))
        self.Modify.clicked.connect(self.show_Modify)
        self.Search = QtGui.QPushButton(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(230, 220, 151, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(24)
        self.Search.setFont(font)
        self.Search.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Search.setIconSize(QtCore.QSize(16, 16))
        self.Search.setFlat(False)
        self.Search.setObjectName(_fromUtf8("Search"))
        self.Search.clicked.connect(self.show_Search)
        self.Statistics = QtGui.QPushButton(self.centralwidget)
        self.Statistics.setGeometry(QtCore.QRect(420, 220, 151, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(24)
        self.Statistics.setFont(font)
        self.Statistics.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.Statistics.setIconSize(QtCore.QSize(16, 16))
        self.Statistics.setFlat(False)
        self.Statistics.setObjectName(_fromUtf8("Statistics"))
        self.Statistics.clicked.connect(self.show_stat)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menubar.setStyleSheet("""

     QMenuBar::item {
         background: rgb(58, 58, 58);
         color: rgb(255, 255, 255);
     }""")

        self.menuFile = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.menuFile.setFont(font)
        self.menuFile.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        
        self.menuWindow = QtGui.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.menuWindow.setFont(font)
        self.menuWindow.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        
        self.actionWatch = QtGui.QAction(MainWindow)
        self.actionWatch.setObjectName(_fromUtf8("actionWatch"))

        self.actionWeb = QtGui.QAction(MainWindow)
        self.actionWeb.setObjectName(_fromUtf8("actionWeb"))

        self.actionViewBook = QtGui.QAction(MainWindow)
        self.actionViewBook.setObjectName(_fromUtf8("actionViewBook"))

        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        
        self.menuWindow.addAction(self.actionWatch)
        self.menuWindow.addAction(self.actionWeb)
        self.menuWindow.addAction(self.actionViewBook)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.Search.setStyleSheet(_fromUtf8("color: rgb(177, 177, 177);"))
        self.Search.setDisabled(True)
        self.Statistics.setStyleSheet(_fromUtf8("color: rgb(177, 177, 177);"))
        self.Statistics.setDisabled(True)

        self.bx.change_button.setStyleSheet(_fromUtf8("color: rgb(177, 177, 177);"))
        self.bx.change_button.setDisabled(True)
        self.bx.delete_button.setStyleSheet(_fromUtf8("color: rgb(177, 177, 177);"))
        self.bx.delete_button.setDisabled(True)



        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL(_fromUtf8("triggered()")), self.save)

        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), self.open)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), lambda:self.disable(self.Search,False))
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), lambda:self.disable(self.Statistics,False))
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), lambda:self.disable(self.bx.change_button,False))
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), lambda:self.disable(self.bx.delete_button,False))



        QtCore.QObject.connect(self.actionNew, QtCore.SIGNAL(_fromUtf8("triggered()")), self.new)
        QtCore.QObject.connect(self.actionWatch, QtCore.SIGNAL(_fromUtf8("triggered()")), self.watch)
        QtCore.QObject.connect(self.actionWeb, QtCore.SIGNAL(_fromUtf8("triggered()")), self.web)
        QtCore.QObject.connect(self.actionViewBook, QtCore.SIGNAL(_fromUtf8("triggered()")), self.show_Book_View)




        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.MainLabel.setText(_translate("MainWindow", "BiblioEdit", None))
        self.Modify.setText(_translate("MainWindow", "Modify", None))
        self.Search.setText(_translate("MainWindow", "Search", None))
        self.Statistics.setText(_translate("MainWindow", "Statistics", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuWindow.setTitle(_translate("MainWindow", "Windows", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionWatch.setText(_translate("MainWindow", "Watch", None))
        self.actionWeb.setText(_translate("MainWindow", "Web", None))
        self.actionViewBook.setText(_translate("MainWindow", "Book Viewer", None))