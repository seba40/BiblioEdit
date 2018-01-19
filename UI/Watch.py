# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Watch2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)      
         
    def update(self,item):
        self.listWidget.addItem(str(item))
    def closeEvent(self,QCloseEvent):
        Controller.control.opened['window']=0
         
        return super().closeEvent(QCloseEvent)  
   
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(235, 320)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);"))
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)

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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Watch", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

