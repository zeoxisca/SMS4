# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sm4_zeox(object):
    def setupUi(self, sm4_zeox):
        sm4_zeox.setObjectName("sm4_zeox")
        sm4_zeox.resize(262, 383)
        sm4_zeox.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(sm4_zeox)
        self.centralwidget.setObjectName("centralwidget")
        self.normBtn = QtWidgets.QPushButton(self.centralwidget)
        self.normBtn.setGeometry(QtCore.QRect(8, 137, 246, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.normBtn.setFont(font)
        self.normBtn.setObjectName("normBtn")
        self.fileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fileBtn.setGeometry(QtCore.QRect(8, 207, 246, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.fileBtn.setFont(font)
        self.fileBtn.setObjectName("fileBtn")
        self.authBtn = QtWidgets.QPushButton(self.centralwidget)
        self.authBtn.setGeometry(QtCore.QRect(8, 277, 246, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.authBtn.setFont(font)
        self.authBtn.setObjectName("authBtn")
        self.line_1 = QtWidgets.QLabel(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(8, 197, 246, 1))
        self.line_1.setText("")
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QLabel(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(8, 267, 246, 1))
        self.line_2.setText("")
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QLabel(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(8, 336, 246, 1))
        self.line_3.setText("")
        self.line_3.setObjectName("line_3")
        self.top_label = QtWidgets.QLabel(self.centralwidget)
        self.top_label.setGeometry(QtCore.QRect(8, 8, 246, 111))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.top_label.setFont(font)
        self.top_label.setObjectName("top_label")
        self.low_label = QtWidgets.QLabel(self.centralwidget)
        self.low_label.setGeometry(QtCore.QRect(162, 340, 91, 20))
        self.low_label.setObjectName("low_label")
        self.top_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.top_label_2.setGeometry(QtCore.QRect(8, 26, 246, 96))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(16)
        self.top_label_2.setFont(font)
        self.top_label_2.setStyleSheet("")
        self.top_label_2.setObjectName("top_label_2")
        sm4_zeox.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(sm4_zeox)
        self.statusbar.setObjectName("statusbar")
        sm4_zeox.setStatusBar(self.statusbar)

        self.retranslateUi(sm4_zeox)
        QtCore.QMetaObject.connectSlotsByName(sm4_zeox)

    def retranslateUi(self, sm4_zeox):
        _translate = QtCore.QCoreApplication.translate
        sm4_zeox.setWindowTitle(_translate("sm4_zeox", "SMS4_ZEOX"))
        self.normBtn.setText(_translate("sm4_zeox", "NORMAL"))
        self.fileBtn.setText(_translate("sm4_zeox", "FILE"))
        self.authBtn.setText(_translate("sm4_zeox", "EXIT"))
        self.top_label.setText(_translate("sm4_zeox", "<html><head/><body><p><br/></p></body></html>"))
        self.low_label.setText(_translate("sm4_zeox", "Copy@Right"))
        self.top_label_2.setText(_translate("sm4_zeox", "  SMS4_ZEOX"))

