# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sendmessage.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sendmessage(object):
    def setupUi(self, sendmessage):
        sendmessage.setObjectName("sendmessage")
        sendmessage.resize(469, 337)
        self.centralwidget = QtWidgets.QWidget(sendmessage)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 250, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 451, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 451, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 451, 111))
        self.textEdit.setObjectName("textEdit")
        sendmessage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sendmessage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 21))
        self.menubar.setObjectName("menubar")
        sendmessage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sendmessage)
        self.statusbar.setObjectName("statusbar")
        sendmessage.setStatusBar(self.statusbar)

        self.retranslateUi(sendmessage)
        QtCore.QMetaObject.connectSlotsByName(sendmessage)

    def retranslateUi(self, sendmessage):
        _translate = QtCore.QCoreApplication.translate
        sendmessage.setWindowTitle(_translate("sendmessage", "?????????????????? ??????????????????"))
        self.pushButton.setText(_translate("sendmessage", "??????????????????"))
        self.label.setText(_translate("sendmessage", "??????????????????"))
        self.label_2.setText(_translate("sendmessage", "????????????????????"))
        self.label_3.setText(_translate("sendmessage", "??????????????????"))
