# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Thu Apr  6 19:17:50 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(490, 146)
        MainWindow.setMinimumSize(QtCore.QSize(490, 146))
        MainWindow.setMaximumSize(QtCore.QSize(490, 146))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 321, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.selectFileLable = QtGui.QLabel(self.horizontalLayoutWidget)
        self.selectFileLable.setObjectName(_fromUtf8("selectFileLable"))
        self.horizontalLayout.addWidget(self.selectFileLable)
        self.selectFilePath = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.selectFilePath.setObjectName(_fromUtf8("selectFilePath"))
        self.horizontalLayout.addWidget(self.selectFilePath)
        self.selectFileButton = QtGui.QToolButton(self.horizontalLayoutWidget)
        self.selectFileButton.setObjectName(_fromUtf8("selectFileButton"))
        self.horizontalLayout.addWidget(self.selectFileButton)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(370, 20, 93, 95))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.yesButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.yesButton.setObjectName(_fromUtf8("yesButton"))
        self.verticalLayout_2.addWidget(self.yesButton)
        self.cancelButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.verticalLayout_2.addWidget(self.cancelButton)
        self.translate = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.translate.setObjectName(_fromUtf8("translate"))
        self.verticalLayout_2.addWidget(self.translate)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 70, 321, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.selectInfoLable = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.selectInfoLable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.selectInfoLable.setAutoFillBackground(False)
        self.selectInfoLable.setObjectName(_fromUtf8("selectInfoLable"))
        self.horizontalLayout_2.addWidget(self.selectInfoLable)
        self.selectInfoCombo = QtGui.QComboBox(self.horizontalLayoutWidget_2)
        self.selectInfoCombo.setObjectName(_fromUtf8("selectInfoCombo"))
        self.selectInfoCombo.addItem(_fromUtf8(""))
        self.selectInfoCombo.addItem(_fromUtf8(""))
        self.selectInfoCombo.addItem(_fromUtf8(""))
        self.selectInfoCombo.addItem(_fromUtf8(""))
        self.selectInfoCombo.addItem(_fromUtf8(""))
        self.selectInfoCombo.addItem(_fromUtf8(""))
        self.selectInfoCombo.addItem(_fromUtf8(""))
        self.selectInfoCombo.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.selectInfoCombo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "音乐信息提取", None))
        self.selectFileLable.setText(_translate("MainWindow", "选择文件", None))
        self.selectFileButton.setText(_translate("MainWindow", "...", None))
        self.yesButton.setText(_translate("MainWindow", "确定", None))
        self.cancelButton.setText(_translate("MainWindow", "取消", None))
        self.translate.setText(_translate("MainWindow", "mp3转wav", None))
        self.selectInfoLable.setText(_translate("MainWindow", "选择显示的信息", None))
        self.selectInfoCombo.setItemText(0, _translate("MainWindow", "MFCC", None))
        self.selectInfoCombo.setItemText(1, _translate("MainWindow", "MFCC_D1", None))
        self.selectInfoCombo.setItemText(2, _translate("MainWindow", "LPC", None))
        self.selectInfoCombo.setItemText(3, _translate("MainWindow", "ZCR", None))
        self.selectInfoCombo.setItemText(4, _translate("MainWindow", "Energy", None))
        self.selectInfoCombo.setItemText(5, _translate("MainWindow", "Sharpness", None))
        self.selectInfoCombo.setItemText(6, _translate("MainWindow", "SpectralRolloff", None))
        self.selectInfoCombo.setItemText(7, _translate("MainWindow", "spectralFlatness", None))

