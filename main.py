import sys
sys.path.append("./extend")
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from mainWindow import Ui_sm4_zeox
from PyQt5.QtCore import *
import time
import math
from PyQt5.QtGui import *
from normalWindow import Ui_normal_sms
from fileWindow import Ui_Form

import hashlib
from EN import NMEN, NMDE, FLEN, FLDE, FLEnDealIn

global input_text, output_text, password

class mainWindow(QMainWindow, Ui_sm4_zeox):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.mainLayout = QGridLayout(self)
        self.SHADOW_WIDTH = 8
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.normalchild = normalWindow()
        self.filechild = fileWindow()
        self.setFixedSize(self.width(), self.height())
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.authBtn.clicked.connect(self.transClose)
        self.authBtn.clicked.connect(QCoreApplication.instance().quit)
        self.normBtn.clicked.connect(self.normalchild.firstSet)
        self.normBtn.clicked.connect(self.normalchild.show)
        self.normBtn.clicked.connect(self.normalchild.transOpen)
        self.fileBtn.clicked.connect(self.filechild.firstSet)
        self.fileBtn.clicked.connect(self.filechild.show)
        self.fileBtn.clicked.connect(self.filechild.transOpen)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("background-color:#2C3E50;")
        self.style = """ 
                        QPushButton{background-color:white;color:gray;border:none;} 
                        #sm4_zeox{ background:white;}
                        QLabel{background:gray;}
                        #top_label{background:#33cc99;color:white;font-weight:bold;}
                        #low_label{background:white;color:gray;}
                        #top_label_2{background:transparent;color:white;font-weight:bold;}
                        QPushButton:hover{background-color:gray;color:white;}
                    """
        self.setStyleSheet(self.style)

    def normalShow(self):
        print(1)
        self.mainLayout.addWidget(self.normalchild)  # 添加子窗口
        self.normalchild.show()

    # def fileShow(self):
    #     self.mainLayout.addWidget(self.filechild)  # 添加子窗口
    #     self.filechild.show()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    def transClose(self):
        i = 0.9
        while i>0:
            self.setWindowOpacity(i)
            time.sleep(0.02)
            i-=0.1

    def drawShadow(self, painter):
        # 绘制左上角、左下角、右上角、右下角、上、下、左、右边框
        self.pixmaps = list()
        self.pixmaps.append(str("./img/l_top.png"))
        self.pixmaps.append(str("./img/l_bottom.png"))
        self.pixmaps.append(str("./img/r_top.png"))
        self.pixmaps.append(str("./img/r_bottom.png"))
        self.pixmaps.append(str("./img/top.png"))
        self.pixmaps.append(str("./img/bottom.png"))
        self.pixmaps.append(str("./img/left.png"))
        self.pixmaps.append(str("./img/right.png"))
        painter.drawPixmap(0, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[0]))  # 左上角
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, 0, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[2]))  # 右上角
        painter.drawPixmap(0, self.height() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[1]))  # 左下角
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH,
                           self.SHADOW_WIDTH, self.SHADOW_WIDTH, QPixmap(self.pixmaps[3]))  # 右下角
        painter.drawPixmap(0, self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[6]).scaled(self.SHADOW_WIDTH,
                                                           self.height() - 2 * self.SHADOW_WIDTH))  # 左
        painter.drawPixmap(self.width() - self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           self.height() - 2 * self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[7]).scaled(self.SHADOW_WIDTH,
                                                           self.height() - 2 * self.SHADOW_WIDTH))  # 右
        painter.drawPixmap(self.SHADOW_WIDTH, 0, self.width() - 2 * self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[4]).scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                           self.SHADOW_WIDTH))  # 上
        painter.drawPixmap(self.SHADOW_WIDTH, self.height() - self.SHADOW_WIDTH,
                           self.width() - 2 * self.SHADOW_WIDTH, self.SHADOW_WIDTH,
                           QPixmap(self.pixmaps[5]).scaled(self.width() - 2 * self.SHADOW_WIDTH,
                                                           self.SHADOW_WIDTH))  # 下

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawShadow(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        painter.drawRect(QRect(self.SHADOW_WIDTH, self.SHADOW_WIDTH, self.width() - 2 * self.SHADOW_WIDTH,
                               self.height() - 2 * self.SHADOW_WIDTH))

            # def normalShow(self):
    #     self.mainLayout.addWidget(self.normalchild)  # 添加子窗口
    #     self.normalchild.show()
    #
    # def fileShow(self):
    #     self.mainLayout.addWidget(self.filechild)  # 添加子窗口
    #     self.filechild.show()


class normalWindow(QMainWindow, Ui_normal_sms):
    def __init__(self):
        super(normalWindow, self).__init__()
        self.key = ''
        self.message = ''
        self.cypher = ''
        self.setupUi(self)
        self.setWindowOpacity(0.01)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.clsBtn.clicked.connect(self.transClose)
        self.clsBtn.clicked.connect(self.close)
        pixMap = QPixmap("./img/back.jpg").scaled(self.left_label.width(), self.left_label.height())
        self.left_label.setPixmap(pixMap)
        self.style = """ 

                        #normal_sms{ background:#2C3E50;}
                        #left_label{background-image:'./img/back.jpg'}

                        
                        #top_label{background:#33cc99;color:#2C3E50;font-weight:bold;}
                        #low_label{background:#2C3E50;color:white;}
                        #top_label_2{background:transparent;color:white;font-weight:bold;}

                        #msgLabel{background:#2C3E50;color:white;}
                        #cyrLabel{background:#2C3E50;color:white;}
                        #keyLabel{background:#2C3E50;color:white;}
                        
                        #encBtn{background-color:#2C3E50;color:white;border:1px;}
                        #decBtn{background-color:#2C3E50;color:white;border:1px;}
                        #clnBtn{background-color:#2C3E50;color:white;border:1px;}
                        #encBtn:hover{background-color:#042441;color:white;}
                        #decBtn:hover{background-color:#042441;color:white;}
                        #clnBtn:hover{background-color:#042441;color:white;}
                        #clsBtn{background-color:#2C3E50;color:white;border:1px;}
                        #clsBtn:hover{background-color:#042441;color:white;}
                        """
        self.setStyleSheet(self.style)
        self.setMouseTracking(True)
        self.encBtn.clicked.connect(self.getMsg)
        # self.encBtn.clicked.connect(self.EN)
        self.encBtn.clicked.connect(self.showCypher)

        self.decBtn.clicked.connect(self.getCpr)
        # self.decBtn.clicked.connect(self.DE)
        self.decBtn.clicked.connect(self.showMessage)

    def getCpr(self):
        self.key = self.keyEdit.text()
        self.cypher = self.cyrEdit.toPlainText()
        if self.key == '' or self.cypher == '':
            reply = QMessageBox.information(self,  # 使用infomation信息框
                                            "warning",
                                            "请输入内容",
                                            QMessageBox.Yes)
        else:
            self.DE()

    def DE(self):
        self.message = NMDE(self.cypher,self.key)

    def showMessage(self):
        self.msgEdit.setText(self.message)

    def getMsg(self):
        self.key = self.keyEdit.text()
        self.message = self.msgEdit.toPlainText()
        if self.message == '16271135':
            reply = QMessageBox.information(self,  # 使用infomation信息框
                                            "哈哈哈哈哈啊哈哈",
                                            "zeoxisC",
                                            QMessageBox.Yes)
        if self.message == '' or self.key == '':
            reply = QMessageBox.information(self,  # 使用infomation信息框
                                            "warning",
                                            "请输入内容",
                                            QMessageBox.Yes)
        else:
            self.EN()


    def EN(self):
        self.cypher = NMEN(self.message,self.key)
    def showCypher(self):
        self.cyrEdit.setText(self.cypher)

    def transOpen(self):
        i = 0

        while i <= 1:
            self.setWindowOpacity(i)
            time.sleep(0.02)
            i += 0.1

    def firstSet(self):
        self.setWindowOpacity(0)

    def transClose(self):
        i = 0.9
        while i>0:
            self.setWindowOpacity(i)
            time.sleep(0.02)
            i-=0.1

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False


class fileWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(fileWindow, self).__init__()
        self.saveName = ''
        self.filename = ''
        self.key = ''
        self.setupUi(self)
        self.setWindowOpacity(0.01)
        self.clsBtn.clicked.connect(self.transClose)
        self.setFixedSize(self.width(), self.height())
        self.clsBtn.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        pixMap = QPixmap("./img/top.jpg").scaled(self.top_label.width(), self.top_label.height())
        self.top_label.setPixmap(pixMap)
        self.style = """ 
                        #pushButton{background-color:#2C3E50;color:white;border:1px;}
                        
                        
                        #pushButton_2{background-color:#2C3E50;color:white;border:1px;}
                        #pushButton_3{background-color:#2C3E50;color:white;border:1px;}
                        #pushButton_4{background-color:#2C3E50;color:white;border:1px;}
                        #pushButton_5{background-color:#2C3E50;color:white;border:1px;}
                        
                        #pushButton:hover{background-color:#042441;color:white}
                        #pushButton_2:hover{background-color:#042441;color:white}
                        #pushButton_3:hover{background-color:#042441;color:white}
                        #pushButton_4:hover{background-color:#042441;color:white}
                        #pushButton_5:hover{background-color:#042441;color:white}
                        #clsBtn{background-color:#2C3E50;color:white;border:1px;}
                        #Form{ background:#2C3E50;}
                        #top_label{background-image:'./img/back.jpg'}
                        QLabel{background:#2C3E50;color:white;}
                        #clsBtn{background:transparent;}
                        #clsBtn:hover{color:gray}
                        #pushButton_4{background:#2C3E50;}
                        #pushButton_5{background:#2C3E50;}
                        #pushButton_4:hover{background-color:#042441;color:white;}
                        #pushButton_5:hover{background-color:#042441;color:white;}
                        #top_label{background:#33cc99;color:white;font-weight:bold;}
                        #low_label{background:white;color:white;}
                        #top_label_2{background:transparent;color:white;font-weight:bold;}
                        """
        self.setStyleSheet(self.style)
        self.pushButton.clicked.connect(self.selectFile)
        self.pushButton_2.clicked.connect(self.selectDir)
        self.pushButton_4.clicked.connect(self.en_getkey)
        # self.pushButton_4.clicked.connect(self.EN)
        self.pushButton_5.clicked.connect(self.de_getkey)
        # self.pushButton_5.clicked.connect(self.DE)
    def selectFile(self):
        self.filename, self.filetype = QFileDialog.getOpenFileName(self, "SelectFile", "C:/", "All Files(*);;Des Files(*.des)")
        self.lineEdit.setText(self.filename)
        # print(filename ,self.filetype)


    def selectDir(self):
        self.saveName, self.ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "C:/",
                                                     "All Files (*)")
        self.lineEdit_2.setText(self.saveName)

    def en_getkey(self):
        self.key = self.lineEdit_3.text()
        if self.filename == '' or self.key == '' or self.saveName == '':
            reply = QMessageBox.information(self,  # 使用infomation信息框
                                            "warning",
                                            "请填满设置",
                                            QMessageBox.Yes)
        else:
            self.EN()

    def de_getkey(self):
        self.key = self.lineEdit_3.text()
        if self.filename == '' or self.key == '' or self.saveName == '':
            reply = QMessageBox.information(self,  # 使用infomation信息框
                                            "warning",
                                            "请填满设置",
                                            QMessageBox.Yes)
        else:
            self.DE()

    def EN(self):
        FLEN(self.filename,self.saveName,self.key)

    def DE(self):
        FLDE(self.filename,self.saveName,self.key)

    def firstSet(self):
        self.setWindowOpacity(0)
        print(1)


    def transOpen(self):
        i = 0
        print(2)
        while i <= 1:
            self.setWindowOpacity(i)
            time.sleep(0.02)
            i += 0.1

    def transClose(self):
        i = 0.9
        while i > 0:
            self.setWindowOpacity(i)
            time.sleep(0.02)
            i -= 0.1

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec())