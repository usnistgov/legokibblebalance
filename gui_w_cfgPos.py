# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_cfgPos.ui'
#
# Created: Thu Sep 29 18:11:17 2016
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
        MainWindow.resize(677, 437)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 331, 201))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.BTN_start = QtGui.QPushButton(self.groupBox_2)
        self.BTN_start.setGeometry(QtCore.QRect(10, 20, 151, 23))
        self.BTN_start.setObjectName(_fromUtf8("BTN_start"))
        self.T_Instructions = QtGui.QPlainTextEdit(self.groupBox_2)
        self.T_Instructions.setGeometry(QtCore.QRect(10, 50, 311, 101))
        self.T_Instructions.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T_Instructions.setReadOnly(True)
        self.T_Instructions.setObjectName(_fromUtf8("T_Instructions"))
        self.BTN_confirm = QtGui.QPushButton(self.groupBox_2)
        self.BTN_confirm.setEnabled(False)
        self.BTN_confirm.setGeometry(QtCore.QRect(190, 160, 131, 31))
        self.BTN_confirm.setObjectName(_fromUtf8("BTN_confirm"))
        self.TXT_ready = QtGui.QLabel(self.groupBox_2)
        self.TXT_ready.setEnabled(False)
        self.TXT_ready.setGeometry(QtCore.QRect(110, 170, 61, 31))
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
        self.TXT_ready.setPalette(palette)
        self.TXT_ready.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_ready.setObjectName(_fromUtf8("TXT_ready"))
        self.TXT_wait = QtGui.QLabel(self.groupBox_2)
        self.TXT_wait.setEnabled(True)
        self.TXT_wait.setGeometry(QtCore.QRect(100, 150, 71, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_wait.setPalette(palette)
        self.TXT_wait.setInputMethodHints(QtCore.Qt.ImhNone)
        self.TXT_wait.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_wait.setObjectName(_fromUtf8("TXT_wait"))
        self.TB_value = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.TB_value.setEnabled(False)
        self.TB_value.setGeometry(QtCore.QRect(10, 160, 81, 31))
        self.TB_value.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.TB_value.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_value.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.TB_value.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.TB_value.setKeyboardTracking(False)
        self.TB_value.setMinimum(-1.0)
        self.TB_value.setMaximum(1000000000.0)
        self.TB_value.setProperty("value", -1.0)
        self.TB_value.setObjectName(_fromUtf8("TB_value"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(350, 10, 321, 201))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.T_points = QtGui.QPlainTextEdit(self.groupBox_3)
        self.T_points.setGeometry(QtCore.QRect(10, 20, 191, 121))
        self.T_points.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T_points.setReadOnly(True)
        self.T_points.setObjectName(_fromUtf8("T_points"))
        self.TB_degree = QtGui.QSpinBox(self.groupBox_3)
        self.TB_degree.setEnabled(False)
        self.TB_degree.setGeometry(QtCore.QRect(210, 30, 101, 31))
        self.TB_degree.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.TB_degree.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_degree.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.TB_degree.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToNearestValue)
        self.TB_degree.setKeyboardTracking(False)
        self.TB_degree.setMinimum(-1)
        self.TB_degree.setMaximum(999999999)
        self.TB_degree.setProperty("value", -1)
        self.TB_degree.setObjectName(_fromUtf8("TB_degree"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(210, 10, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.BTN_fit = QtGui.QPushButton(self.groupBox_3)
        self.BTN_fit.setEnabled(False)
        self.BTN_fit.setGeometry(QtCore.QRect(210, 70, 101, 31))
        self.BTN_fit.setObjectName(_fromUtf8("BTN_fit"))
        self.BTN_savefit = QtGui.QPushButton(self.groupBox_3)
        self.BTN_savefit.setEnabled(False)
        self.BTN_savefit.setGeometry(QtCore.QRect(210, 110, 101, 31))
        self.BTN_savefit.setObjectName(_fromUtf8("BTN_savefit"))
        self.T_fitresult = QtGui.QPlainTextEdit(self.groupBox_3)
        self.T_fitresult.setGeometry(QtCore.QRect(10, 150, 301, 41))
        self.T_fitresult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T_fitresult.setReadOnly(True)
        self.T_fitresult.setObjectName(_fromUtf8("T_fitresult"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 210, 661, 221))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.PW_fits = PlotWidget(self.groupBox_4)
        self.PW_fits.setGeometry(QtCore.QRect(10, 40, 641, 171))
        self.PW_fits.setObjectName(_fromUtf8("PW_fits"))
        self.TXT_calculatedfit = QtGui.QLabel(self.groupBox_4)
        self.TXT_calculatedfit.setGeometry(QtCore.QRect(10, 20, 81, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_calculatedfit.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TXT_calculatedfit.setFont(font)
        self.TXT_calculatedfit.setObjectName(_fromUtf8("TXT_calculatedfit"))
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 71, 16))
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
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.TXT_currentfit = QtGui.QLabel(self.groupBox_4)
        self.TXT_currentfit.setGeometry(QtCore.QRect(170, 20, 331, 16))
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
        self.TXT_currentfit.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TXT_currentfit.setFont(font)
        self.TXT_currentfit.setObjectName(_fromUtf8("TXT_currentfit"))
        self.TXT_currentfit_2 = QtGui.QLabel(self.groupBox_4)
        self.TXT_currentfit_2.setGeometry(QtCore.QRect(510, 20, 151, 16))
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
        self.TXT_currentfit_2.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TXT_currentfit_2.setFont(font)
        self.TXT_currentfit_2.setObjectName(_fromUtf8("TXT_currentfit_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Calibrate Position", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Take Sample Points:", None))
        self.BTN_start.setText(_translate("MainWindow", "Start Calibration", None))
        self.T_Instructions.setPlainText(_translate("MainWindow", "Start the Calibration, \n"
"then follow the Instructions here!", None))
        self.BTN_confirm.setText(_translate("MainWindow", "Confirm", None))
        self.TXT_ready.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">READY</span></p></body></html>", None))
        self.TXT_wait.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">WAIT</span></p></body></html>", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Fitting Points:", None))
        self.T_points.setPlainText(_translate("MainWindow", "Once you took samplepoints, they will be displayed here:\n"
"\n"
"", None))
        self.label_2.setText(_translate("MainWindow", "Degree of PolyFit:", None))
        self.BTN_fit.setText(_translate("MainWindow", "Fit", None))
        self.BTN_savefit.setText(_translate("MainWindow", "Save fit ", None))
        self.T_fitresult.setPlainText(_translate("MainWindow", "Once you fitted your points, the Fit will be shown here:\n"
"(highest Polynomial first)\n"
"\n"
"", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Fit:", None))
        self.TXT_calculatedfit.setText(_translate("MainWindow", "Calculated Fit", None))
        self.label_5.setText(_translate("MainWindow", "Current Fit:", None))
        self.TXT_currentfit.setText(_translate("MainWindow", "I AM JUST CLEANING HERE", None))
        self.TXT_currentfit_2.setText(_translate("MainWindow", "(highest polynomial first)", None))

from pyqtgraph import PlotWidget