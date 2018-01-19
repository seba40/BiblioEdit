# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Book_View.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Controller import Controller
from Controller.File import File
import copy


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

class Ui_Book_Watch(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.sort_opt=1

    def update_watch(self,item):
        if self.sort_opt==1:
            item.clear()
            for i in range(0,len(Controller.control.rCarte.cr)):
                item.addItem(str(Controller.control.rCarte.cr[i].getTitle()))
            item.setCurrentRow(-1)
        if self.sort_opt==2:
            item.clear()
            cpy=[]
            for i in Controller.control.rCarte.cr:
                cpy.append(i.getTitle())
            cpy=sorted(cpy)
            for i in cpy:
                item.addItem(str(i))
            item.setCurrentRow(-1)
        if self.sort_opt==3:
            item.clear()
            self.cpy=[]
            
            self.aux=0
            for i in Controller.control.rCarte.cr:
                self.cpy.append(i)
            for i in range (0,len(self.cpy)-1):
                for j in range(i+1,len(self.cpy)):
                    if str(self.cpy[i].getAuthor()) > str(self.cpy[j].getAuthor()):
                        self.aux=self.cpy[i]
                        self.cpy[i]=self.cpy[j]
                        self.cpy[j]=self.aux
            for i in self.cpy:
                item.addItem(str(i.getTitle()))


    def sort(self):
        if self.comboBox.currentIndex()==0:
            self.sort_opt=1
            self.update_watch(self.listView)
        if self.comboBox.currentIndex()==1:
            self.sort_opt=2
            self.update_watch(self.listView)
        if self.comboBox.currentIndex()==2:
            self.sort_opt=3
            self.update_watch(self.listView)


    def setPage(self):
        index=self.listView.currentItem().text()
        for i in Controller.control.rCarte.cr:
            if i.getTitle()==index:
                self.image_label.setPixmap(QtGui.QPixmap(_fromUtf8(i.getImage())))
                self.title_label.setText(i.getTitle())
                self.author_label.setText(i.getAuthor())
                file=File()
                file.openDesc(i.getDesc())
                self.description_text.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Soft Elegance\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">%s</p></body></html>" % (''.join(file.openDesc(i.getDesc()))))
                self.by_label.setText(_translate("Book_Watch", "by", None))



    def closeEvent(self,QCloseEvent):
        Controller.control.opened['bk']=0
         
        return super().closeEvent(QCloseEvent)  


    def setupUi(self, Book_Watch):
        Book_Watch.setObjectName(_fromUtf8("Book_Watch"))
        Book_Watch.resize(657, 436)
        Book_Watch.setFixedSize(657, 436)
        Book_Watch.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);"))
        self.listView = QtGui.QListWidget(Book_Watch)
        self.listView.setGeometry(QtCore.QRect(380, 50, 256, 371))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.listView.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.listView.setFont(font)




        self.sort_label = QtGui.QLabel(Book_Watch)
        self.sort_label.setGeometry(QtCore.QRect(380, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.sort_label.setFont(font)
        self.sort_label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.sort_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sort_label.setObjectName(_fromUtf8("sort_label"))
        self.comboBox = QtGui.QComboBox(Book_Watch)
        self.comboBox.setGeometry(QtCore.QRect(480, 20, 101, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.image_label = QtGui.QLabel(Book_Watch)
        self.image_label.setGeometry(QtCore.QRect(140, 30, 101, 151))
        self.image_label.setText(_fromUtf8(""))
        self.image_label.setScaledContents(False)
        self.image_label.setObjectName(_fromUtf8("image_label"))
        self.title_label = QtGui.QLabel(Book_Watch)
        self.title_label.setGeometry(QtCore.QRect(90, 200, 201, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(14)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setWordWrap(True)
        self.title_label.setIndent(-1)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.by_label = QtGui.QLabel(Book_Watch)
        self.by_label.setGeometry(QtCore.QRect(90, 230, 201, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(14)
        self.by_label.setFont(font)
        self.by_label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.by_label.setAlignment(QtCore.Qt.AlignCenter)
        self.by_label.setObjectName(_fromUtf8("by_label"))
        self.author_label = QtGui.QLabel(Book_Watch)
        self.author_label.setGeometry(QtCore.QRect(90, 260, 201, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(14)
        self.author_label.setFont(font)
        self.author_label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.author_label.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label.setObjectName(_fromUtf8("author_label"))
        self.description_text = QtGui.QTextBrowser(Book_Watch)
        self.description_text.setGeometry(QtCore.QRect(30, 290, 321, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.description_text.setFont(font)
        self.description_text.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.description_text.setFrameShape(QtGui.QFrame.NoFrame)
        self.description_text.setFrameShadow(QtGui.QFrame.Plain)
        self.description_text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.description_text.setObjectName(_fromUtf8("description_text"))
        self.pushButton = QtGui.QPushButton(Book_Watch)
        self.pushButton.setGeometry(QtCore.QRect(600, 20, 31, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.sort)


        self.retranslateUi(Book_Watch)
        QtCore.QObject.connect(self.listView, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.setPage)
        QtCore.QMetaObject.connectSlotsByName(Book_Watch)


    def retranslateUi(self, Book_Watch):
        Book_Watch.setWindowTitle(_translate("Book_Watch", "Book Viewer", None))
        self.sort_label.setText(_translate("Book_Watch", "SORT BY :", None))
        self.comboBox.setItemText(0, _translate("Book_Watch", "ID", None))
        self.comboBox.setItemText(1, _translate("Book_Watch", "Title", None))
        self.comboBox.setItemText(2, _translate("Book_Watch", "Author", None))
        self.pushButton.setText(_translate("Book_Watch", "OK", None))
