# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_dataAcqSettings.ui'
#
# Created: Thu Mar 02 18:00:55 2017
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
        MainWindow.resize(483, 249)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.TB_samprate = QtGui.QSpinBox(self.centralwidget)
        self.TB_samprate.setGeometry(QtCore.QRect(140, 50, 101, 31))
        self.TB_samprate.setMaximum(999999999)
        self.TB_samprate.setObjectName(_fromUtf8("TB_samprate"))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.TB_length = QtGui.QSpinBox(self.centralwidget)
        self.TB_length.setGeometry(QtCore.QRect(140, 90, 101, 31))
        self.TB_length.setMaximum(999999999)
        self.TB_length.setObjectName(_fromUtf8("TB_length"))
        self.LCD_totalSamprate = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_totalSamprate.setGeometry(QtCore.QRect(390, 50, 81, 31))
        self.LCD_totalSamprate.setObjectName(_fromUtf8("LCD_totalSamprate"))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 50, 121, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 90, 121, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 130, 121, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.LCD_TrueSampleDt = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_TrueSampleDt.setGeometry(QtCore.QRect(390, 90, 81, 31))
        self.LCD_TrueSampleDt.setObjectName(_fromUtf8("LCD_TrueSampleDt"))
        self.LCD_dt = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_dt.setGeometry(QtCore.QRect(390, 130, 81, 31))
        self.LCD_dt.setObjectName(_fromUtf8("LCD_dt"))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 121, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.TB_maxlen = QtGui.QSpinBox(self.centralwidget)
        self.TB_maxlen.setGeometry(QtCore.QRect(140, 170, 101, 31))
        self.TB_maxlen.setMaximum(999999999)
        self.TB_maxlen.setObjectName(_fromUtf8("TB_maxlen"))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 170, 121, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.LCD_callbacksPerPeriod = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_callbacksPerPeriod.setGeometry(QtCore.QRect(390, 170, 81, 31))
        self.LCD_callbacksPerPeriod.setObjectName(_fromUtf8("LCD_callbacksPerPeriod"))
        self.BTN_saverestart = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_saverestart.setGeometry(QtCore.QRect(110, 210, 231, 31))
        self.BTN_saverestart.setObjectName(_fromUtf8("BTN_saverestart"))
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 461, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_8.setPalette(palette)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 130, 121, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.TB_buffersize = QtGui.QSpinBox(self.centralwidget)
        self.TB_buffersize.setGeometry(QtCore.QRect(140, 130, 101, 31))
        self.TB_buffersize.setMaximum(999999999)
        self.TB_buffersize.setObjectName(_fromUtf8("TB_buffersize"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Data acquisition settings", None))
        self.label.setText(_translate("MainWindow", "Samplerate per channel", None))
        self.label_2.setText(_translate("MainWindow", "Samples per channel", None))
        self.label_3.setText(_translate("MainWindow", "Overall samplerate", None))
        self.label_4.setText(_translate("MainWindow", "Time between samples", None))
        self.label_5.setText(_translate("MainWindow", "Time between callbacks", None))
        self.label_6.setText(_translate("MainWindow", "Saved seconds per chnl.", None))
        self.label_7.setText(_translate("MainWindow", "Callbacks per sine period", None))
        self.BTN_saverestart.setText(_translate("MainWindow", "Save values and restart program", None))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">CHANGING THESE VALUES REQUIRES A PROGRAM RESTART!!!</span></p></body></html>", None))
        self.label_9.setText(_translate("MainWindow", "Buffersize (Faktor)", None))

