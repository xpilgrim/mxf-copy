# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mxf_copy_main.ui'
#
# Created: Wed Jun 20 22:17:02 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MxfCopyMain(object):
    def setupUi(self, MxfCopyMain):
        MxfCopyMain.setObjectName(_fromUtf8("MxfCopyMain"))
        MxfCopyMain.resize(649, 504)
        MxfCopyMain.setWindowTitle(QtGui.QApplication.translate("MxfCopyMain", "MXF-Copy-Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MxfCopyMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setText(QtGui.QApplication.translate("MxfCopyMain", "Quelle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_1.setText(QtGui.QApplication.translate("MxfCopyMain", "Quell-Ordner", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_1.setObjectName(_fromUtf8("lineEdit_1"))
        self.gridLayout.addWidget(self.lineEdit_1, 3, 0, 1, 1)
        self.toolButton_1 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_1.setToolTip(QtGui.QApplication.translate("MxfCopyMain", "Quellverzeichnis", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_1.setText(QtGui.QApplication.translate("MxfCopyMain", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_1.setObjectName(_fromUtf8("toolButton_1"))
        self.gridLayout.addWidget(self.toolButton_1, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setText(QtGui.QApplication.translate("MxfCopyMain", "Ziel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setText(QtGui.QApplication.translate("MxfCopyMain", "Ziel-Ordner", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 5, 0, 1, 1)
        self.toolButton_2 = QtGui.QToolButton(self.centralwidget)
        self.toolButton_2.setToolTip(QtGui.QApplication.translate("MxfCopyMain", "Zielverzeichnis", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("MxfCopyMain", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.gridLayout.addWidget(self.toolButton_2, 5, 1, 1, 1)
        self.label_1 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setText(QtGui.QApplication.translate("MxfCopyMain", "MXF-Copy-Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 8, 0, 1, 1)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setText(QtGui.QApplication.translate("MxfCopyMain", "Kopieren starten", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.gridLayout.addWidget(self.commandLinkButton, 8, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setText(QtGui.QApplication.translate("MxfCopyMain", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 9, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 9, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 7, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setText(QtGui.QApplication.translate("MxfCopyMain", "Prefix", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        MxfCopyMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MxfCopyMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MxfCopyMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MxfCopyMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MxfCopyMain.setStatusBar(self.statusbar)

        self.retranslateUi(MxfCopyMain)
        QtCore.QMetaObject.connectSlotsByName(MxfCopyMain)
        MxfCopyMain.setTabOrder(self.lineEdit_1, self.toolButton_1)
        MxfCopyMain.setTabOrder(self.toolButton_1, self.lineEdit_2)
        MxfCopyMain.setTabOrder(self.lineEdit_2, self.toolButton_2)

    def retranslateUi(self, MxfCopyMain):
        pass

