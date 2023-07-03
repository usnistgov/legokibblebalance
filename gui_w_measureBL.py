# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_measureBL.ui'
#
# Created: Fri Mar 10 17:21:35 2017
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
        MainWindow.resize(672, 621)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.BTN_resetBL0 = QtGui.QPushButton(self.centralwidget)
        self.BTN_resetBL0.setObjectName(_fromUtf8("BTN_resetBL0"))
        self.gridLayout.addWidget(self.BTN_resetBL0, 0, 0, 1, 1)
        self.TXT_BLcoil = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TXT_BLcoil.setFont(font)
        self.TXT_BLcoil.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_BLcoil.setObjectName(_fromUtf8("TXT_BLcoil"))
        self.gridLayout.addWidget(self.TXT_BLcoil, 0, 1, 1, 1)
        self.BTN_saveBL0 = QtGui.QPushButton(self.centralwidget)
        self.BTN_saveBL0.setObjectName(_fromUtf8("BTN_saveBL0"))
        self.gridLayout.addWidget(self.BTN_saveBL0, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.LCD_BLcurrent = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_BLcurrent.setMinimumSize(QtCore.QSize(0, 30))
        self.LCD_BLcurrent.setObjectName(_fromUtf8("LCD_BLcurrent"))
        self.gridLayout.addWidget(self.LCD_BLcurrent, 2, 0, 1, 1)
        self.LCD_BLmean = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_BLmean.setMinimumSize(QtCore.QSize(0, 30))
        self.LCD_BLmean.setObjectName(_fromUtf8("LCD_BLmean"))
        self.gridLayout.addWidget(self.LCD_BLmean, 2, 1, 1, 1)
        self.LCD_BLerror = QtGui.QLCDNumber(self.centralwidget)
        self.LCD_BLerror.setMinimumSize(QtCore.QSize(0, 30))
        self.LCD_BLerror.setObjectName(_fromUtf8("LCD_BLerror"))
        self.gridLayout.addWidget(self.LCD_BLerror, 2, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.label_8.setPalette(palette)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.PW_2periods = PlotWidget(self.centralwidget)
        self.PW_2periods.setObjectName(_fromUtf8("PW_2periods"))
        self.gridLayout.addWidget(self.PW_2periods, 4, 0, 1, 3)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.PW_BLofPos = PlotWidget(self.centralwidget)
        self.PW_BLofPos.setObjectName(_fromUtf8("PW_BLofPos"))
        self.gridLayout.addWidget(self.PW_BLofPos, 6, 0, 1, 3)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.PW_BL0ofTime = PlotWidget(self.centralwidget)
        self.PW_BL0ofTime.setObjectName(_fromUtf8("PW_BL0ofTime"))
        self.gridLayout.addWidget(self.PW_BL0ofTime, 8, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Measure BL", None))
        self.BTN_resetBL0.setText(_translate("MainWindow", "Reset: BL at zero position (time)", None))
        self.TXT_BLcoil.setText(_translate("MainWindow", "BL of coil X", None))
        self.BTN_saveBL0.setText(_translate("MainWindow", "Save Mean Bl0", None))
        self.label_2.setText(_translate("MainWindow", "Current BL@0:", None))
        self.label.setText(_translate("MainWindow", "Mean BL@0:", None))
        self.label_3.setText(_translate("MainWindow", "Error in %:", None))
        self.label_5.setText(_translate("MainWindow", "Voltage depending on coil velocity (white)", None))
        self.label_8.setText(_translate("MainWindow", "Fit (red)", None))
        self.label_6.setText(_translate("MainWindow", "BL depending on balance position", None))
        self.label_7.setText(_translate("MainWindow", "BL at zero position measurements:", None))

from pyqtgraph import PlotWidget
