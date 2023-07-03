# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_coilPolarity.ui'
#
# Created: Fri Mar 03 14:56:39 2017
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
        MainWindow.setMinimumSize(QtCore.QSize(220, 110))
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.RDB_A_neg = QtGui.QRadioButton(self.groupBox)
        self.RDB_A_neg.setObjectName(_fromUtf8("RDB_A_neg"))
        self.gridLayout_3.addWidget(self.RDB_A_neg, 2, 0, 1, 1)
        self.RDB_A_pos = QtGui.QRadioButton(self.groupBox)
        self.RDB_A_pos.setObjectName(_fromUtf8("RDB_A_pos"))
        self.gridLayout_3.addWidget(self.RDB_A_pos, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.RDB_B_pos = QtGui.QRadioButton(self.groupBox_2)
        self.RDB_B_pos.setObjectName(_fromUtf8("RDB_B_pos"))
        self.gridLayout_2.addWidget(self.RDB_B_pos, 1, 0, 1, 1)
        self.RDB_B_neg = QtGui.QRadioButton(self.groupBox_2)
        self.RDB_B_neg.setObjectName(_fromUtf8("RDB_B_neg"))
        self.gridLayout_2.addWidget(self.RDB_B_neg, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings: Coil Polarity", None))
        self.groupBox.setTitle(_translate("MainWindow", "Coil A", None))
        self.label.setText(_translate("MainWindow", "Polarity", None))
        self.RDB_A_neg.setText(_translate("MainWindow", "Negative", None))
        self.RDB_A_pos.setText(_translate("MainWindow", "Positive", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Coil B", None))
        self.label_2.setText(_translate("MainWindow", "Polarity", None))
        self.RDB_B_pos.setText(_translate("MainWindow", "Positive", None))
        self.RDB_B_neg.setText(_translate("MainWindow", "Negative", None))

