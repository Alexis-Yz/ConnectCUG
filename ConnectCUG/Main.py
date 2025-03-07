# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(500, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setMinimumSize(QtCore.QSize(500, 500))
        Main.setMaximumSize(QtCore.QSize(500, 500))
        self.gridLayout_2 = QtWidgets.QGridLayout(Main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Main)
        self.groupBox_2.setMinimumSize(QtCore.QSize(191, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_ip = QtWidgets.QLabel(self.groupBox_2)
        self.label_ip.setGeometry(QtCore.QRect(80, 20, 101, 16))
        self.label_ip.setObjectName("label_ip")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_status = QtWidgets.QLabel(self.groupBox_2)
        self.label_status.setGeometry(QtCore.QRect(80, 50, 101, 16))
        self.label_status.setObjectName("label_status")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(80, 80, 101, 16))
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Main)
        self.groupBox.setMinimumSize(QtCore.QSize(181, 111))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 31, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 50, 141, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(50, 80, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 80, 91, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Main)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(Main)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 70))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 70))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 2)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "CUG自动连网 v1.0.0"))
        self.groupBox_2.setTitle(_translate("Main", "当前状态"))
        self.label_3.setText(_translate("Main", "IP地址"))
        self.label_ip.setText(_translate("Main", "0.0.0.0"))
        self.label_4.setText(_translate("Main", "网络状态"))
        self.label_status.setText(_translate("Main", "未接到连网络"))
        self.label_5.setText(_translate("Main", "网络类型"))
        self.label_7.setText(_translate("Main", "无"))
        self.groupBox.setTitle(_translate("Main", "用户信息"))
        self.label.setText(_translate("Main", "学号"))
        self.label_2.setText(_translate("Main", "密码"))
        self.pushButton.setText(_translate("Main", "登录"))
        self.pushButton_2.setText(_translate("Main", "释放登录按钮"))
        self.groupBox_3.setTitle(_translate("Main", "日志输出"))
        self.textEdit.setHtml(_translate("Main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">CUG校园网专用，请勿滥用</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">初次使用请管理员模式运行并手动登录账号</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">初次运行后，程序后续会开机自启并自动登录账号</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">程序生成的info.txt和run_connectCUG_admin.bat勿删除</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">有问题请联系zyue@163.com</span></p></body></html>"))
