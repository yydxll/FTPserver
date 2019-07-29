# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Neusoft\python\untitle\more1\untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import tkinter as tk
from tkinter import filedialog
import socket
import threading

import ctypes
import inspect



try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    myaddr = s.getsockname()[0]
finally:
    s.close()



def FTPserver(loginame,yu,password,lujing):
# 新建一个用户组
    authorizer = DummyAuthorizer()
# 将用户名，密码，指定目录，权限 添加到里面
    authorizer.add_user(loginame, password, lujing, perm="elradmfw")  # adfmw
# 匿名用户
#     print(x.yu)
#     print(x.loginame)
#     print(x.password)
#     print(x.lujing)
    authorizer.add_anonymous(lujing,perm= yu)

    handler = FTPHandler
    handler.authorizer = authorizer
# 开启服务器
    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()


def _async_raise(tid, exctype):
   """raises the exception, performs cleanup if needed"""
   tid = ctypes.c_long(tid)
   if not inspect.isclass(exctype):
      exctype = type(exctype)
   res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
   if res == 0:
      raise ValueError("invalid thread id")
   elif res != 1:
      # """if it returns a number greater than one, you're in trouble,
      # and you should call it again with exc=NULL to revert the effect"""
      ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
      raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
   _async_raise(thread.ident, SystemExit)

