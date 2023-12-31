# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_w_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 465)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 641, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.TAB_measurement = QtWidgets.QWidget()
        self.TAB_measurement.setObjectName("TAB_measurement")
        self.BTN_measureBL = QtWidgets.QPushButton(self.TAB_measurement)
        self.BTN_measureBL.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.BTN_measureBL.setObjectName("BTN_measureBL")
        self.BTN_measureh = QtWidgets.QPushButton(self.TAB_measurement)
        self.BTN_measureh.setEnabled(False)
        self.BTN_measureh.setGeometry(QtCore.QRect(10, 130, 111, 23))
        self.BTN_measureh.setObjectName("BTN_measureh")
        self.BTN_weighMass = QtWidgets.QPushButton(self.TAB_measurement)
        self.BTN_weighMass.setGeometry(QtCore.QRect(10, 70, 111, 23))
        self.BTN_weighMass.setObjectName("BTN_weighMass")
        self.label_4 = QtWidgets.QLabel(self.TAB_measurement)
        self.label_4.setGeometry(QtCore.QRect(140, 130, 281, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.TAB_measurement)
        self.label_5.setGeometry(QtCore.QRect(140, 70, 281, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.TAB_measurement)
        self.label_6.setGeometry(QtCore.QRect(140, 10, 281, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.TAB_measurement)
        self.label_7.setGeometry(QtCore.QRect(140, 150, 281, 21))
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.TAB_measurement, "")
        self.TAB_calibration = QtWidgets.QWidget()
        self.TAB_calibration.setObjectName("TAB_calibration")
        self.BTN_PID = QtWidgets.QPushButton(self.TAB_calibration)
        self.BTN_PID.setGeometry(QtCore.QRect(10, 10, 201, 23))
        self.BTN_PID.setObjectName("BTN_PID")
        self.label_2 = QtWidgets.QLabel(self.TAB_calibration)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 401, 21))
        self.label_2.setObjectName("label_2")
        self.BTN_cfgPos = QtWidgets.QPushButton(self.TAB_calibration)
        self.BTN_cfgPos.setGeometry(QtCore.QRect(10, 100, 201, 23))
        self.BTN_cfgPos.setObjectName("BTN_cfgPos")
        self.BTN_velocitymode = QtWidgets.QPushButton(self.TAB_calibration)
        self.BTN_velocitymode.setGeometry(QtCore.QRect(10, 140, 201, 23))
        self.BTN_velocitymode.setObjectName("BTN_velocitymode")
        self.BTN_cfgShadowSensor = QtWidgets.QPushButton(self.TAB_calibration)
        self.BTN_cfgShadowSensor.setGeometry(QtCore.QRect(10, 50, 201, 23))
        self.BTN_cfgShadowSensor.setObjectName("BTN_cfgShadowSensor")
        self.label_8 = QtWidgets.QLabel(self.TAB_calibration)
        self.label_8.setGeometry(QtCore.QRect(220, 50, 401, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.TAB_calibration)
        self.label_9.setGeometry(QtCore.QRect(220, 100, 401, 21))
        self.label_9.setObjectName("label_9")
        self.label_16 = QtWidgets.QLabel(self.TAB_calibration)
        self.label_16.setGeometry(QtCore.QRect(220, 140, 401, 21))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.TAB_calibration)
        self.label_17.setGeometry(QtCore.QRect(220, 70, 401, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.TAB_calibration)
        self.label_18.setGeometry(QtCore.QRect(220, 160, 401, 21))
        self.label_18.setObjectName("label_18")
        self.tabWidget.addTab(self.TAB_calibration, "")
        self.TAB_settings = QtWidgets.QWidget()
        self.TAB_settings.setObjectName("TAB_settings")
        self.BTN_PathAndVariables = QtWidgets.QPushButton(self.TAB_settings)
        self.BTN_PathAndVariables.setGeometry(QtCore.QRect(10, 70, 191, 23))
        self.BTN_PathAndVariables.setObjectName("BTN_PathAndVariables")
        self.BTN_dataAcq = QtWidgets.QPushButton(self.TAB_settings)
        self.BTN_dataAcq.setGeometry(QtCore.QRect(10, 40, 191, 23))
        self.BTN_dataAcq.setObjectName("BTN_dataAcq")
        self.BTN_ChooseDevice = QtWidgets.QPushButton(self.TAB_settings)
        self.BTN_ChooseDevice.setGeometry(QtCore.QRect(10, 10, 191, 23))
        self.BTN_ChooseDevice.setObjectName("BTN_ChooseDevice")
        self.BTN_CoilPolarities = QtWidgets.QPushButton(self.TAB_settings)
        self.BTN_CoilPolarities.setGeometry(QtCore.QRect(10, 100, 191, 23))
        self.BTN_CoilPolarities.setObjectName("BTN_CoilPolarities")
        self.BTN_Debugging = QtWidgets.QPushButton(self.TAB_settings)
        self.BTN_Debugging.setGeometry(QtCore.QRect(10, 130, 191, 23))
        self.BTN_Debugging.setObjectName("BTN_Debugging")
        self.BTN_FactoryReset = QtWidgets.QPushButton(self.TAB_settings)
        self.BTN_FactoryReset.setGeometry(QtCore.QRect(10, 160, 191, 23))
        self.BTN_FactoryReset.setObjectName("BTN_FactoryReset")
        self.label_3 = QtWidgets.QLabel(self.TAB_settings)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 361, 21))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.TAB_settings)
        self.label_10.setGeometry(QtCore.QRect(260, 40, 361, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.TAB_settings)
        self.label_11.setGeometry(QtCore.QRect(260, 70, 361, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.TAB_settings)
        self.label_12.setGeometry(QtCore.QRect(260, 100, 361, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.TAB_settings)
        self.label_13.setGeometry(QtCore.QRect(260, 130, 361, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.TAB_settings)
        self.label_14.setGeometry(QtCore.QRect(260, 160, 361, 21))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.TAB_settings, "")
        self.TAB_about = QtWidgets.QWidget()
        self.TAB_about.setObjectName("TAB_about")
        self.Messages = QtWidgets.QPlainTextEdit(self.TAB_about)
        self.Messages.setGeometry(QtCore.QRect(10, 10, 621, 171))
        self.Messages.setObjectName("Messages")
        self.tabWidget.addTab(self.TAB_about, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 221, 171))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.BTN_current = QtWidgets.QPushButton(self.groupBox)
        self.BTN_current.setGeometry(QtCore.QRect(10, 140, 131, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.BTN_current.setFont(font)
        self.BTN_current.setObjectName("BTN_current")
        self.BTN_coilposition = QtWidgets.QPushButton(self.groupBox)
        self.BTN_coilposition.setGeometry(QtCore.QRect(10, 50, 131, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.BTN_coilposition.setFont(font)
        self.BTN_coilposition.setObjectName("BTN_coilposition")
        self.BTN_voltageacrosscoils = QtWidgets.QPushButton(self.groupBox)
        self.BTN_voltageacrosscoils.setGeometry(QtCore.QRect(10, 110, 131, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.BTN_voltageacrosscoils.setFont(font)
        self.BTN_voltageacrosscoils.setObjectName("BTN_voltageacrosscoils")
        self.BTN_coilvelocities = QtWidgets.QPushButton(self.groupBox)
        self.BTN_coilvelocities.setGeometry(QtCore.QRect(10, 80, 131, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.BTN_coilvelocities.setFont(font)
        self.BTN_coilvelocities.setObjectName("BTN_coilvelocities")
        self.TXT_coilPosition = QtWidgets.QLabel(self.groupBox)
        self.TXT_coilPosition.setEnabled(False)
        self.TXT_coilPosition.setGeometry(QtCore.QRect(150, 50, 61, 31))
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
        self.TXT_coilPosition.setPalette(palette)
        self.TXT_coilPosition.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_coilPosition.setObjectName("TXT_coilPosition")
        self.TXT_coilVelocities = QtWidgets.QLabel(self.groupBox)
        self.TXT_coilVelocities.setEnabled(False)
        self.TXT_coilVelocities.setGeometry(QtCore.QRect(150, 80, 61, 31))
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
        self.TXT_coilVelocities.setPalette(palette)
        self.TXT_coilVelocities.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_coilVelocities.setObjectName("TXT_coilVelocities")
        self.TXT_coilVoltage = QtWidgets.QLabel(self.groupBox)
        self.TXT_coilVoltage.setEnabled(False)
        self.TXT_coilVoltage.setGeometry(QtCore.QRect(150, 110, 61, 31))
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
        self.TXT_coilVoltage.setPalette(palette)
        self.TXT_coilVoltage.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_coilVoltage.setObjectName("TXT_coilVoltage")
        self.TXT_current = QtWidgets.QLabel(self.groupBox)
        self.TXT_current.setEnabled(False)
        self.TXT_current.setGeometry(QtCore.QRect(150, 140, 61, 31))
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
        self.TXT_current.setPalette(palette)
        self.TXT_current.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_current.setObjectName("TXT_current")
        self.BTN_rawphoto = QtWidgets.QPushButton(self.groupBox)
        self.BTN_rawphoto.setGeometry(QtCore.QRect(10, 23, 131, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.BTN_rawphoto.setFont(font)
        self.BTN_rawphoto.setObjectName("BTN_rawphoto")
        self.TXT_rawphoto = QtWidgets.QLabel(self.groupBox)
        self.TXT_rawphoto.setEnabled(False)
        self.TXT_rawphoto.setGeometry(QtCore.QRect(150, 20, 61, 31))
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
        self.TXT_rawphoto.setPalette(palette)
        self.TXT_rawphoto.setAlignment(QtCore.Qt.AlignCenter)
        self.TXT_rawphoto.setObjectName("TXT_rawphoto")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 250, 201, 171))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.RB_coilA = QtWidgets.QRadioButton(self.groupBox_2)
        self.RB_coilA.setGeometry(QtCore.QRect(20, 40, 171, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.RB_coilA.setFont(font)
        self.RB_coilA.setObjectName("RB_coilA")
        self.RB_coilB = QtWidgets.QRadioButton(self.groupBox_2)
        self.RB_coilB.setGeometry(QtCore.QRect(20, 60, 171, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.RB_coilB.setFont(font)
        self.RB_coilB.setObjectName("RB_coilB")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 20, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 80, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 110, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.TXT_BLCoil = QtWidgets.QLabel(self.groupBox_2)
        self.TXT_BLCoil.setGeometry(QtCore.QRect(140, 70, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.TXT_BLCoil.setFont(font)
        self.TXT_BLCoil.setObjectName("TXT_BLCoil")
        self.TXT_weighingCoil = QtWidgets.QLabel(self.groupBox_2)
        self.TXT_weighingCoil.setGeometry(QtCore.QRect(140, 100, 61, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.TXT_weighingCoil.setFont(font)
        self.TXT_weighingCoil.setObjectName("TXT_weighingCoil")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 260, 171, 171))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(15, 20, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.TXT_activeMode = QtWidgets.QLabel(self.groupBox_3)
        self.TXT_activeMode.setGeometry(QtCore.QRect(40, 40, 51, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.TXT_activeMode.setFont(font)
        self.TXT_activeMode.setObjectName("TXT_activeMode")
        self.BTN_manualBalancecontrol = QtWidgets.QPushButton(self.groupBox_3)
        self.BTN_manualBalancecontrol.setGeometry(QtCore.QRect(10, 90, 151, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.BTN_manualBalancecontrol.setFont(font)
        self.BTN_manualBalancecontrol.setObjectName("BTN_manualBalancecontrol")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LEGO Watt-Balance"))
        self.BTN_measureBL.setText(_translate("MainWindow", "Measure BL"))
        self.BTN_measureh.setText(_translate("MainWindow", "Measure h"))
        self.BTN_weighMass.setText(_translate("MainWindow", "Weigh Mass"))
        self.label_4.setText(_translate("MainWindow", "Try to measure Planck\'s Constant, and see how close"))
        self.label_5.setText(_translate("MainWindow", "Weigh a Mass"))
        self.label_6.setText(_translate("MainWindow", "Start velocity mode to measure BL at zero position"))
        self.label_7.setText(_translate("MainWindow", "you are to the latest values."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_measurement), _translate("MainWindow", "Measurement"))
        self.BTN_PID.setText(_translate("MainWindow", "Configure static PID"))
        self.label_2.setText(_translate("MainWindow", "Modify the control loop which is used to stabilize the balance"))
        self.BTN_cfgPos.setText(_translate("MainWindow", "Configure Position"))
        self.BTN_velocitymode.setText(_translate("MainWindow", "Configure Velomode"))
        self.BTN_cfgShadowSensor.setText(_translate("MainWindow", "Configure Shadow S."))
        self.label_8.setText(_translate("MainWindow", "Set the balance\'s zero position and determine where "))
        self.label_9.setText(_translate("MainWindow", "Calibrate the shadow-sensor voltage to millimeter conversion"))
        self.label_16.setText(_translate("MainWindow", "Modify the control loop used in velo mode and customize "))
        self.label_17.setText(_translate("MainWindow", "the correlation shadow-sensor to position is linear. "))
        self.label_18.setText(_translate("MainWindow", "the sine wave used to drive the balance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_calibration), _translate("MainWindow", "Calibration"))
        self.BTN_PathAndVariables.setText(_translate("MainWindow", "Paths and Variables"))
        self.BTN_dataAcq.setText(_translate("MainWindow", "Data Acquisition"))
        self.BTN_ChooseDevice.setText(_translate("MainWindow", "Choose Device"))
        self.BTN_CoilPolarities.setText(_translate("MainWindow", "Coil Polarities"))
        self.BTN_Debugging.setText(_translate("MainWindow", "Debugging"))
        self.BTN_FactoryReset.setText(_translate("MainWindow", "Factory reset"))
        self.label_3.setText(_translate("MainWindow", "Choose another Device in your System"))
        self.label_10.setText(_translate("MainWindow", "Customize the Data Acquisition Parameters"))
        self.label_11.setText(_translate("MainWindow", "Adjust File Path, and Variables depending on your Setup"))
        self.label_12.setText(_translate("MainWindow", "Set the polarities for your Wattbalance coils"))
        self.label_13.setText(_translate("MainWindow", "Get some more information to debugg your system"))
        self.label_14.setText(_translate("MainWindow", "Reset everything to default"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_settings), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TAB_about), _translate("MainWindow", "Messages"))
        self.groupBox.setTitle(_translate("MainWindow", "Graphs:"))
        self.BTN_current.setText(_translate("MainWindow", "Current"))
        self.BTN_coilposition.setText(_translate("MainWindow", "Coil position"))
        self.BTN_voltageacrosscoils.setText(_translate("MainWindow", "Voltage in coils"))
        self.BTN_coilvelocities.setText(_translate("MainWindow", "Coil velocities"))
        self.TXT_coilPosition.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Open</span></p></body></html>"))
        self.TXT_coilVelocities.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Open</span></p></body></html>"))
        self.TXT_coilVoltage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Open</span></p></body></html>"))
        self.TXT_current.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Open</span></p></body></html>"))
        self.BTN_rawphoto.setText(_translate("MainWindow", "Raw photo"))
        self.TXT_rawphoto.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Open</span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Coil Info:"))
        self.RB_coilA.setText(_translate("MainWindow", "Coil A"))
        self.RB_coilB.setText(_translate("MainWindow", "Coil B"))
        self.label_15.setText(_translate("MainWindow", "Coil with currentl:"))
        self.label_19.setText(_translate("MainWindow", "BL meas. on:"))
        self.label_21.setText(_translate("MainWindow", "Weighing on:"))
        self.TXT_BLCoil.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">A/B</span></p></body></html>"))
        self.TXT_weighingCoil.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">A/B</span></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Mode Info:"))
        self.label_20.setText(_translate("MainWindow", "Mode:"))
        self.TXT_activeMode.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">S/V/M</p></body></html>"))
        self.BTN_manualBalancecontrol.setText(_translate("MainWindow", "Manual Control"))
