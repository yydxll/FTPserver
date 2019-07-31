# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget(1).ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(511, 446)
        self.ID = QtWidgets.QLabel(Widget)
        self.ID.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.ID.setStyleSheet("font: 75 9pt \"华文楷体\";\n"
"font: 75 12pt \"华文楷体\";")
        self.ID.setObjectName("ID")
        self.port = QtWidgets.QLabel(Widget)
        self.port.setGeometry(QtCore.QRect(30, 80, 72, 21))
        self.port.setStyleSheet("font: 75 9pt \"华文楷体\";\n"
"font: 75 12pt \"华文楷体\";")
        self.port.setObjectName("port")
        self.name = QtWidgets.QLabel(Widget)
        self.name.setGeometry(QtCore.QRect(30, 120, 72, 15))
        self.name.setStyleSheet("font: 75 12pt \"华文楷体\";")
        self.name.setObjectName("name")
        self.passwd = QtWidgets.QLabel(Widget)
        self.passwd.setGeometry(QtCore.QRect(40, 190, 41, 21))
        self.passwd.setStyleSheet("font: 75 12pt \"华文楷体\";")
        self.passwd.setObjectName("passwd")
        self.ID_2 = QtWidgets.QLineEdit(Widget)
        self.ID_2.setGeometry(QtCore.QRect(100, 40, 131, 21))
        self.ID_2.setObjectName("ID_2")
        self.port_2 = QtWidgets.QLineEdit(Widget)
        self.port_2.setGeometry(QtCore.QRect(100, 80, 131, 21))
        self.port_2.setText("")
        self.port_2.setObjectName("port_2")
        self.name_2 = QtWidgets.QLineEdit(Widget)
        self.name_2.setGeometry(QtCore.QRect(100, 120, 131, 21))
        self.name_2.setObjectName("name_2")
        self.passwd_2 = QtWidgets.QLineEdit(Widget)
        self.passwd_2.setGeometry(QtCore.QRect(100, 190, 131, 21))
        self.passwd_2.setObjectName("passwd_2")
        self.startButton = QtWidgets.QPushButton(Widget)
        self.startButton.setGeometry(QtCore.QRect(20, 380, 191, 29))
        self.startButton.setStyleSheet("font: 75 11pt \"华文楷体\";")
        self.startButton.setObjectName("startButton")
        self.closeButton_2 = QtWidgets.QPushButton(Widget)
        self.closeButton_2.setGeometry(QtCore.QRect(280, 380, 191, 29))
        self.closeButton_2.setStyleSheet("font: 75 11pt \"华文楷体\";")
        self.closeButton_2.setObjectName("closeButton_2")
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(40, 260, 131, 31))
        self.label.setStyleSheet("font: 9pt \"华文楷体\";\n"
"font: 75 11pt \"华文楷体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(40, 230, 61, 21))
        self.label_2.setStyleSheet("font: 75 12pt \"华文楷体\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 230, 131, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.fileload = QtWidgets.QPushButton(Widget)
        self.fileload.setGeometry(QtCore.QRect(240, 220, 41, 41))
        self.fileload.setAcceptDrops(True)
        self.fileload.setAutoFillBackground(False)
        self.fileload.setStyleSheet("border-image: url(:/文件.jpg);")
        self.fileload.setText("")
        self.fileload.setObjectName("fileload")
        self.fileUp = QtWidgets.QCheckBox(Widget)
        self.fileUp.setGeometry(QtCore.QRect(210, 300, 165, 24))
        self.fileUp.setStyleSheet("font: 75 11pt \"华文楷体\";")
        self.fileUp.setObjectName("fileUp")
        self.filecreate = QtWidgets.QCheckBox(Widget)
        self.filecreate.setGeometry(QtCore.QRect(50, 300, 509, 24))
        self.filecreate.setStyleSheet("font: 75 11pt \"华文楷体\";")
        self.filecreate.setObjectName("filecreate")
        self.filedelete = QtWidgets.QCheckBox(Widget)
        self.filedelete.setGeometry(QtCore.QRect(380, 300, 251, 24))
        self.filedelete.setStyleSheet("font: 75 11pt \"华文楷体\";")
        self.filedelete.setObjectName("filedelete")
        self.filerename = QtWidgets.QCheckBox(Widget)
        self.filerename.setGeometry(QtCore.QRect(210, 340, 111, 24))
        self.filerename.setStyleSheet("font: 75 11pt \"华文楷体\";")
        self.filerename.setObjectName("filerename")
        self.checkBox_5 = QtWidgets.QCheckBox(Widget)
        self.checkBox_5.setGeometry(QtCore.QRect(50, 340, 151, 24))
        self.checkBox_5.setStyleSheet("font: 75 11pt \"华文楷体\";")
        self.checkBox_5.setObjectName("checkBox_5")
        self.noname = QtWidgets.QRadioButton(Widget)
        self.noname.setGeometry(QtCore.QRect(100, 160, 115, 19))
        self.noname.setStyleSheet("font: 75 10pt \"华文楷体\";")
        self.noname.setObjectName("noname")
        self.textEdit = QtWidgets.QTextEdit(Widget)
        self.textEdit.setGeometry(QtCore.QRect(280, 70, 191, 81))
        self.textEdit.setStyleSheet("font: 75 12pt \"华文楷体\";\n"
"background-color: rgb(240, 240, 240);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Widget)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 170, 161, 41))
        self.textEdit_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.ID.setText(_translate("Widget", "本机ID"))
        self.port.setText(_translate("Widget", "端口号"))
        self.name.setText(_translate("Widget", "用户名"))
        self.passwd.setText(_translate("Widget", "密码"))
        self.name_2.setText(_translate("Widget", "root"))
        self.startButton.setText(_translate("Widget", "启动服务"))
        self.closeButton_2.setText(_translate("Widget", "终止服务"))
        self.label.setText(_translate("Widget", "用户权限："))
        self.label_2.setText(_translate("Widget", "路径"))
        self.fileUp.setText(_translate("Widget", "上传文件"))
        self.filecreate.setText(_translate("Widget", "创建文件"))
        self.filedelete.setText(_translate("Widget", "删除文件"))
        self.filerename.setText(_translate("Widget", "重命名文件"))
        self.checkBox_5.setText(_translate("Widget", "写入文件"))
        self.noname.setText(_translate("Widget", "匿名登陆"))
        self.textEdit.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文楷体\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:400;\">东软睿道</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:400;\">沈阳工业大学</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-weight:400;\">指导教师：翟治安</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic;\">FTPServer</span></p></body></html>"))

