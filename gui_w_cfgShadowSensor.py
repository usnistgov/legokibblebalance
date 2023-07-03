# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_cfgShadowSensor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 153)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.T_instructions = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.T_instructions.setGeometry(QtCore.QRect(10, 10, 321, 61))
        self.T_instructions.setObjectName("T_instructions")
        self.LCD_oldZeropos = QtWidgets.QLCDNumber(self.centralwidget)
        self.LCD_oldZeropos.setGeometry(QtCore.QRect(120, 100, 101, 31))
        self.LCD_oldZeropos.setDigitCount(8)
        self.LCD_oldZeropos.setObjectName("LCD_oldZeropos")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(230, 80, 71, 20))
        self.label_10.setObjectName("label_10")
        self.TB_photooffsetChange = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.TB_photooffsetChange.setEnabled(True)
        self.TB_photooffsetChange.setGeometry(QtCore.QRect(230, 100, 101, 31))
        self.TB_photooffsetChange.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.TB_photooffsetChange.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_photooffsetChange.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.TB_photooffsetChange.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.TB_photooffsetChange.setKeyboardTracking(False)
        self.TB_photooffsetChange.setDecimals(5)
        self.TB_photooffsetChange.setMinimum(-10.0)
        self.TB_photooffsetChange.setMaximum(10.0)
        self.TB_photooffsetChange.setSingleStep(0.001)
        self.TB_photooffsetChange.setProperty("value", 0.0)
        self.TB_photooffsetChange.setObjectName("TB_photooffsetChange")
        self.LCD_InputVoltage = QtWidgets.QLCDNumber(self.centralwidget)
        self.LCD_InputVoltage.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.LCD_InputVoltage.setSmallDecimalPoint(False)
        self.LCD_InputVoltage.setDigitCount(7)
        self.LCD_InputVoltage.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.LCD_InputVoltage.setObjectName("LCD_InputVoltage")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(120, 80, 61, 21))
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calibrate Zero-Position"))
        self.T_instructions.setPlainText(_translate("MainWindow", "Bring the balance to the center\n"
"(with your hands).\n"
"Enter the measured value as  new Photoffset"))
        self.label_10.setText(_translate("MainWindow", "New Photooffset:"))
        self.label_12.setText(_translate("MainWindow", "Input Voltage:"))
        self.label_13.setText(_translate("MainWindow", "Photooffset:"))

