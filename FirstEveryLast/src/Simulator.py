'''
Created on 2016. 5. 12.

@author: bklim
'''
import random


class Simulator(object):
    '''
    classdocs
    '''
    def __init__(self, pro, ter):
        '''
        Constructor
        '''
        self.Pro = pro
        self.Terminate = ter
        
    def setProblem(self, pro):
        self.Pro = pro
    
    def batchSimulate(self, startState, num):
        batchhistory = [];
        
        for i in range(0, num):
            ahistory = self.runSimulate(startState)
            batchhistory.append(ahistory)
        
        return batchhistory
        
    def runSimulate(self, startState):
        history = [startState]
        nowState = startState;
        while(nowState != self.Terminate):
            nowState = self.randomState(self.Pro.Trans[nowState])
            history.append(nowState)
        return history            
    
    def randomState(self, problist):
        point = random.random()
        for i in range(0,len(problist)):
            point = point - problist[i]
            if point <= 0:
                return i
    
    