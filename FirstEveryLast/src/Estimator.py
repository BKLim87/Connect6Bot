'''
Created on 2016. 5. 12.

@author: bklim
'''
import random

class Estimator(object):
    '''
    classdocs
    '''


    def __init__(self, pro, historys):
        '''
        Constructor
        '''
        self.Pro = pro
        self.batchCalcValues(historys)
        
    def batchCalcValues(self, historys):
        self.Values =[]
        for ahistory in historys:
            self.Values.append(self.calcValue(ahistory))
        
    def Every(self, historys):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            for j in range(0, len(historys[i])):
                Nstate[historys[i][j]] += 1
                Nvalue[historys[i][j]] += self.Values[i][j]
                
        for i in range(0, len(Nvalue)):
            Nvalue[i] = Nvalue[i]/Nstate[i]
        
        return [Nstate, Nvalue]
    
    def Last(self, historys):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            tempstate = [0]*len(self.Pro.States)
            for j in range(len(historys[i])-1,-1,-1):
                if tempstate[historys[i][j]] == 0:
                    Nstate[historys[i][j]] += 1
                    tempstate[historys[i][j]] += 1
                    Nvalue[historys[i][j]] += self.Values[i][j]
                    
        for i in range(0, len(Nvalue)):
            Nvalue[i] = Nvalue[i]/Nstate[i]
        
        return [Nstate, Nvalue]
    
    def Random(self, historys):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        Rstate = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            tempstate = [0]*len(self.Pro.States)
            
            for r in range(0,len(self.Pro.States)):
                Rstate[r] = random.randrange(0,20)
            
            for j in range(0, len(historys[i])):                
                tempstate[historys[i][j]] += 1
                if tempstate[historys[i][j]] == Rstate[historys[i][j]]:
                    Nstate[historys[i][j]] += 1
                    Nvalue[historys[i][j]] += self.Values[i][j]
                    
        for i in range(0, len(Nvalue)):
            if(Nstate[i] == 0):
                Nvalue[i] = 'NaN'
            else:
                Nvalue[i] = Nvalue[i]/Nstate[i]
        
        return [Nstate, Nvalue]
        
    def First(self, historys):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            tempstate = [0]*len(self.Pro.States)
            for j in range(0, len(historys[i])):
                if tempstate[historys[i][j]] == 0:
                    Nstate[historys[i][j]] += 1
                    tempstate[historys[i][j]] += 1
                    Nvalue[historys[i][j]] += self.Values[i][j]
                    
        for i in range(0, len(Nvalue)):
            Nvalue[i] = Nvalue[i]/Nstate[i]
        
        return [Nstate, Nvalue]
    
    def Order(self, historys, ord):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            tempstate = [0]*len(self.Pro.States)
            for j in range(0, len(historys[i])):                
                tempstate[historys[i][j]] += 1
                if tempstate[historys[i][j]] == ord:
                    Nstate[historys[i][j]] += 1
                    Nvalue[historys[i][j]] += self.Values[i][j]
                    
        for i in range(0, len(Nvalue)):
            if(Nstate[i] == 0):
                Nvalue[i] = 'NaN'
            else:
                Nvalue[i] = Nvalue[i]/Nstate[i]
        
        return [Nstate, Nvalue]
    
    def TDalphaLamda(self, historys, alpha, lamda):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            for j in range(0, len(historys[i])):
                Nstate[historys[i][j]] += 1
                
                tempstepvalue = self.Pro.Reward[historys[i][j]]
                for n in range(j+1, len(historys[i])):
                    nn = n - j                    
                    tempstepvalue += pow(self.Pro.Lamda, n-j)*self.Pro.Reward[historys[i][n]]
                    
                if alpha == 0:                    
                    Nvalue[historys[i][j]] += (tempstepvalue-Nvalue[historys[i][j]])/Nstate[historys[i][j]]                
                else:    
                    Nvalue[historys[i][j]] += (tempstepvalue-Nvalue[historys[i][j]])*alpha
                    
        return [Nstate, Nvalue]
    
    def TDalphaLast(self, historys, alpha):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            for j in range(0, len(historys[i])):
                Nstate[historys[i][j]] += 1
                
                tempstepvalue = self.Pro.Reward[historys[i][j]]
                for n in range(j+1, len(historys[i])):
                    tempstepvalue += pow(self.Pro.Lamda, n-j)*self.Pro.Reward[historys[i][n]]
                    
                if alpha == 0:                    
                    Nvalue[historys[i][j]] += (tempstepvalue-Nvalue[historys[i][j]])/Nstate[historys[i][j]]                
                else:    
                    Nvalue[historys[i][j]] += (tempstepvalue-Nvalue[historys[i][j]])*alpha
                    
        return [Nstate, Nvalue]
        
    
    def TDalphaNstep(self, historys, alpha, Nst):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            for j in range(0, len(historys[i])):
                Nstate[historys[i][j]] += 1
                if j>=len(historys[i])-Nst:
                    tempstepvalue = 0
                    for n in range(0, Nst):
                        if j+n < len(historys[i]):
                            tempstepvalue += pow(self.Pro.Lamda,n)*self.Pro.Reward[historys[i][j+n]]
                        else:
                            tempstepvalue += pow(self.Pro.Lamda,n)*self.Pro.Reward[historys[i][len(historys[i])-1]]
                    tempstepvalue += pow(self.Pro.Lamda, Nst)*Nvalue[historys[i][len(historys[i])-1]]
                    if alpha == 0:                    
                        Nvalue[historys[i][j]] += (tempstepvalue-Nvalue[historys[i][j]])/Nstate[historys[i][j]]                
                    else:    
                        Nvalue[historys[i][j]] += (tempstepvalue-Nvalue[historys[i][j]])*alpha
                else:
                    tempstepvalue = 0
                    for n in range(0, Nst):
                        tempstepvalue += pow(self.Pro.Lamda,n)*self.Pro.Reward[historys[i][j+n]]
                    tempstepvalue += pow(self.Pro.Lamda, Nst)*Nvalue[historys[i][j+Nst]]
                    if alpha == 0:                    
                        Nvalue[historys[i][j]] += (tempstepvalue-Nvalue[historys[i][j]])/Nstate[historys[i][j]]                
                    else:    
                        Nvalue[historys[i][j]] += (tempstepvalue-Nvalue[historys[i][j]])*alpha
        
        return [Nstate, Nvalue]
    
    def TDalpha(self, historys, alpha):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            for j in range(0, len(historys[i])):
                Nstate[historys[i][j]] += 1
                if j==len(historys[i])-1:
                    Nvalue[historys[i][j]] += (self.Pro.Reward[historys[i][j]]+self.Pro.Lamda*Nvalue[historys[i][j]]-Nvalue[historys[i][j]])*alpha
                else:
                    Nvalue[historys[i][j]] += (self.Pro.Reward[historys[i][j]]+self.Pro.Lamda*Nvalue[historys[i][j+1]]-Nvalue[historys[i][j]])*alpha
        
        return [Nstate, Nvalue]
    
    def TD(self, historys):
        Nstate = [0]*len(self.Pro.States)
        Nvalue = [0]*len(self.Pro.States)
        
        for i in range(0,len(historys)):
            for j in range(0, len(historys[i])):
                Nstate[historys[i][j]] += 1
                if j==len(historys[i])-1:
                    Nvalue[historys[i][j]] += (self.Pro.Reward[historys[i][j]]+self.Pro.Lamda*Nvalue[historys[i][j]]-Nvalue[historys[i][j]])/Nstate[historys[i][j]]
                else:
                    Nvalue[historys[i][j]] += (self.Pro.Reward[historys[i][j]]+self.Pro.Lamda*Nvalue[historys[i][j+1]]-Nvalue[historys[i][j]])/Nstate[historys[i][j]]
        
        return [Nstate, Nvalue]
        
    def calcValue(self, history):
        valuelist = []
        for i in range(0,len(history)):
            value = self.Pro.Reward[history[i]]
            for j in range(i+1, len(history)):
                value += pow(self.Pro.Lamda,(j-i))*self.Pro.Reward[history[j]]
            valuelist.append(value)
        return valuelist