# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_pathsAndVariables.ui'
#
# Created: Fri Mar 10 17:21:53 2017
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

class Ui_w_pathsAndVariables(object):
    def setupUi(self, w_pathsAndVariables):
        w_pathsAndVariables.setObjectName(_fromUtf8("w_pathsAndVariables"))
        w_pathsAndVariables.resize(311, 481)
        self.centralwidget = QtWidgets.QWidget(w_pathsAndVariables)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.CB_defaultFolder = QtWidgets.QCheckBox(self.groupBox)
        self.CB_defaultFolder.setEnabled(False)
        self.CB_defaultFolder.setChecked(True)
        self.CB_defaultFolder.setObjectName(_fromUtf8("CB_defaultFolder"))
        self.gridLayout_2.addWidget(self.CB_defaultFolder, 0, 0, 1, 2)
        self.CB_diffrentFolder = QtWidgets.QCheckBox(self.groupBox)
        self.CB_diffrentFolder.setEnabled(False)
        self.CB_diffrentFolder.setObjectName(_fromUtf8("CB_diffrentFolder"))
        self.gridLayout_2.addWidget(self.CB_diffrentFolder, 0, 2, 1, 1)
        self.label_Path = QtWidgets.QLabel(self.groupBox)
        self.label_Path.setEnabled(False)
        self.label_Path.setObjectName(_fromUtf8("label_Path"))
        self.gridLayout_2.addWidget(self.label_Path, 1, 0, 1, 1)
        self.TEXT_Path = QtWidgets.QLineEdit(self.groupBox)
        self.TEXT_Path.setEnabled(False)
        self.TEXT_Path.setText(_fromUtf8(""))
        self.TEXT_Path.setObjectName(_fromUtf8("TEXT_Path"))
        self.gridLayout_2.addWidget(self.TEXT_Path, 1, 1, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.TB_Armlength = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.TB_Armlength.setDecimals(2)
        self.TB_Armlength.setMaximum(1000.0)
        self.TB_Armlength.setObjectName(_fromUtf8("TB_Armlength"))
        self.gridLayout.addWidget(self.TB_Armlength, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.TB_Resistance = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.TB_Resistance.setMaximum(999999999.0)
        self.TB_Resistance.setObjectName(_fromUtf8("TB_Resistance"))
        self.gridLayout.addWidget(self.TB_Resistance, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.TB_little_g = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.TB_little_g.setDecimals(4)
        self.TB_little_g.setMinimum(8.0)
        self.TB_little_g.setMaximum(11.0)
        self.TB_little_g.setSingleStep(0.01)
        self.TB_little_g.setProperty("value", 8.0)
        self.TB_little_g.setObjectName(_fromUtf8("TB_little_g"))
        self.gridLayout.addWidget(self.TB_little_g, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.TB_AcceptablePositionDeviation = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.TB_AcceptablePositionDeviation.setDecimals(4)
        self.TB_AcceptablePositionDeviation.setMinimum(0.0)
        self.TB_AcceptablePositionDeviation.setMaximum(1.0)
        self.TB_AcceptablePositionDeviation.setSingleStep(0.001)
        self.TB_AcceptablePositionDeviation.setProperty("value", 0.007)
        self.TB_AcceptablePositionDeviation.setObjectName(_fromUtf8("TB_AcceptablePositionDeviation"))
        self.gridLayout.addWidget(self.TB_AcceptablePositionDeviation, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.BTN_saveRestart = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_saveRestart.setObjectName(_fromUtf8("BTN_saveRestart"))
        self.gridLayout_3.addWidget(self.BTN_saveRestart, 2, 0, 1, 1)
        w_pathsAndVariables.setCentralWidget(self.centralwidget)

        self.retranslateUi(w_pathsAndVariables)
        QtCore.QMetaObject.connectSlotsByName(w_pathsAndVariables)

    def retranslateUi(self, w_pathsAndVariables):
        w_pathsAndVariables.setWindowTitle(_translate("w_pathsAndVariables", "Settings: Paths & Variables", None))
        self.groupBox.setTitle(_translate("w_pathsAndVariables", "Paths", None))
        self.CB_defaultFolder.setText(_translate("w_pathsAndVariables", "Use default Folder", None))
        self.CB_diffrentFolder.setText(_translate("w_pathsAndVariables", "Use default Folder", None))
        self.label_Path.setText(_translate("w_pathsAndVariables", "Path for Config-Files:", None))
        self.groupBox_2.setTitle(_translate("w_pathsAndVariables", "Variables", None))
        self.label_9.setText(_translate("w_pathsAndVariables", "Watt Balance Armlength", None))
        self.label_10.setText(_translate("w_pathsAndVariables", "cm", None))
        self.label_6.setText(_translate("w_pathsAndVariables", "Resitance ", None))
        self.label_11.setText(_translate("w_pathsAndVariables", "ohm", None))
        self.label_7.setText(_translate("w_pathsAndVariables", "g", None))
        self.label_12.setText(_translate("w_pathsAndVariables", "m/s²", None))
        self.label_8.setText(_translate("w_pathsAndVariables", "Acceptable Position Deviation:", None))
        self.label_13.setText(_translate("w_pathsAndVariables", "?mm?", None))
        self.BTN_saveRestart.setText(_translate("w_pathsAndVariables", "save values and close program", None))

