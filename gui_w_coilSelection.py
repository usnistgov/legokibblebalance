# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_coilSelection.ui'
#
# Created: Fri Sep 23 09:59:55 2016
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.resize(273, 68)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.TXT_activecoil = QtGui.QLabel(self.centralwidget)
        self.TXT_activecoil.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_activecoil.setObjectName(_fromUtf8("TXT_activecoil"))
        self.gridLayout.addWidget(self.TXT_activecoil, 1, 0, 1, 2)
        self.BTN_useCoilA = QtGui.QPushButton(self.centralwidget)
        self.BTN_useCoilA.setObjectName(_fromUtf8("BTN_useCoilA"))
        self.gridLayout.addWidget(self.BTN_useCoilA, 2, 0, 1, 1)
        self.BTN_useCoilB = QtGui.QPushButton(self.centralwidget)
        self.BTN_useCoilB.setObjectName(_fromUtf8("BTN_useCoilB"))
        self.gridLayout.addWidget(self.BTN_useCoilB, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Coil Selection", None))
        self.TXT_activecoil.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Active: Coil X</span></p></body></html>", None))
        self.BTN_useCoilA.setText(_translate("MainWindow", "Use coil A", None))
        self.BTN_useCoilB.setText(_translate("MainWindow", "Use coil B", None))

