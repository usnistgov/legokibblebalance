# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_weighmass.ui'
#
# Created: Fri Sep 23 15:57:11 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(340, 230)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(100, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.TXT_oncoil = QtWidgets.QLabel(self.centralwidget)
        self.TXT_oncoil.setObjectName(_fromUtf8("TXT_oncoil"))
        self.gridLayout.addWidget(self.TXT_oncoil, 0, 2, 1, 1)
        self.BTN_start = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_start.setObjectName(_fromUtf8("BTN_start"))
        self.gridLayout.addWidget(self.BTN_start, 0, 0, 1, 1)
        self.BTN_ZR1 = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_ZR1.setEnabled(False)
        self.BTN_ZR1.setObjectName(_fromUtf8("BTN_ZR1"))
        self.gridLayout.addWidget(self.BTN_ZR1, 1, 1, 1, 1)
        self.BTN_ZR2 = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_ZR2.setEnabled(False)
        self.BTN_ZR2.setObjectName(_fromUtf8("BTN_ZR2"))
        self.gridLayout.addWidget(self.BTN_ZR2, 3, 1, 1, 1)
        self.LCD_ZR1 = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_ZR1.setMinimumSize(QtCore.QSize(0, 30))
        self.LCD_ZR1.setObjectName(_fromUtf8("LCD_ZR1"))
        self.gridLayout.addWidget(self.LCD_ZR1, 1, 2, 1, 1)
        self.T_result = QtGui.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_result.sizePolicy().hasHeightForWidth())
        self.T_result.setSizePolicy(sizePolicy)
        self.T_result.setObjectName(_fromUtf8("T_result"))
        self.gridLayout.addWidget(self.T_result, 4, 0, 1, 3)
        self.LCD_WM = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_WM.setMinimumSize(QtCore.QSize(0, 30))
        self.LCD_WM.setObjectName(_fromUtf8("LCD_WM"))
        self.gridLayout.addWidget(self.LCD_WM, 2, 2, 1, 1)
        self.TXT_readyWM = QtWidgets.QLabel(self.centralwidget)
        self.TXT_readyWM.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(46, 194, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 194, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_readyWM.setPalette(palette)
        self.TXT_readyWM.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_readyWM.setObjectName(_fromUtf8("TXT_readyWM"))
        self.gridLayout.addWidget(self.TXT_readyWM, 2, 0, 1, 1)
        self.LCD_ZR2 = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_ZR2.setMinimumSize(QtCore.QSize(0, 30))
        self.LCD_ZR2.setObjectName(_fromUtf8("LCD_ZR2"))
        self.gridLayout.addWidget(self.LCD_ZR2, 3, 2, 1, 1)
        self.TXT_readyZR2 = QtWidgets.QLabel(self.centralwidget)
        self.TXT_readyZR2.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(46, 194, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 194, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_readyZR2.setPalette(palette)
        self.TXT_readyZR2.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_readyZR2.setObjectName(_fromUtf8("TXT_readyZR2"))
        self.gridLayout.addWidget(self.TXT_readyZR2, 3, 0, 1, 1)
        self.TXT_readyZR1 = QtWidgets.QLabel(self.centralwidget)
        self.TXT_readyZR1.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(46, 194, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 194, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_readyZR1.setPalette(palette)
        self.TXT_readyZR1.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_readyZR1.setObjectName(_fromUtf8("TXT_readyZR1"))
        self.gridLayout.addWidget(self.TXT_readyZR1, 1, 0, 1, 1)
        self.BTN_restart = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_restart.setEnabled(False)
        self.BTN_restart.setObjectName(_fromUtf8("BTN_restart"))
        self.gridLayout.addWidget(self.BTN_restart, 0, 1, 1, 1)
        self.BTN_WM = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_WM.setEnabled(False)
        self.BTN_WM.setObjectName(_fromUtf8("BTN_WM"))
        self.gridLayout.addWidget(self.BTN_WM, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Weigh Mass", None))
        self.TXT_oncoil.setText(_translate("MainWindow", "Measured Current:", None))
        self.BTN_start.setText(_translate("MainWindow", "Start", None))
        self.BTN_ZR1.setText(_translate("MainWindow", "Zero Reading", None))
        self.BTN_ZR2.setText(_translate("MainWindow", "Zero Reading", None))
        self.T_result.setPlainText(_translate("MainWindow", "Press Start Measurement!", None))
        self.TXT_readyWM.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">READY</span></p></body></html>", None))
        self.TXT_readyZR2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">READY</span></p></body></html>", None))
        self.TXT_readyZR1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">READY</span></p></body></html>", None))
        self.BTN_restart.setText(_translate("MainWindow", "Restart", None))
        self.BTN_WM.setText(_translate("MainWindow", "Weigh Mass", None))

