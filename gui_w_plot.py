# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_plot.ui'
#
# Created: Tue Aug 30 16:22:51 2016
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
        MainWindow.resize(536, 338)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.TXT_plot1 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_plot1.setPalette(palette)
        self.TXT_plot1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TXT_plot1.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_plot1.setObjectName(_fromUtf8("TXT_plot1"))
        self.gridLayout.addWidget(self.TXT_plot1, 0, 2, 1, 1)
        self.TXT_plot2 = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.TXT_plot2.setPalette(palette)
        self.TXT_plot2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TXT_plot2.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_plot2.setObjectName(_fromUtf8("TXT_plot2"))
        self.gridLayout.addWidget(self.TXT_plot2, 0, 1, 1, 1)
        self.PW = PlotWidget(self.centralwidget)
        self.PW.setObjectName(_fromUtf8("PW"))
        self.gridLayout.addWidget(self.PW, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Plotwindow", None))
        self.TXT_plot1.setText(_translate("MainWindow", " ", None))
        self.TXT_plot2.setText(_translate("MainWindow", " ", None))

from pyqtgraph import PlotWidget
