# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zmaeyma_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zmeyka(object):
    def setupUi(self, Zmeyka):
        Zmeyka.setObjectName("Zmeyka")
        Zmeyka.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Zmeyka)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 420, 121, 71))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 280, 761, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 210, 271, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 0, 241, 121))
        self.label_2.setMinimumSize(QtCore.QSize(161, 121))
        self.label_2.setObjectName("label_2")
        Zmeyka.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Zmeyka)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Zmeyka.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Zmeyka)
        self.statusbar.setObjectName("statusbar")
        Zmeyka.setStatusBar(self.statusbar)

        self.retranslateUi(Zmeyka)
        QtCore.QMetaObject.connectSlotsByName(Zmeyka)

    def retranslateUi(self, Zmeyka):
        _translate = QtCore.QCoreApplication.translate
        Zmeyka.setWindowTitle(_translate("Zmeyka", "MainWindow"))
        self.pushButton_2.setText(_translate("Zmeyka", "НАЧАТЬ"))
        self.pushButton_4.setText(_translate("Zmeyka", "большой"))
        self.pushButton_3.setText(_translate("Zmeyka", "средний"))
        self.pushButton.setText(_translate("Zmeyka", "маленький"))
        self.label.setText(_translate("Zmeyka", "<html><head/><body><p><span style=\" font-size:18pt;\">Выберите размер поля:</span></p></body></html>"))
        self.label_2.setText(_translate("Zmeyka", "<html><head/><body><p><span style=\" font-size:48pt;\">ZMEYKA</span></p></body></html>"))