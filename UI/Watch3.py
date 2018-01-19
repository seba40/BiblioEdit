# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Watch2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from Controller.Controller import control
from Controller import Controller
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

class Ui_Form3(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def update_watch(self,item):
        item.clear()
        item.addItem("Books : ")
        for i in range(0,len(control.rCarte.cr)):
            item.addItem("  "+str(control.rCarte.cr[i]))
        item.addItem("Clients : ")
        for i in range(0,len(control.rClient.cl)):
            item.addItem("  "+str(control.rClient.cl[i]))
        item.addItem("Entries : ")
        for i in range(0,len(control.rImprumut.im)):
            item.addItem("  "+str(control.rImprumut.im[i]))

    def topr(self):
        self.listWidget.clear()
        control.stat_topr()
        for i in range(0,5):
            if i<len(control.top.cl) :
                if control.ord[int(control.top.cl[i].getIds())-1] > 0: 
                    self.listWidget.addItem('ID : '+str(control.top.cl[i].getIds()))
                    self.listWidget.addItem('Name : '+str(control.top.cl[i].getName()))
                    self.listWidget.addItem('CNP : '+str(control.top.cl[i].getCnp()))
                    self.listWidget.addItem('Number of books : '+str(control.ord[int(control.top.cl[i].getIds())-1]))
                    self.listWidget.addItem('------------')

    def topb(self):
        self.listWidget.clear()
        control.stat_topb()
        for i in range(0,5):
           if i<len(control.top2.cr) and control.ord[int(control.top2.cr[i].getIds())-1] >0 :
            self.listWidget.addItem('ID : '+str(control.top2.cr[i].getIds()))
            self.listWidget.addItem('Title : '+str(control.top2.cr[i].getTitle()))
            self.listWidget.addItem('Author : '+str(control.top2.cr[i].getAuthor()))
            self.listWidget.addItem('Times Borrowed : '+str(control.ord[int(control.top2.cr[i].getIds())-1]))
            self.listWidget.addItem('------------')
    def closeEvent(self,QCloseEvent):
        Controller.control.opened['fx']=0
         
        return super().closeEvent(QCloseEvent)  

   
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(235, 320)
        Form.setWindowIcon(QtGui.QIcon('UI\logo.png'))
        Form.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);"))
        self.horizontalLayout = QtGui.QVBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.b = QtGui.QPushButton(Form)
        self.b.setGeometry(QtCore.QRect(20, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)
        self.b.setFont(font)
        self.b.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.b.setObjectName(_fromUtf8("Add_Button"))
 
        self.c = QtGui.QPushButton(Form)
        self.c.setGeometry(QtCore.QRect(20, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)
        self.c.setFont(font)
        self.c.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.c.setObjectName(_fromUtf8("c_Button"))

 
        self.listWidget = QtGui.QListWidget(Form)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addWidget(self.b)
        self.horizontalLayout.addWidget(self.c)
        self.b.setFixedSize(120,30)
        self.c.setFixedSize(120,30)
        self.b.clicked.connect(self.topr)
        self.c.clicked.connect(self.topb)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Watch", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.b.setText(_translate("Form", "Top Readers", None))
        self.c.setText(_translate("Form", "Top Books", None))

