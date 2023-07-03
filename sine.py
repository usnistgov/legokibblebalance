import math
import numpy as np


class Sine():                   #creating and updating a sine curve with flexible a f
    def __init__(self,a,f, data):
        self.myData = data
        self.sinesamplesperu = 1
        self.co = 0
        self.N = 5
#        self.a = self.myData.convertMMToVolt(a)
        self.a = a
        self.f = f
        self.isActive = False
        self.t = np.zeros(1)
        self.sineCurve = np.zeros(1)
        self.sineupdatedt = 1
        self.sinesampledt = 1
        

    def setActive(self, value):
        self.isActive = value

    def saveTask(self, task):
        self.myTask = task        
        self.myTask.signalNewCallback.connect(self.updateSine)
            
    def updateSine(self):
        if self.isActive:
            self.sineupdatedt = self.myTask.getDt() * self.myTask.getL()      
            self.sinesampledt= self.sineupdatedt / self.sinesamplesperu
            self.maxlen= int(1 / self.sinesampledt * self.N)
            
            nt=self.sinesampledt*np.arange(self.co,(self.co+self.sinesamplesperu))
            self.t=np.hstack((self.t,nt))
                
            for x in nt:
                y = self.a * math.sin(self.f *2*math.pi*x)
                self.sineCurve = np.append(self.sineCurve,y)
                
            self.co += self.sinesamplesperu
    
            if len(self.t)>self.maxlen:
                self.t = self.t[-self.maxlen:]
                self.sineCurve = self.sineCurve[-self.maxlen:]
               
    def giveSineData(self):             #returning x and y values of the curve as a list
        sine = []
        x = self.t
        y = self.sineCurve
        lx =len(x)
        ly =len(y)
        lmin =min(lx,ly)
        x = x[0:lmin]
        y = y[0:lmin]
        sine.append(x)
        sine.append(y)
        return sine
        
    def giveDerivative(self):
        nt=self.sinesampledt*np.arange(self.co,(self.co+self.sinesamplesperu))
        x=nt[-1]
        y = self.a *self.f *2* math.cos(self.f *2*math.pi*x)
        return y
        
    def giveCurrentY(self):
        sine = self.giveSineData()
        return sine[1][-1]
        
    def setAF(self, a, f):
#        self.a = self.myData.convertMMToVolt(a)
        self.a = a
        self.f = f
        
    def getA(self):
        return self.a
        
    def getF(self):
        return self.f
        