class Ui_nihao(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_nihao, self).__init__()
        self.setObjectName("nihao")
        self.resize(400, 300)
        self.setWindowTitle("提示")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 80, 350, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("您已成功开启FTP服务！")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.yu = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 565)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(34, 450, 581, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)




        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.setEnabled(False)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 340, 306, 89))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 241, 157))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.radioButton)

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_11)

        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(420, 50, 160, 83))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 200, 201, 231))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 181, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)



        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)



        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 230, 171, 51))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "启动FTPserver"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭服务"))
        self.pushButton.setText(_translate("MainWindow", "退出系统"))

        self.pushButton.clicked.connect(self.on_push_button_1_clicked)
        self.pushButton_2.clicked.connect(self.on_push_button_2_clicked)
        self.pushButton_3.clicked.connect(self.on_push_button_3_clicked)

        self.radioButton.toggled.connect(lambda: self.btnstate(self.radioButton))
        self.label.setText(_translate("MainWindow", "文件路径"))
        self.pushButton_4.setText(_translate("MainWindow", "。。。"))
        self.pushButton_4.clicked.connect(self.on_push_button_4_clicked)

        self.label_5.setText(_translate("MainWindow", "账户名称"))
        self.label_2.setText(_translate("MainWindow", "账户密码"))
        self.label_6.setText(_translate("MainWindow", "侦听端口"))
        self.label_7.setText(_translate("MainWindow", "最大连接"))
        self.label_11.setText(_translate("MainWindow", "本机ip"))
        self.label_4.setText(_translate("MainWindow", "沈阳工业大学软件学院"))
        self.label_8.setText(_translate("MainWindow", "计算机科学与技术专业"))
        self.label_10.setText(_translate("MainWindow", "指导教师：翟治安"))
        self.label_9.setText(_translate("MainWindow", "作者：张家瑞"))
        numnum='100'
        self.spinBox.setSpecialValueText(_translate("MainWindow", numnum))

        self.radioButton.setText(_translate("MainWindow", "仅允许匿名登陆"))
        self.groupBox.setTitle(_translate("MainWindow", "       用户权限"))


        self.checkBox.setText(_translate("MainWindow", "上传文件"))
        self.checkBox_3.setText(_translate("MainWindow", "创建文件"))
        self.checkBox_2.setText(_translate("MainWindow", "删除文件"))
        self.checkBox_4.setText(_translate("MainWindow", "重命名文件"))
        self.checkBox_5.setText(_translate("MainWindow", "写入文件"))

        self.checkBox.setChecked(True)  # 该复选框是否勾选,select为勾选, deselect为不勾选
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.setChecked(True)
        self.checkBox_5.setChecked(True)
        self.radioButton.setChecked(True)


        loginame = 'anonymity'
        self.lineEdit.setText(_translate("MainWindow", loginame))
        self.loginame = loginame
        password = ''
        lujing='D:/'
        self.lineEdit_5.setText(_translate("MainWindow", lujing))
        self.lujing = lujing


        self.lineEdit_2.setText(_translate("MainWindow", password))
        self.password = password
        self.lineEdit_3.setText(_translate("MainWindow", "21"))

        self.label_3.setText(_translate("MainWindow", "NEUEDU东软睿道"))
        self.lineEdit_4.setText(_translate("MainWindow", myaddr))
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.label_5.setEnabled(False)
        self.label_2.setEnabled(False)

        # chk1Status = self.checkBox.text() + ", isChecked=" + str(self.checkBox.isChecked()) + ', chekState=' + str(self.checkBox.checkState()) + "\n"
        # chk1Status1 = self.checkBox_3.text() + ", isChecked=" + str(self.checkBox_3.isChecked()) + ', chekState=' + str(self.checkBox_3.checkState()) + "\n"

        # print(chk1Status)
        # print(chk1Status1)

    # a
    # 文件上传
    # d
    # 删除文件
    # f
    # 文件重命名
    # m
    # 创建文件
    # w
    # 写权限
    def checkbox(self):
        quanxian = 'elr'

        if self.checkBox.isChecked()==True:
            quanxian+='a'

        if self.checkBox_3.isChecked()==True:
            quanxian += 'd'

        if self.checkBox_2.isChecked()==True:
            quanxian += 'm'
        if self.checkBox_4.isChecked()==True:
            quanxian += 'f'
        if self.checkBox_5.isChecked()==True:
            quanxian += 'w'
        self.yu = quanxian




    def on_push_button_1_clicked(self):#退出系统
        exit()

    def on_push_button_3_clicked(self):
        #FTPserver(self)
        self.t2 = threading.Thread(target=FTPserver,args=(self.loginame,self.yu,self.password,self.lujing))  # 生成一个线程实例
        self.t2.start()
        # self.haoN = Ui_nihao()
        # self.haoN.show()
        self.pushButton_3.setEnabled(False)
        self.pushButton_2.setEnabled(True)

    def on_push_button_2_clicked(self):
        stop_thread(self.t2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(True)


    def on_push_button_4_clicked(self):

        _translate = QtCore.QCoreApplication.translate

        '''打开选择文件夹对话框'''
        root = tk.Tk()
        root.withdraw()

        Folderpath = filedialog.askdirectory()  # 获得选择好的文件夹

        lujing = str(Folderpath)
        self.lineEdit_5.setText(_translate("MainWindow", lujing))
        self.lujing = lujing

    def btnstate(self,btn):
        if btn.isChecked() == True:
            self.lineEdit.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.label_5.setEnabled(False)
            self.label_2.setEnabled(False)
        else:
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.label_5.setEnabled(True)
            self.label_2.setEnabled(True)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.showMenu()
        self.other()

    def showMenu(self):
        "设计托盘的菜单，这里我实现了一个二级菜单"
        self.menu = QMenu()
        self.menu1 = QMenu()

        self.quitAction = QAction("退出", self, triggered=self.quit)
        self.menu1.addAction("联系方式")
        self.menu1.addAction("18740058827")
        self.menu.addMenu(self.menu1, )


        self.menu.addAction(self.quitAction)
        self.menu1.setTitle("help")
        self.setContextMenu(self.menu)

        # Ui_MainWindow().on_push_button_3_clicked


    def other(self):
        self.activated.connect(self.iconClied)
        # 把鼠标点击图标的信号和槽连接
        self.messageClicked.connect(self.mClied)
        # 把鼠标点击弹出消息的信号和槽连接
        self.setIcon(QIcon("p1_jump.png"))
        self.icon = self.MessageIcon()
        # 设置图标

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        # print(reason)

    def mClied(self):
        self.showMessage("提示", "你点了消息", self.icon)

    def showM(self):

        self.showMessage("测试", "我是消息", self.icon)

    def quit(self):
        "保险起见，为了完整的退出"
        self.setVisible(False)
        self.parent().exit()
        qApp.quit()
        sys.exit()



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.checkbox()

        ti = TrayIcon(self)
        ti.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.setWindowFlags(Qt.Tool)

    myWin.show()


    sys.exit(app.exec_())
