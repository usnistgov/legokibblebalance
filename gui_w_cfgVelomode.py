# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_cfgVelomode.ui'
#
# Created: Thu Sep 29 16:17:07 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

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
        MainWindow.resize(549, 376)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.PW_sine = PlotWidget(self.centralwidget)
        self.PW_sine.setGeometry(QtCore.QRect(10, 10, 531, 131))
        self.PW_sine.setObjectName(_fromUtf8("PW_sine"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 281, 211))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.TB_I_velo = QtGui.QDoubleSpinBox(self.groupBox)
        self.TB_I_velo.setGeometry(QtCore.QRect(110, 29, 71, 31))
        self.TB_I_velo.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_I_velo.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.TB_I_velo.setKeyboardTracking(False)
        self.TB_I_velo.setDecimals(2)
        self.TB_I_velo.setMinimum(-1000.0)
        self.TB_I_velo.setMaximum(1000.0)
        self.TB_I_velo.setObjectName(_fromUtf8("TB_I_velo"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(140, 10, 16, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(50, 10, 16, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(230, 10, 16, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.TB_P_velo = QtGui.QDoubleSpinBox(self.groupBox)
        self.TB_P_velo.setGeometry(QtCore.QRect(20, 29, 71, 31))
        self.TB_P_velo.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_P_velo.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.TB_P_velo.setKeyboardTracking(False)
        self.TB_P_velo.setDecimals(2)
        self.TB_P_velo.setMinimum(-1000.0)
        self.TB_P_velo.setMaximum(1000.0)
        self.TB_P_velo.setObjectName(_fromUtf8("TB_P_velo"))
        self.TB_D_velo = QtGui.QDoubleSpinBox(self.groupBox)
        self.TB_D_velo.setGeometry(QtCore.QRect(200, 30, 71, 31))
        self.TB_D_velo.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_D_velo.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.TB_D_velo.setKeyboardTracking(False)
        self.TB_D_velo.setDecimals(2)
        self.TB_D_velo.setMinimum(-1000.0)
        self.TB_D_velo.setMaximum(1000.0)
        self.TB_D_velo.setObjectName(_fromUtf8("TB_D_velo"))
        self.BTN_savePIDvelo = QtGui.QPushButton(self.groupBox)
        self.BTN_savePIDvelo.setGeometry(QtCore.QRect(60, 70, 75, 23))
        self.BTN_savePIDvelo.setObjectName(_fromUtf8("BTN_savePIDvelo"))
        self.BTN_loadPIDvelo = QtGui.QPushButton(self.groupBox)
        self.BTN_loadPIDvelo.setGeometry(QtCore.QRect(160, 70, 75, 23))
        self.BTN_loadPIDvelo.setObjectName(_fromUtf8("BTN_loadPIDvelo"))
        self.LCD_eps = QtGui.QLCDNumber(self.groupBox)
        self.LCD_eps.setGeometry(QtCore.QRect(110, 140, 161, 31))
        self.LCD_eps.setNumDigits(10)
        self.LCD_eps.setObjectName(_fromUtf8("LCD_eps"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 81, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.LCD_su = QtGui.QLCDNumber(self.groupBox)
        self.LCD_su.setGeometry(QtCore.QRect(110, 110, 161, 31))
        self.LCD_su.setNumDigits(10)
        self.LCD_su.setObjectName(_fromUtf8("LCD_su"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 81, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.LCD_output = QtGui.QLCDNumber(self.groupBox)
        self.LCD_output.setGeometry(QtCore.QRect(110, 170, 161, 31))
        self.LCD_output.setNumDigits(10)
        self.LCD_output.setObjectName(_fromUtf8("LCD_output"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 180, 81, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 150, 241, 211))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.BTN_saveAF = QtGui.QPushButton(self.groupBox_3)
        self.BTN_saveAF.setGeometry(QtCore.QRect(20, 140, 201, 23))
        self.BTN_saveAF.setObjectName(_fromUtf8("BTN_saveAF"))
        self.LCD_validRange = QtGui.QLCDNumber(self.groupBox_3)
        self.LCD_validRange.setGeometry(QtCore.QRect(130, 100, 91, 31))
        self.LCD_validRange.setNumDigits(5)
        self.LCD_validRange.setObjectName(_fromUtf8("LCD_validRange"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 81, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.TB_freq = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.TB_freq.setGeometry(QtCore.QRect(20, 40, 81, 31))
        self.TB_freq.setDecimals(2)
        self.TB_freq.setMinimum(0.01)
        self.TB_freq.setMaximum(99.99)
        self.TB_freq.setProperty("value", 1.0)
        self.TB_freq.setObjectName(_fromUtf8("TB_freq"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 61, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(110, 70, 121, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.TB_amp = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.TB_amp.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.TB_amp.setDecimals(3)
        self.TB_amp.setMinimum(-10.0)
        self.TB_amp.setMaximum(10.0)
        self.TB_amp.setSingleStep(0.1)
        self.TB_amp.setProperty("value", 0.2)
        self.TB_amp.setObjectName(_fromUtf8("TB_amp"))
        self.LCD_period = QtGui.QLCDNumber(self.groupBox_3)
        self.LCD_period.setGeometry(QtCore.QRect(130, 40, 91, 31))
        self.LCD_period.setNumDigits(3)
        self.LCD_period.setObjectName(_fromUtf8("LCD_period"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.BTN_loadAF = QtGui.QPushButton(self.groupBox_3)
        self.BTN_loadAF.setGeometry(QtCore.QRect(20, 170, 201, 23))
        self.BTN_loadAF.setObjectName(_fromUtf8("BTN_loadAF"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Configure velocity mode", None))
        self.groupBox.setTitle(_translate("MainWindow", "Configure velocity PID", None))
        self.label_6.setText(_translate("MainWindow", "I", None))
        self.label_10.setText(_translate("MainWindow", "P", None))
        self.label_11.setText(_translate("MainWindow", "D", None))
        self.BTN_savePIDvelo.setText(_translate("MainWindow", "Save", None))
        self.BTN_loadPIDvelo.setText(_translate("MainWindow", "Load", None))
        self.label_9.setText(_translate("MainWindow", "Epsilon:", None))
        self.label_7.setText(_translate("MainWindow", "Integrator sum:", None))
        self.label_13.setText(_translate("MainWindow", "Output:", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sine Curve", None))
        self.BTN_saveAF.setText(_translate("MainWindow", "Save Amplitude and Frequency", None))
        self.label_2.setText(_translate("MainWindow", "Amplitude in mm:", None))
        self.label_5.setText(_translate("MainWindow", "Period in s:", None))
        self.label_12.setText(_translate("MainWindow", "Maximal Amplitude in mm:", None))
        self.label.setText(_translate("MainWindow", "Frequency in Hz:", None))
        self.BTN_loadAF.setText(_translate("MainWindow", "Load Amplitude and Frequency", None))

from pyqtgraph import PlotWidget