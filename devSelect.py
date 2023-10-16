# -*- coding: utf-8 -*-

import PyDAQmx as daq
from PyQt5 import QtGui, QtCore,QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from functools import partial
import sys

class DeviceListDialog(QWidget):
    def __init__(self, active_devices, myChanger):
        QtWidgets.QWidget.__init__(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setAlignment             
        text = QtWidgets.QLabel()
        text.setText("Choose the NI-Device you want to use")
        layout.addWidget(text)
        self.buttons = []
        for device in active_devices:
            self.buttons.append(QtWidgets.QPushButton(device, self))
            self.buttons[-1].clicked.connect(partial(myChanger.changeActiveDevice, data=device))
            self.buttons[-1].clicked.connect(myChanger.saveRemember)
            self.buttons[-1].clicked.connect(self.done)
            layout.addWidget(self.buttons[-1])
        cb_UseAsDefault = QtWidgets.QCheckBox("Always use this Device")
        cb_UseAsDefault.stateChanged.connect(lambda: myChanger.toggleRemember(cb_UseAsDefault.isChecked()))
        layout.addWidget(cb_UseAsDefault)
        
    def done(self):
        self.close()
            
class DeviceFinder(object):
    def __init__(self,config, window_main):
        self.myconfig = config
        self.myChanger = DevChanger(self.myconfig, window_main)
        self.rememberedDevice = self.myconfig['global']['remember']
        
    def forcedSearch(self,w_main):
        result = QtWidgets.QMessageBox.question(w_main,
                          "Choose New Device?",
                          "If you choose a new Device the Program will close and you have to restart manually.",
                          QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            self.rememberedDevice = "False"
            self.search()
            w_main.prepareDesiredClose()
            w_main.close()
        
        
    def search(self):
        self.buffer_size = 100
        self.the_buffer = daq.ctypes.create_string_buffer(self.buffer_size)
        daq.DAQmxGetSysDevNames(self.the_buffer, self.buffer_size);
        
        self.device_list = self.the_buffer.value.decode()
        print(self.device_list)
        self.active_devices = [i.strip() for i in self.device_list.split(",")]
        self.w_devselect = DeviceListDialog(self.active_devices,self.myChanger)
    
    
        if len(self.active_devices[0])!=0:
            if len(self.active_devices)!=1:
                if (self.rememberedDevice == "True"):
                    if self.myconfig['global']['device'] in self.active_devices:
                        self.myChanger.changeActiveDevice(self.myconfig['global']['device']) #TODO shorten (just end method)
                        self.w_devselect.close()
                    else:
                        self.w_devselect.show()
                else:
                    self.w_devselect.show()
                
            else:
                self.myChanger.changeActiveDevice(self.active_devices[0])
                self.w_devselect.close()
        else:   
            self.msgBox = QtWidgets.QMessageBox()
            self.msgBox.setWindowModality(QtCore.Qt.ApplicationModal)
            self.msgBox.setWindowTitle("Lego Watt-Balance")
            self.msgBox.setText("Error:")
            self.msgBox.setInformativeText("No Device has been found")
            self.msgBox.addButton(QtWidgets.QPushButton('Try Again'), QtWidgets.QMessageBox.AcceptRole)
            self.msgBox.addButton(QtWidgets.QPushButton('Exit'), QtWidgets.QMessageBox.NoRole)
            ret = self.msgBox.exec_()
            if ret == QtWidgets.QMessageBox.AcceptRole:
                self.msgBox.close()
                self.search()
            else:
                self.msgBox.close()
                sys.exit()


class DevChanger(QtCore.QObject):
    deviceFound = QtCore.pyqtSignal(object)
    def __init__(self, config, window_main):
        QtCore.QObject.__init__(self)
        self.myconfig = config
        self.myMainwindow = window_main
        self.remember = False
        
    def changeActiveDevice(self,data):            
        self.myconfig['global']['device'] = str(data)
        self.deviceFound.emit(self.myMainwindow)
        print("device changed")
        
    def toggleRemember(self, newRemember):
        self.remember = newRemember
        
    def saveRemember(self):
        if self.remember:
            self.myconfig['global']['remember'] = "True"
        else:
            self.myconfig['global']['remember'] = "False"
        with open('config.ini', 'w') as configfile:
            self.myconfig.write(configfile)


    
            
