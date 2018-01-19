# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
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

class Ui_Error_Window(QtGui.QWidget):
    def __init__(self,text):
        QtGui.QWidget.__init__(self)
        self.textbox=str(text)

        self.setupUi(self)

    def setupUi(self, Error_Window):
        Error_Window.setObjectName(_fromUtf8("Error_Window"))
        Error_Window.resize(171, 96)
        Error_Window.setFixedSize(171, 96)
        Error_Window.setWindowIcon(QtGui.QIcon('UI\logo.png'))



        Error_Window.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);"))

        self.pushButton = QtGui.QPushButton(Error_Window)
        self.pushButton.setGeometry(QtCore.QRect(50, 60, 71, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(Error_Window.close)
        self.label = QtGui.QLabel(Error_Window)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Error_Window)
        QtCore.QMetaObject.connectSlotsByName(Error_Window)

    def retranslateUi(self, Error_Window):
        Error_Window.setWindowTitle(_translate("Error_Window", "Error", None))
        self.pushButton.setText(_translate("Error_Window", "OK", None))
        self.label.setText(_translate("Error_Window", str(self.textbox), None))

