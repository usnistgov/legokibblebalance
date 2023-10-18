from __future__ import division
import numpy as np
import datetime

class PID():
    def __init__(self, usecf, PIDfine, PIDcoarse, PIDSwitchvaluegiven, dtgiven, Lgiven, Ilimitgiven, Targetgiven, maxout): 
        #INITIALISE VARIABLES
        self.P_fine = PIDfine[0]                    #saving given PIDs
        self.I_fine = PIDfine[1]
        self.D_fine = PIDfine[2]
        self.P_coarse = PIDcoarse[0]
        self.I_coarse = PIDcoarse[1]
        self.D_coarse = PIDcoarse[2]
        self.dt = dtgiven                           #saving given dt
        self.L = Lgiven                             #saving given L
        self.target = Targetgiven                   #saving given target
        self.Ilimit = Ilimitgiven                   #saving given Ilimit
        self.PIDSwitchValue = PIDSwitchvaluegiven   #saving given PIDSwitchvalue
        self.pid_fine_co=0                          #counter for how long PID fine area has been reached
        self.PIDmode = 'coarse'
        self.eps = 0.0                                #initialising PID variables
        self.su = 0.0
        self.pid_yom = 0.0
        self.deriv = 0.0
        self.output=0.0
        self.maxoutput = maxout                     #saving given maxoutput
        self.useCoarseFine = usecf                  #determines the use of c/f
                                                    #IF FAlSE INPUT PID SHOULD BE THE SAME FOR PIDfine/coarse
        self.otime = datetime.datetime.now()
        
    def doPIDCalc(self,y,target_der=0,filtfac=0.8,use_measured_dt=True):
        self.now = datetime.datetime.now()
        self.measured_dt = (self.now-self.otime).total_seconds()
        self.otime = self.now
        
        self.eps = y - self.target
        
        if self.useCoarseFine:
            if abs(self.eps) > self.PIDSwitchValue:     #deciding on fine/coarse
                self.PIDmode = 'coarse'                 #coarse if eps is smaller than switchval
                self.pid_fine_co =  0
            else:
                self.pid_fine_co =  self.pid_fine_co + 1#fine if fine area has been reached long enough
                if self.pid_fine_co> 100:
                    self.PIDmode = 'fine'
                    
            if self.PIDmode == 'coarse':                #seeting variables depending on fine/coarse
                P=self.P_coarse
                I=self.I_coarse
                D=self.D_coarse            
            else:
                P=self.P_fine
                I=self.I_fine
                D=self.D_fine
        else:
            P=self.P_fine
            I=self.I_fine
            D=self.D_fine
            
        if use_measured_dt==False:
            self.pid_dt = self.dt * self.L                  #PID Calulation
        else:
            self.pid_dt = self.measured_dt
        if self.pid_dt==0:
            self.pid_dt = 1e-3

        self.su = self.su + I*self.eps*self.pid_dt

        
        if self.su> self.Ilimit:
            self.su= self.Ilimit
        if self.su< -self.Ilimit:
            self.su= -self.Ilimit
            
        self.filtfac = filtfac
        newderiv = ( (y-self.pid_yom)/self.pid_dt) - target_der
        self.deriv =  newderiv *(1-self.filtfac) +self.filtfac* self.deriv 
                      
        self.output = P *self.eps + self.su + D* self.deriv
#        print("% 08.5f\t% 05.2f\t% 05.2f\t% 05.2f\t% 05.2f\t% 05.2f\t% 05.2f\t% 08.5f\t%s\t% 05.2f\t% 05.2f\t% 05.2f"%(self.eps,self.output,P *self.eps,self.su,D*self.deriv,self.deriv,newderiv,self.pid_dt,self.PIDmode,P,I,D))
        if self.output> self.maxoutput:                 #ensuring output is within maxout
            self.output = self.maxoutput
        elif self.output<(-1*self.maxoutput):
            self.output=(-1*self.maxoutput)
        
        self.pid_yom = y
        return self.output                              #returning output

    def generateLastEps(self, eps):
        self.lastXSecondEps = np.hstack((self.lastXSecondEps,eps))
        if len(self.lastXSecondEps)>self.x*self.calcsPerSecond: 
            self.lastXSecondEps = self.lastXSecondEps[-self.x*self.calcsPerSecond:]
        
    def setPID(self, value, name, mode):                #set P I or D coarse/fine
        print('setPID(',value,name,mode,')')
        if mode == 'fine':
            if name == 'p':
                self.P_fine = value
            elif name == 'i':
                self.I_fine = value
            elif name == 'd':
                self.D_fine = value
            else: print('use p,i,d')
        elif mode == 'coarse':
            if name == 'p':
                self.P_coarse = value
            elif name == 'i':
                self.I_coarse = value
            elif name == 'd':
                self.D_coarse = value
            else: print('use p,i,d')
        elif mode == 'velo':
            if name == 'p':
                self.P_coarse = value
                self.P_fine = value
            elif name == 'i':
                self.I_coarse = value
                self.I_fine = value
            elif name == 'd':
                self.D_coarse = value
                self.D_fine = value
            else: print('use p,i,d')          
        else: print('use velo, fine or coarse')
    
    def setL(self,l):
        self.L = l

    
    def setTarget(self, value):                         #set a target
        self.target = value
        #print("received new target: ",self.target)

    def setPIDSwitch(self, value):                      #set a new switchvalue
        print(value)
        self.PIDSwitchValue = abs(value)
        self.printValues()
        
    def printValues(self):
        print("fine(P,I,D):",self.P_fine,self.I_fine,self.D_fine)
        print( "coarse(P,I,D):",self.P_coarse,self.I_coarse,self.D_coarse)
        print( "other Values: mode, switch, usecf", self.PIDmode, self.PIDSwitchValue, self.useCoarseFine)
        
    def getPIDmode(self):                               #get current pid mode fine/coarse
        return self.PIDmode        
        
    def getOutput(self):                                
        return self.output
        
    def getEps(self):
        return self.eps
    
    def getSu(self):
        return self.su
        
    def resetIntegrator(self):
        self.su = 0.0