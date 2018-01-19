# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
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

class Ui_web(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def closeEvent(self,QCloseEvent):
        Controller.control.opened['gx']=0
         
        return super().closeEvent(QCloseEvent)  

    def setupUi(self, web):
        web.setObjectName(_fromUtf8("web"))
        web.resize(473, 299)
        web.setWindowIcon(QtGui.QIcon('UI\logo.png'))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        web.setFont(font)
        web.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);"))
        self.horizontalLayout = QtGui.QHBoxLayout(web)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.webView = QtWebKit.QWebView(web)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Adobe Arabic"))
        self.webView.setFont(font)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("https://www.goodreads.com/")))
        self.webView.setZoomFactor(0.699999988079071)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayout.addWidget(self.webView)

        self.retranslateUi(web)
        QtCore.QMetaObject.connectSlotsByName(web)

    def retranslateUi(self, web):
        web.setWindowTitle(_translate("web", "Web", None))

from PyQt4 import QtWebKit
