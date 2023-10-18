# -*- coding: utf-8 -*-

from PyQt5 import QtGui,QtWidgets

def doFactoryReset(w_main, config):
    question = QtWidgets.QMessageBox()
    question.setWindowTitle("Confirm Factory Reset...")
    text = "Are you sure you want do a Factory-Reset and restore everything to default? \n Program will close afterwards"
    question.setText(text)
    question.setStandardButtons(QtWidgets.QMessageBox.Yes)
    question.addButton(QtWidgets.QMessageBox.No)
    question.setDefaultButton(QtWidgets.QMessageBox.No)
    if (question.exec_() == QtWidgets.QMessageBox.Yes):
        resetFactory(config)
        w_main.prepareDesiredClose()
        w_main.close()
        
def resetFactory(config):
    
    config['dataacq']['samprate']=str(220)
    config['dataacq']['length']=str(1)
    config['dataacq']['s']=str(10)
    
    config['global']['remember']=str("False")
    config['global']['activecoil']=str("coilA")
    config['global']['device']=str(" ")
    config['global']['movearea']=str(3)
    config['global']['velo_amp']=str(0.3)
    config['global']['velo_freq']=str(0.5)
    config['global']['mymin']=str(-0.04)
    config['global']['mymax']=str(0.04)
    config['global']['offset']=str(0.03)
    config['global']['valrange']=str(0.1)
    config['global']['balance0photooffset']=str(0.17375)
    config['global']['posfit']=str("-8.97529997447,-8.73595864182,0.0")
    config['global']['ssvfit']=str("-0.0126111144448,-0.114172563963,0.0")
    config['global']['armlength']=str(175.0)
    config['global']['g']=str(9.81)
    config['global']['resistance']=str(1500)
    config['global']['accPosError']=str(0.007)

    config['coilA']['p_fine']=str(0.5)
    config['coilA']['i_fine']=str(1.0)
    config['coilA']['d_fine']=str(0.5)
    config['coilA']['p_coarse']=str(50.0)
    config['coilA']['i_coarse']=str(10.0)
    config['coilA']['i_coarse']=str(10.0)
    config['coilA']['pidswitchvalue']=str(0.3)
    config['coilA']['p_velo']=str(200.0)
    config['coilA']['i_velo']=str(400.0)
    config['coilA']['d_velo']=str(10.0)
    config['coilA']['bl0']=str(21.5181748568)
    
    config['coilB']['p_fine']=str(0.5)
    config['coilB']['i_fine']=str(1.0)
    config['coilB']['d_fine']=str(0.5)
    config['coilB']['p_coarse']=str(50.0)
    config['coilB']['i_coarse']=str(10.0)
    config['coilB']['i_coarse']=str(10.0)
    config['coilB']['pidswitchvalue']=str(0.3)
    config['coilB']['p_velo']=str(200.0)
    config['coilB']['i_velo']=str(400.0)
    config['coilB']['d_velo']=str(10.0)
    config['coilB']['bl0']=str(22.0836657922)
    
    with open('config.ini', 'w') as configfile:
            config.write(configfile)

    return