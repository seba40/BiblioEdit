# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from Controller import Controller
from PyQt4.QtCore import QTimer
from UI.Error import Ui_Error_Window



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

class Ui_modify4(QtGui.QWidget):
    def __init__(self,bk):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.bk=bk
        self.alpha=255
        self.fileDesc=''
        self.fileImage=''
    def show_error(self,text):
        self.error=Ui_Error_Window(text)
        self.error.show()
    def donel(self):
        self.alpha-=1
        if self.alpha >0:
            self.done.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255,%s);"%(self.alpha)))
        elif self.alpha==0:
            self.done.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255,%s);"%(self.alpha)))
            self.time.stop()
    def timer(self):
        self.time=QTimer()
        self.time.timeout.connect(self.donel)
        self.done.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255,255);"))
        self.alpha=255
        self.time.start(7)






    def setopt(self,x,stack):
        self.select_line.setGeometry(QtCore.QRect(x, 10, 101, 16))
        self.select_line.show()
        self.stackedWidget.setCurrentIndex(0)
        self.modify_widget.setCurrentIndex(stack)
        self.modify_widget.hide()
        self.select_line2.hide()


    def setpage(self,opt):
        if opt ==2 and self.modify_widget.currentIndex()==2:
            self.set_delete3()
        self.add_widget.setCurrentIndex(opt)
        self.change_widget.setCurrentIndex(opt)
        self.delete_widget.setCurrentIndex(opt)
        self.modify_widget.show()
        if opt== 0:
            self.select_line2.setGeometry(QtCore.QRect(40, -10, 21, 20))
        elif opt== 1:
            self.select_line2.setGeometry(QtCore.QRect(180, -10, 21, 20))
        elif opt == 2:
            self.select_line2.setGeometry(QtCore.QRect(320, -10, 21, 20))

        self.select_line2.show()
    def image_path(self):
        try:
            self.fileImage = QtGui.QFileDialog.getOpenFileName(self, 'Open',filter='*.png')
        except:
            pass
    def desc_path(self):
        try:
            self.fileDesc = QtGui.QFileDialog.getOpenFileName(self, 'Open',filter='*.txt')
        except:
            pass
    def closeEvent(self,QCloseEvent):
        Controller.control.opened['bx']=0
         
        return super().closeEvent(QCloseEvent)  


    def add(self):
        if self.add_widget.currentIndex()==0:
            title=self.title_text1.text()
            author=self.author_text1.text()
            if Controller.control.val_data(self.fileDesc,self.fileImage) == True:
                Controller.control.add_Carte(0,title, author,self.fileDesc,self.fileImage)
                self.title_text1.clear()
                self.author_text1.clear()
                self.timer()
                self.fileDesc=''
                self.fileImage=''

            else:
                self.show_error('Cover and details missing !')
        elif self.add_widget.currentIndex()==1:
            name=self.name_text1.text()
            if Controller.control.val_cnp(self.cnp_text1.text())==True:
                cnp=self.cnp_text1.text()
            else: 
                self.show_error('CCN is invalid !')

            if Controller.control.val_cnp(self.cnp_text1.text())==True:

                Controller.control.add_Client(0,name,cnp)
                self.name_text1.clear()
                self.cnp_text1.clear()
                self.timer()

        elif self.add_widget.currentIndex()==2:
            if Controller.control.val_int(self.idbook_text1.text()) == True and Controller.control.val_int(self.idclient_text1.text()) == True:
                if Controller.control.val_range(int(self.idbook_text1.text()),1) == True and Controller.control.val_range(int(self.idclient_text1.text()),2) == True:
                    idbook=int(self.idbook_text1.text())
                    idclient=int(self.idclient_text1.text())
                else:
                    self.show_error('ID is not available !')

            else:
                self.show_error('Input is not a number !')
            year=self.borrowed_text1.date().year()
            month=self.borrowed_text1.date().month()
            day=self.borrowed_text1.date().day()
            datai=str(day)+ "."+str(month)+ "."+ str(year)

            year=self.due_text1.date().year()
            month=self.due_text1.date().month()
            day=self.due_text1.date().day()
            datar=str(day)+ "."+str(month)+ "."+ str(year)
            if Controller.control.val_int(self.idbook_text1.text()) == True and Controller.control.val_int(self.idclient_text1.text()) == True:
                if Controller.control.val_range(int(self.idbook_text1.text()),1) == True and Controller.control.val_range(int(self.idclient_text1.text()),2) == True:
                    Controller.control.add_Imprumut(0, idbook, idclient, datai, datar)
                    self.idbook_text1.clear()
                    self.idclient_text1.clear()
                    self.timer()



        self.bk.update_watch(self.bk.listView)
    
    def change(self):
        if self.change_widget.currentIndex() ==0:
            if Controller.control.val_int(self.id_text1.text()):
                if Controller.control.val_range(int(self.id_text1.text()),1)==True:
                    id=int(self.id_text1.text())
            title=self.title_text2.text()
            author=self.author_text2.text()
            if Controller.control.val_int(self.id_text1.text()):

                if Controller.control.val_range(int(self.id_text1.text()),1)==True:

                    Controller.control.change_Carte(id,title, author,self.fileDesc,self.fileImage)
                    self.id_text1.clear()
                    self.title_text2.clear()
                    self.author_text2.clear()
                    self.fileDesc=''
                    self.fileImage=''

                    self.timer()
                else:
                    self.show_error('ID is not available !')
            else:
                self.show_error('ID is not a number !')

        elif self.change_widget.currentIndex() ==1:
            if Controller.control.val_int(self.id_text2.text()):
                if Controller.control.val_range(int(self.id_text2.text()),2)==True:
                    id=int(self.id_text2.text())
            name=self.name_text12.text()
            if Controller.control.val_cnp(self.cnp_text12.text())==True:

                ccn=self.cnp_text12.text()
            if Controller.control.val_int(self.id_text2.text()):
                if Controller.control.val_range(int(self.id_text2.text()),2)==True:
                    if Controller.control.val_cnp(self.cnp_text12.text())==True:
                        Controller.control.change_Client(id,name,ccn)
                        self.id_text2.clear()
                        self.name_text12.clear()
                        self.cnp_text12.clear()
                        self.timer()
                    else:
                        self.show_error('CCN is invalid !')
                else:
                    self.show_error('ID is not available !')
            else:
                self.show_error('ID is not a number !')
        elif self.change_widget.currentIndex() ==2:
            if Controller.control.val_int(self.idbook_text2_2.text())==True:
                if Controller.control.val_range(self.idbook_text2_2.text(),3)==True:
                    id= int(self.idbook_text2_2.text())
            
            if Controller.control.val_int(self.idbook_text2.text(),empty=1) == True:
                if Controller.control.val_range(self.idbook_text2.text(),1,empty=1) == True:
                    if self.idbook_text2.text()!='':
                        idbook=int(self.idbook_text2.text())
                    else:
                        idbook=''
            if Controller.control.val_int(self.idclient_text2.text(),empty=1) == True:
                if Controller.control.val_range(self.idclient_text2.text(),2,empty=1) == True:
                    if self.idclient_text2.text()!='':
                        idclient=int(self.idclient_text2.text())
                    else:
                        idclient=''
            year=self.borrowed_text2.date().year()
            month=self.borrowed_text2.date().month()
            day=self.borrowed_text2.date().day()
            datai=str(day)+ "."+str(month)+ "."+ str(year)

            year=self.due_text2.date().year()
            month=self.due_text2.date().month()
            day=self.due_text2.date().day()
            datar=str(day)+ "."+str(month)+ "."+ str(year)
            if Controller.control.val_int(self.idbook_text2_2.text())==True and Controller.control.val_int(self.idbook_text2.text(),empty=1) == True and Controller.control.val_int(self.idclient_text2.text(),empty=1) == True:
                if Controller.control.val_range(int(self.idbook_text2_2.text()),3)==True and Controller.control.val_range(self.idbook_text2.text(),1,empty=1) == True and Controller.control.val_range(self.idclient_text2.text(),2,empty=1) == True:

                    Controller.control.change_Imprumut(id, idbook, idclient, datai, datar)
                    self.idbook_text2.clear()
                    self.idclient_text2.clear()
                    self.idbook_text2_2.clear()
                    self.timer()
                else: 
                    self.show_error('ID is not available !')
            else:
                self.show_error('ID is not a number !')

    

        self.bk.update_watch(self.bk.listView)

    def set_delete1(self):
        if self.delete_text1.currentIndex() == 0:
            self.item_text1.clear()
            for i in Controller.control.rCarte.cr:
                self.item_text1.addItem(str(i.getIds()))
        if self.delete_text1.currentIndex() == 1:
            self.item_text1.clear()
            for i in Controller.control.rCarte.cr:
                self.item_text1.addItem(str(i.getTitle()))     
        if self.delete_text1.currentIndex() == 2:
            self.item_text1.clear()
            self.alist=[]
            for i in Controller.control.rCarte.cr:
                self.alist.append(i.getAuthor())

            myList = sorted(set(self.alist))
            for i in myList:
                self.item_text1.addItem(str(i))     
    def set_delete2(self):
        if self.delete_text2.currentIndex() == 0:
            self.item_text1_2.clear()
            for i in Controller.control.rClient.cl:
                self.item_text1_2.addItem(str(i.getIds()))
        if self.delete_text2.currentIndex() == 1:
            self.item_text1_2.clear()
            for i in Controller.control.rClient.cl:
                self.item_text1_2.addItem(str(i.getName()))     
        if self.delete_text2.currentIndex() == 2:
            self.item_text1_2.clear()
            for i in Controller.control.rClient.cl:
                self.item_text1_2.addItem(str(i.getCnp()))
    def set_delete3(self):
        self.delete_text4.clear()
        for i in Controller.control.rImprumut.im:
                self.delete_text4.addItem(str(i.getIds()))
    def delete(self):

        if self.delete_widget.currentIndex() ==0 :
                if self.delete_text1.currentIndex() == 0:
                    self.gigi=int(self.item_text1.currentText())
                    Controller.control.delete_Carte(1,int(self.gigi))
                    self.item_text1.removeItem(self.item_text1.currentIndex())
                if self.delete_text1.currentIndex() == 1:
                    self.gigi=self.item_text1.currentText()
                    Controller.control.delete_Carte(2,self.gigi)
                    self.item_text1.removeItem(self.item_text1.currentIndex())
                if self.delete_text1.currentIndex() == 2:
                    self.gigi=self.item_text1.currentText()
                    Controller.control.delete_Carte(3,self.gigi)
                    self.item_text1.removeItem(self.item_text1.currentIndex())
        if self.delete_widget.currentIndex() ==1 :
                if self.delete_text2.currentIndex() == 0:
                    self.gigi=int(self.item_text1_2.currentText())
                    Controller.control.delete_Client(1,int(self.gigi))
                    self.item_text1_2.removeItem(self.item_text1_2.currentIndex())
                if self.delete_text2.currentIndex() == 1:
                    self.gigi=self.item_text1_2.currentText()
                    Controller.control.delete_Client(2,self.gigi)
                    self.item_text1_2.removeItem(self.item_text1_2.currentIndex())
                if self.delete_text2.currentIndex() == 2:
                    self.gigi=self.item_text1_2.currentText()
                    Controller.control.delete_Client(3,self.gigi)
                    self.item_text1_2.removeItem(self.item_text1_2.currentIndex())
        if self.delete_widget.currentIndex() ==2 :
                self.gigi=int(self.delete_text4.currentText())
                Controller.control.delete_Imprumut(int(self.gigi))
                self.delete_text4.removeItem(self.delete_text4.currentIndex())



        self.bk.update_watch(self.bk.listView)
  
        

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(421, 420)
        Form.setFixedSize(421,420)
        Form.setWindowIcon(QtGui.QIcon('UI\logo.png'))

        Form.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);"))


        self.add_button = QtGui.QPushButton(Form)
        self.add_button.setGeometry(QtCore.QRect(20, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.add_button.clicked.connect(lambda:self.setopt(20,0))

        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 90, 381, 20))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))




        self.change_button = QtGui.QPushButton(Form)
        self.change_button.setGeometry(QtCore.QRect(160, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)
        self.change_button.setFont(font)
        self.change_button.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.change_button.setObjectName(_fromUtf8("change_button"))
        self.change_button.clicked.connect(lambda:self.setopt(160,1))


        self.delete_button = QtGui.QPushButton(Form)
        self.delete_button.setGeometry(QtCore.QRect(300, 30, 101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)
        self.delete_button.setFont(font)
        self.delete_button.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.delete_button.clicked.connect(lambda:self.setopt(300,2))


        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 110, 381, 51))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))


        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))

        self.select_line2 = QtGui.QFrame(self.page)
        self.select_line2.setGeometry(QtCore.QRect(40, 0, 21, 20))

        self.select_line2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.select_line2.setFrameShadow(QtGui.QFrame.Plain)
        self.select_line2.setLineWidth(4)
        self.select_line2.setFrameShape(QtGui.QFrame.HLine)
        self.select_line2.setObjectName(_fromUtf8("select_line2"))

        self.pushButton_4 = QtGui.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(lambda:self.setpage(0))




        self.pushButton_6 = QtGui.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_6.clicked.connect(lambda:self.setpage(1))



        self.pushButton_7 = QtGui.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(16)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_7.clicked.connect(lambda:self.setpage(2))


        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        self.modify_widget = QtGui.QStackedWidget(Form)
        self.modify_widget.setGeometry(QtCore.QRect(20, 169, 381, 221))
        self.modify_widget.setObjectName(_fromUtf8("modify_widget"))
        self.page_ADD = QtGui.QWidget()
        self.page_ADD.setObjectName(_fromUtf8("page_ADD"))
        self.add_widget = QtGui.QStackedWidget(self.page_ADD)
        self.add_widget.setGeometry(QtCore.QRect(10, 20, 361, 191))
        self.add_widget.setObjectName(_fromUtf8("add_widget"))
        self.page_Book1 = QtGui.QWidget()
        self.page_Book1.setObjectName(_fromUtf8("page_Book1"))
        self.title_label1 = QtGui.QLabel(self.page_Book1)
        self.title_label1.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.title_label1.setFont(font)
        self.title_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.title_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label1.setObjectName(_fromUtf8("title_label1"))
        self.author_label1 = QtGui.QLabel(self.page_Book1)
        self.author_label1.setGeometry(QtCore.QRect(0, 50, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.author_label1.setFont(font)
        self.author_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.author_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label1.setObjectName(_fromUtf8("author_label1"))
        self.details_label1 = QtGui.QLabel(self.page_Book1)
        self.details_label1.setGeometry(QtCore.QRect(0, 90, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.details_label1.setFont(font)
        self.details_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.details_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.details_label1.setObjectName(_fromUtf8("details_label1"))
        self.cover_label1 = QtGui.QLabel(self.page_Book1)
        self.cover_label1.setGeometry(QtCore.QRect(0, 130, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.cover_label1.setFont(font)
        self.cover_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.cover_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.cover_label1.setObjectName(_fromUtf8("cover_label1"))
        self.title_text1 = QtGui.QLineEdit(self.page_Book1)
        self.title_text1.setGeometry(QtCore.QRect(110, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.title_text1.setFont(font)
        self.title_text1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.title_text1.setFrame(False)
        self.title_text1.setObjectName(_fromUtf8("title_text1"))
        self.author_text1 = QtGui.QLineEdit(self.page_Book1)
        self.author_text1.setGeometry(QtCore.QRect(110, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.author_text1.setFont(font)
        self.author_text1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.author_text1.setFrame(False)
        self.author_text1.setObjectName(_fromUtf8("author_text1"))
        self.open_details1 = QtGui.QPushButton(self.page_Book1)
        self.open_details1.setGeometry(QtCore.QRect(140, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.open_details1.setFont(font)
        self.open_details1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.open_details1.setObjectName(_fromUtf8("open_details1"))
        self.open_details1.clicked.connect(self.desc_path)
        self.open_cover1 = QtGui.QPushButton(self.page_Book1)
        self.open_cover1.setGeometry(QtCore.QRect(140, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.open_cover1.setFont(font)
        self.open_cover1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.open_cover1.setObjectName(_fromUtf8("open_cover1"))
        self.open_cover1.clicked.connect(self.image_path)

        self.done_button1 = QtGui.QPushButton(self.page_Book1)
        self.done_button1.setGeometry(QtCore.QRect(280, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.done_button1.setFont(font)
        self.done_button1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.done_button1.setObjectName(_fromUtf8("done_button1"))
        self.done_button1.clicked.connect(self.add)

        self.add_widget.addWidget(self.page_Book1)
        self.page_Client1 = QtGui.QWidget()
        self.page_Client1.setObjectName(_fromUtf8("page_Client1"))
        self.cnp_text1 = QtGui.QLineEdit(self.page_Client1)
        self.cnp_text1.setGeometry(QtCore.QRect(110, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.cnp_text1.setFont(font)
        self.cnp_text1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.cnp_text1.setFrame(False)
        self.cnp_text1.setObjectName(_fromUtf8("cnp_text1"))
        self.name_label1 = QtGui.QLabel(self.page_Client1)
        self.name_label1.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.name_label1.setFont(font)
        self.name_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.name_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label1.setObjectName(_fromUtf8("name_label1"))
        self.done_button2 = QtGui.QPushButton(self.page_Client1)
        self.done_button2.setGeometry(QtCore.QRect(180, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.done_button2.setFont(font)
        self.done_button2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.done_button2.setObjectName(_fromUtf8("done_button2"))

        self.done_button2.clicked.connect(self.add)
        self.name_text1 = QtGui.QLineEdit(self.page_Client1)
        self.name_text1.setGeometry(QtCore.QRect(110, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.name_text1.setFont(font)
        self.name_text1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.name_text1.setFrame(False)
        self.name_text1.setObjectName(_fromUtf8("name_text1"))
        self.cnp_label1 = QtGui.QLabel(self.page_Client1)
        self.cnp_label1.setGeometry(QtCore.QRect(0, 50, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.cnp_label1.setFont(font)
        self.cnp_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.cnp_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.cnp_label1.setObjectName(_fromUtf8("cnp_label1"))
        self.add_widget.addWidget(self.page_Client1)
        self.page_Entry1 = QtGui.QWidget()
        self.page_Entry1.setObjectName(_fromUtf8("page_Entry1"))
        self.idbook_label1 = QtGui.QLabel(self.page_Entry1)
        self.idbook_label1.setGeometry(QtCore.QRect(0, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.idbook_label1.setFont(font)
        self.idbook_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.idbook_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.idbook_label1.setObjectName(_fromUtf8("idbook_label1"))
        self.idclient_label1 = QtGui.QLabel(self.page_Entry1)
        self.idclient_label1.setGeometry(QtCore.QRect(0, 50, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.idclient_label1.setFont(font)
        self.idclient_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.idclient_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.idclient_label1.setObjectName(_fromUtf8("idclient_label1"))
        self.idbook_text1 = QtGui.QLineEdit(self.page_Entry1)
        self.idbook_text1.setGeometry(QtCore.QRect(100, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.idbook_text1.setFont(font)
        self.idbook_text1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.idbook_text1.setFrame(False)
        self.idbook_text1.setObjectName(_fromUtf8("idbook_text1"))
        self.idclient_text1 = QtGui.QLineEdit(self.page_Entry1)
        self.idclient_text1.setGeometry(QtCore.QRect(100, 50, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.idclient_text1.setFont(font)
        self.idclient_text1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.idclient_text1.setFrame(False)
        self.idclient_text1.setObjectName(_fromUtf8("idclient_text1"))
        self.line_2 = QtGui.QFrame(self.page_Entry1)
        self.line_2.setGeometry(QtCore.QRect(140, 0, 20, 81))
        self.line_2.setFrameShadow(QtGui.QFrame.Raised)
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.borrowed_label1 = QtGui.QLabel(self.page_Entry1)
        self.borrowed_label1.setGeometry(QtCore.QRect(160, 10, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.borrowed_label1.setFont(font)
        self.borrowed_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.borrowed_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.borrowed_label1.setObjectName(_fromUtf8("borrowed_label1"))
        self.due_label1 = QtGui.QLabel(self.page_Entry1)
        self.due_label1.setGeometry(QtCore.QRect(170, 50, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.due_label1.setFont(font)
        self.due_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.due_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.due_label1.setObjectName(_fromUtf8("due_label1"))
        self.borrowed_text1 = QtGui.QDateEdit(self.page_Entry1)
        self.borrowed_text1.setGeometry(QtCore.QRect(270, 10, 91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.borrowed_text1.setFont(font)
        self.borrowed_text1.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);\n"
"color: rgb(255, 255, 255);"))
        self.borrowed_text1.setCalendarPopup(False)
        self.borrowed_text1.setObjectName(_fromUtf8("borrowed_text1"))
        self.due_text1 = QtGui.QDateEdit(self.page_Entry1)
        self.due_text1.setGeometry(QtCore.QRect(270, 50, 91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.due_text1.setFont(font)
        self.due_text1.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);\n"
"color: rgb(255, 255, 255);"))
        self.due_text1.setCalendarPopup(False)
        self.due_text1.setObjectName(_fromUtf8("due_text1"))
        self.done_button3 = QtGui.QPushButton(self.page_Entry1)
        self.done_button3.setGeometry(QtCore.QRect(270, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.done_button3.setFont(font)
        self.done_button3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.done_button3.setObjectName(_fromUtf8("done_button3"))
        self.done_button3.clicked.connect(self.add)
        self.add_widget.addWidget(self.page_Entry1)
        self.modify_widget.addWidget(self.page_ADD)
        self.page_CHANGE = QtGui.QWidget()
        self.page_CHANGE.setObjectName(_fromUtf8("page_CHANGE"))
        self.change_widget = QtGui.QStackedWidget(self.page_CHANGE)
        self.change_widget.setGeometry(QtCore.QRect(10, 20, 361, 191))
        self.change_widget.setObjectName(_fromUtf8("change_widget"))
        self.page_Book2 = QtGui.QWidget()
        self.page_Book2.setObjectName(_fromUtf8("page_Book2"))
        self.title_label2 = QtGui.QLabel(self.page_Book2)
        self.title_label2.setGeometry(QtCore.QRect(10, 50, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.title_label2.setFont(font)
        self.title_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.title_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label2.setObjectName(_fromUtf8("title_label2"))
        self.author_label2 = QtGui.QLabel(self.page_Book2)
        self.author_label2.setGeometry(QtCore.QRect(0, 90, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.author_label2.setFont(font)
        self.author_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.author_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.author_label2.setObjectName(_fromUtf8("author_label2"))
        self.details_label2 = QtGui.QLabel(self.page_Book2)
        self.details_label2.setGeometry(QtCore.QRect(0, 130, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.details_label2.setFont(font)
        self.details_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.details_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.details_label2.setObjectName(_fromUtf8("details_label2"))
        self.cover_label2 = QtGui.QLabel(self.page_Book2)
        self.cover_label2.setGeometry(QtCore.QRect(0, 170, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.cover_label2.setFont(font)
        self.cover_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.cover_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.cover_label2.setObjectName(_fromUtf8("cover_label2"))
        self.title_text2 = QtGui.QLineEdit(self.page_Book2)
        self.title_text2.setGeometry(QtCore.QRect(110, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.title_text2.setFont(font)
        self.title_text2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.title_text2.setFrame(False)
        self.title_text2.setObjectName(_fromUtf8("title_text2"))
        self.author_text2 = QtGui.QLineEdit(self.page_Book2)
        self.author_text2.setGeometry(QtCore.QRect(110, 90, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.author_text2.setFont(font)
        self.author_text2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.author_text2.setFrame(False)
        self.author_text2.setObjectName(_fromUtf8("author_text2"))
        self.open_details2 = QtGui.QPushButton(self.page_Book2)
        self.open_details2.setGeometry(QtCore.QRect(140, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.open_details2.setFont(font)
        self.open_details2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.open_details2.setObjectName(_fromUtf8("open_details2"))
        self.open_details2.clicked.connect(self.desc_path)
        self.open_cover2 = QtGui.QPushButton(self.page_Book2)
        self.open_cover2.setGeometry(QtCore.QRect(140, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.open_cover2.setFont(font)
        self.open_cover2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.open_cover2.setObjectName(_fromUtf8("open_cover2"))
        self.open_cover2.clicked.connect(self.image_path)
        self.done_button4 = QtGui.QPushButton(self.page_Book2)
        self.done_button4.setGeometry(QtCore.QRect(280, 170, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.done_button4.setFont(font)
        self.done_button4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))

        self.done_button4.setObjectName(_fromUtf8("done_button4"))
        self.done_button4.clicked.connect(self.change)
        self.id_text1 = QtGui.QLineEdit(self.page_Book2)
        self.id_text1.setGeometry(QtCore.QRect(110, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.id_text1.setFont(font)
        self.id_text1.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.id_text1.setFrame(False)
        self.id_text1.setObjectName(_fromUtf8("id_text1"))
        self.id_label1 = QtGui.QLabel(self.page_Book2)
        self.id_label1.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.id_label1.setFont(font)
        self.id_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.id_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label1.setObjectName(_fromUtf8("id_label1"))
        self.change_widget.addWidget(self.page_Book2)
        self.page_Client2 = QtGui.QWidget()
        self.page_Client2.setObjectName(_fromUtf8("page_Client2"))
        self.cnp_text12 = QtGui.QLineEdit(self.page_Client2)
        self.cnp_text12.setGeometry(QtCore.QRect(110, 90, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.cnp_text12.setFont(font)
        self.cnp_text12.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.cnp_text12.setFrame(False)
        self.cnp_text12.setObjectName(_fromUtf8("cnp_text12"))
        self.name_label2 = QtGui.QLabel(self.page_Client2)
        self.name_label2.setGeometry(QtCore.QRect(10, 50, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.name_label2.setFont(font)
        self.name_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.name_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label2.setObjectName(_fromUtf8("name_label2"))
        self.done_button5 = QtGui.QPushButton(self.page_Client2)
        self.done_button5.setGeometry(QtCore.QRect(180, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.done_button5.setFont(font)
        self.done_button5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.done_button5.setObjectName(_fromUtf8("done_button5"))
        self.done_button5.clicked.connect(self.change)
        self.name_text12 = QtGui.QLineEdit(self.page_Client2)
        self.name_text12.setGeometry(QtCore.QRect(110, 50, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.name_text12.setFont(font)
        self.name_text12.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.name_text12.setFrame(False)
        self.name_text12.setObjectName(_fromUtf8("name_text12"))
        self.cnp_label2 = QtGui.QLabel(self.page_Client2)
        self.cnp_label2.setGeometry(QtCore.QRect(0, 90, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.cnp_label2.setFont(font)
        self.cnp_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.cnp_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.cnp_label2.setObjectName(_fromUtf8("cnp_label2"))
        self.id_label2 = QtGui.QLabel(self.page_Client2)
        self.id_label2.setGeometry(QtCore.QRect(10, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.id_label2.setFont(font)
        self.id_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.id_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.id_label2.setObjectName(_fromUtf8("id_label2"))
        self.id_text2 = QtGui.QLineEdit(self.page_Client2)
        self.id_text2.setGeometry(QtCore.QRect(110, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(10)
        self.id_text2.setFont(font)
        self.id_text2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.id_text2.setFrame(False)
        self.id_text2.setObjectName(_fromUtf8("id_text2"))
        self.change_widget.addWidget(self.page_Client2)
        self.page_Entry2 = QtGui.QWidget()
        self.page_Entry2.setObjectName(_fromUtf8("page_Entry2"))
        self.idbook_label2 = QtGui.QLabel(self.page_Entry2)
        self.idbook_label2.setGeometry(QtCore.QRect(0, 50, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.idbook_label2.setFont(font)
        self.idbook_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.idbook_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.idbook_label2.setObjectName(_fromUtf8("idbook_label2"))
        self.idclient_label2 = QtGui.QLabel(self.page_Entry2)
        self.idclient_label2.setGeometry(QtCore.QRect(0, 90, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.idclient_label2.setFont(font)
        self.idclient_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.idclient_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.idclient_label2.setObjectName(_fromUtf8("idclient_label2"))
        self.idbook_text2 = QtGui.QLineEdit(self.page_Entry2)
        self.idbook_text2.setGeometry(QtCore.QRect(100, 50, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.idbook_text2.setFont(font)
        self.idbook_text2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.idbook_text2.setFrame(False)
        self.idbook_text2.setObjectName(_fromUtf8("idbook_text2"))
        self.idclient_text2 = QtGui.QLineEdit(self.page_Entry2)
        self.idclient_text2.setGeometry(QtCore.QRect(100, 90, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.idclient_text2.setFont(font)
        self.idclient_text2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.idclient_text2.setFrame(False)
        self.idclient_text2.setObjectName(_fromUtf8("idclient_text2"))
        self.line_4 = QtGui.QFrame(self.page_Entry2)
        self.line_4.setGeometry(QtCore.QRect(140, 0, 20, 121))
        self.line_4.setFrameShadow(QtGui.QFrame.Raised)
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(0)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.borrowed_label2 = QtGui.QLabel(self.page_Entry2)
        self.borrowed_label2.setGeometry(QtCore.QRect(160, 10, 101, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.borrowed_label2.setFont(font)
        self.borrowed_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.borrowed_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.borrowed_label2.setObjectName(_fromUtf8("borrowed_label2"))
        self.due_label2 = QtGui.QLabel(self.page_Entry2)
        self.due_label2.setGeometry(QtCore.QRect(170, 50, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.due_label2.setFont(font)
        self.due_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.due_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.due_label2.setObjectName(_fromUtf8("due_label2"))
        self.due_text2 = QtGui.QDateEdit(self.page_Entry2)
        self.due_text2.setGeometry(QtCore.QRect(270, 50, 91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.due_text2.setFont(font)
        self.due_text2.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);\n"
"color: rgb(255, 255, 255);"))
        self.due_text2.setCalendarPopup(False)
        self.due_text2.setObjectName(_fromUtf8("due_text2"))
        self.borrowed_text2 = QtGui.QDateEdit(self.page_Entry2)
        self.borrowed_text2.setGeometry(QtCore.QRect(270, 10, 91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.borrowed_text2.setFont(font)
        self.borrowed_text2.setStyleSheet(_fromUtf8("background-color: rgb(58, 58, 58);\n"
"color: rgb(255, 255, 255);"))
        self.borrowed_text2.setCalendarPopup(False)
        self.borrowed_text2.setObjectName(_fromUtf8("borrowed_text2"))
        self.done_button6 = QtGui.QPushButton(self.page_Entry2)
        self.done_button6.setGeometry(QtCore.QRect(270, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.done_button6.setFont(font)
        self.done_button6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.done_button6.setObjectName(_fromUtf8("done_button6"))
        self.done_button6.clicked.connect(self.change)
        self.idbook_label2_2 = QtGui.QLabel(self.page_Entry2)
        self.idbook_label2_2.setGeometry(QtCore.QRect(0, 10, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.idbook_label2_2.setFont(font)
        self.idbook_label2_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.idbook_label2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.idbook_label2_2.setObjectName(_fromUtf8("idbook_label2_2"))
        self.idbook_text2_2 = QtGui.QLineEdit(self.page_Entry2)
        self.idbook_text2_2.setGeometry(QtCore.QRect(100, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.idbook_text2_2.setFont(font)
        self.idbook_text2_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(58, 58, 58);"))
        self.idbook_text2_2.setFrame(False)
        self.idbook_text2_2.setObjectName(_fromUtf8("idbook_text2_2"))
        self.change_widget.addWidget(self.page_Entry2)
        self.modify_widget.addWidget(self.page_CHANGE)
        self.page_DELETE = QtGui.QWidget()
        self.page_DELETE.setObjectName(_fromUtf8("page_DELETE"))
        self.delete_widget = QtGui.QStackedWidget(self.page_DELETE)
        self.delete_widget.setGeometry(QtCore.QRect(10, 20, 361, 191))
        self.delete_widget.setObjectName(_fromUtf8("delete_widget"))
        self.page_Book3 = QtGui.QWidget()
        self.page_Book3.setObjectName(_fromUtf8("page_Book3"))
        self.item_label1 = QtGui.QLabel(self.page_Book3)
        self.item_label1.setGeometry(QtCore.QRect(10, 50, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.item_label1.setFont(font)
        self.item_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.item_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label1.setObjectName(_fromUtf8("item_label1"))
        self.done_button7 = QtGui.QPushButton(self.page_Book3)
        self.done_button7.setGeometry(QtCore.QRect(150, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.done_button7.setFont(font)
        self.done_button7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.done_button7.setObjectName(_fromUtf8("done_button7"))
        self.done_button7.clicked.connect(self.delete)

        self.delete_label1 = QtGui.QLabel(self.page_Book3)
        self.delete_label1.setGeometry(QtCore.QRect(0, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.delete_label1.setFont(font)
        self.delete_label1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.delete_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.delete_label1.setObjectName(_fromUtf8("delete_label1"))
        self.delete_text1 = QtGui.QComboBox(self.page_Book3)
        self.delete_text1.setGeometry(QtCore.QRect(110, 10, 91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.delete_text1.setFont(font)
        self.delete_text1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.delete_text1.setObjectName(_fromUtf8("delete_text1"))
        self.delete_text1.addItem(_fromUtf8(""))
        self.delete_text1.addItem(_fromUtf8(""))
        self.delete_text1.addItem(_fromUtf8(""))
        self.item_text1 = QtGui.QComboBox(self.page_Book3)
        self.item_text1.setGeometry(QtCore.QRect(110, 50, 181, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.item_text1.setFont(font)
        self.item_text1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.item_text1.setObjectName(_fromUtf8("item_text1"))
        self.delete_widget.addWidget(self.page_Book3)
        self.page_Client3 = QtGui.QWidget()
        self.page_Client3.setObjectName(_fromUtf8("page_Client3"))
        self.delete_text2 = QtGui.QComboBox(self.page_Client3)
        self.delete_text2.setGeometry(QtCore.QRect(110, 10, 91, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.delete_text2.setFont(font)
        self.delete_text2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.delete_text2.setObjectName(_fromUtf8("delete_text2"))
        self.delete_text2.addItem(_fromUtf8(""))
        self.delete_text2.addItem(_fromUtf8(""))
        self.delete_text2.addItem(_fromUtf8(""))
        self.done_button8 = QtGui.QPushButton(self.page_Client3)
        self.done_button8.setGeometry(QtCore.QRect(150, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.done_button8.setFont(font)
        self.done_button8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.done_button8.setObjectName(_fromUtf8("done_button8"))
        self.done_button8.clicked.connect(self.delete)

        self.delete_label2 = QtGui.QLabel(self.page_Client3)
        self.delete_label2.setGeometry(QtCore.QRect(0, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.delete_label2.setFont(font)
        self.delete_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.delete_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.delete_label2.setObjectName(_fromUtf8("delete_label2"))
        self.item_label2 = QtGui.QLabel(self.page_Client3)
        self.item_label2.setGeometry(QtCore.QRect(10, 50, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.item_label2.setFont(font)
        self.item_label2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.item_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.item_label2.setObjectName(_fromUtf8("item_label2"))
        self.item_text1_2 = QtGui.QComboBox(self.page_Client3)
        self.item_text1_2.setGeometry(QtCore.QRect(110, 50, 181, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.item_text1_2.setFont(font)
        self.item_text1_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.item_text1_2.setObjectName(_fromUtf8("item_text1_2"))
        self.delete_widget.addWidget(self.page_Client3)
        self.page_Entry3 = QtGui.QWidget()
        self.page_Entry3.setObjectName(_fromUtf8("page_Entry3"))
        self.delete_text4 = QtGui.QComboBox(self.page_Entry3)
        self.delete_text4.setGeometry(QtCore.QRect(150, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(11)
        self.delete_text4.setFont(font)
        self.delete_text4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.delete_text4.setObjectName(_fromUtf8("delete_text4"))
        self.done_button9 = QtGui.QPushButton(self.page_Entry3)
        self.done_button9.setGeometry(QtCore.QRect(140, 80, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.done_button9.setFont(font)
        self.done_button9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.done_button9.setObjectName(_fromUtf8("done_button9"))
        self.done_button9.clicked.connect(self.delete)

        self.done = QtGui.QLabel(Form)
        self.done.setGeometry(QtCore.QRect(173, 390, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(12)
        self.done.setFont(font)
        self.done.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255,0);"))
        self.done.setAlignment(QtCore.Qt.AlignCenter)
        self.done.setObjectName(_fromUtf8("done"))
        self.done.setText(_translate("Form", "- DONE -", None))


        self.delete_label3 = QtGui.QLabel(self.page_Entry3)
        self.delete_label3.setGeometry(QtCore.QRect(140, 10, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Soft Elegance"))
        font.setPointSize(13)
        self.delete_label3.setFont(font)
        self.delete_label3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.delete_label3.setAlignment(QtCore.Qt.AlignCenter)
        self.delete_label3.setObjectName(_fromUtf8("delete_label3"))
        self.delete_widget.addWidget(self.page_Entry3)
        self.modify_widget.addWidget(self.page_DELETE)
        self.select_line = QtGui.QFrame(Form)
        self.select_line.setGeometry(QtCore.QRect(20, 10, 101, 16))

        self.select_line.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.select_line.setFrameShadow(QtGui.QFrame.Plain)
        self.select_line.setLineWidth(2)
        self.select_line.setFrameShape(QtGui.QFrame.HLine)
        self.select_line.setObjectName(_fromUtf8("select_line"))
        self.select_line.hide()

        self.retranslateUi(Form)
        self.modify_widget.hide()
        self.stackedWidget.setCurrentIndex(1)
        self.add_widget.setCurrentIndex(0)
        self.change_widget.setCurrentIndex(2)
        self.delete_widget.setCurrentIndex(2)
        QtCore.QObject.connect(self.delete_text1, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.set_delete1)
        QtCore.QObject.connect(self.delete_text2, QtCore.SIGNAL(_fromUtf8("activated(int)")), self.set_delete2)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_translate("Form", "Modify", None))
        self.add_button.setText(_translate("Form", "ADD", None))
        self.change_button.setText(_translate("Form", "CHANGE", None))
        self.delete_button.setText(_translate("Form", "DELETE", None))
        self.pushButton_4.setText(_translate("Form", "BOOK", None))
        self.pushButton_6.setText(_translate("Form", "CLIENT", None))
        self.pushButton_7.setText(_translate("Form", "ENTRY", None))
        self.title_label1.setText(_translate("Form", "TITLE", None))
        self.author_label1.setText(_translate("Form", "AUTHOR", None))
        self.details_label1.setText(_translate("Form", "DETAILS", None))
        self.cover_label1.setText(_translate("Form", "COVER", None))
        self.open_details1.setText(_translate("Form", "OPEN", None))
        self.open_cover1.setText(_translate("Form", "OPEN", None))
        self.done_button1.setText(_translate("Form", "ADD", None))
        self.name_label1.setText(_translate("Form", "NAME", None))
        self.done_button2.setText(_translate("Form", "ADD", None))
        self.cnp_label1.setText(_translate("Form", "CCN", None))
        self.idbook_label1.setText(_translate("Form", "ID BOOK", None))
        self.idclient_label1.setText(_translate("Form", "ID CLIENT", None))
        self.borrowed_label1.setText(_translate("Form", "BORROWED", None))
        self.due_label1.setText(_translate("Form", "DUE", None))
        self.done_button3.setText(_translate("Form", "ADD", None))
        self.title_label2.setText(_translate("Form", "TITLE", None))
        self.author_label2.setText(_translate("Form", "AUTHOR", None))
        self.details_label2.setText(_translate("Form", "DETAILS", None))
        self.cover_label2.setText(_translate("Form", "COVER", None))
        self.open_details2.setText(_translate("Form", "OPEN", None))
        self.open_cover2.setText(_translate("Form", "OPEN", None))
        self.done_button4.setText(_translate("Form", "CHANGE", None))
        self.id_label1.setText(_translate("Form", "ID", None))
        self.name_label2.setText(_translate("Form", "NAME", None))
        self.done_button5.setText(_translate("Form", "CHANGE", None))
        self.cnp_label2.setText(_translate("Form", "CCN", None))
        self.id_label2.setText(_translate("Form", "ID", None))
        self.idbook_label2.setText(_translate("Form", "ID BOOK", None))
        self.idclient_label2.setText(_translate("Form", "ID CLIENT", None))
        self.borrowed_label2.setText(_translate("Form", "BORROWED", None))
        self.due_label2.setText(_translate("Form", "DUE", None))
        self.done_button6.setText(_translate("Form", "CHANGE", None))
        self.idbook_label2_2.setText(_translate("Form", "ID", None))
        self.item_label1.setText(_translate("Form", "ITEM", None))
        self.done_button7.setText(_translate("Form", "DELETE", None))
        self.delete_label1.setText(_translate("Form", "DELETE BY", None))
        self.delete_text1.setItemText(0, _translate("Form", "ID", None))
        self.delete_text1.setItemText(1, _translate("Form", "Title", None))
        self.delete_text1.setItemText(2, _translate("Form", "Author", None))
        self.delete_text2.setItemText(0, _translate("Form", "ID", None))
        self.delete_text2.setItemText(1, _translate("Form", "Name", None))
        self.delete_text2.setItemText(2, _translate("Form", "CNN", None))
        self.done_button8.setText(_translate("Form", "DELETE", None))
        self.delete_label2.setText(_translate("Form", "DELETE BY", None))
        self.item_label2.setText(_translate("Form", "ITEM", None))
        self.done_button9.setText(_translate("Form", "DELETE", None))
        self.delete_label3.setText(_translate("Form", "ID", None))

