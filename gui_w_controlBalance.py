# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_controlBalance.ui'
#
# Created: Mon Mar 06 14:36:24 2017
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
        MainWindow.resize(312, 84)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.TB_analogOutput = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.TB_analogOutput.setFrame(True)
        self.TB_analogOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.TB_analogOutput.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.TB_analogOutput.setKeyboardTracking(False)
        self.TB_analogOutput.setDecimals(3)
        self.TB_analogOutput.setMinimum(-10.0)
        self.TB_analogOutput.setMaximum(10.0)
        self.TB_analogOutput.setSingleStep(0.01)
        self.TB_analogOutput.setObjectName(_fromUtf8("TB_analogOutput"))
        self.horizontalLayout.addWidget(self.TB_analogOutput)
        self.LCD_analogOutput = QtWidgets.QLCDNumber(self.groupBox)
        self.LCD_analogOutput.setObjectName(_fromUtf8("LCD_analogOutput"))
        self.horizontalLayout.addWidget(self.LCD_analogOutput)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 4, 1)
        self.CB_usePIDFeedback = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_usePIDFeedback.setChecked(True)
        self.CB_usePIDFeedback.setObjectName(_fromUtf8("CB_usePIDFeedback"))
        self.gridLayout.addWidget(self.CB_usePIDFeedback, 0, 0, 1, 1)
        self.CB_useInputBox = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_useInputBox.setChecked(False)
        self.CB_useInputBox.setObjectName(_fromUtf8("CB_useInputBox"))
        self.gridLayout.addWidget(self.CB_useInputBox, 1, 0, 1, 1)
        self.CB_useInputWheel = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_useInputWheel.setEnabled(False)
        self.CB_useInputWheel.setObjectName(_fromUtf8("CB_useInputWheel"))
        self.gridLayout.addWidget(self.CB_useInputWheel, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Control Balance Manual", None))
        self.groupBox.setTitle(_translate("MainWindow", "Output Voltage", None))
        self.CB_usePIDFeedback.setText(_translate("MainWindow", "Use static PID Feedback", None))
        self.CB_useInputBox.setText(_translate("MainWindow", "Use Input Box", None))
        self.CB_useInputWheel.setText(_translate("MainWindow", "Use Input Wheel", None))

