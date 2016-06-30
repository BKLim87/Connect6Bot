'''
Created on 2016. 6. 26.

@author: Administrator
'''
from Resource.Map import Map
from Resource.NestedDictionary import NestedDictionary
import random

class QLearning(object):
    '''
    classdocs
    '''


    def __init__(self, al):
        '''
        Constructor
        '''
        self.alpha = al
    def update(self, aLearningObject, aMatchHistory, LO1, LO2):
        Qdic = aLearningObject.Qdic
        
        LO1side = 1
        if aMatchHistory[1][0][0].isStartMap():
            LO1side = 2
            LO2side = 1
        else:
            LO2side = 2
        
        #Learning from LO1
        for i in range(0, len(aMatchHistory[1])-1):
            turnState = aLearningObject.StateChanger.getStatebyMap(aMatchHistory[1][i][0], LO1side)
            if aLearningObject.ActionType.getName() == LO1.ActionType.getName():
                turnAction = aMatchHistory[1][i][1]
            else:
                turnAction = aLearningObject.ActionType.decodePhase()
            
            nextState = aLearningObject.StateChanger.getStatebyMap(aMatchHistory[1][i+1][0], LO1side)
            
            maxQ = -1
            for aAction in aLearningObject.ActionType.getActionList(aMatchHistory[1][i+1][0]):
                if not Qdic.isContain(nextState, aAction):
                    Qdic.setNestedItem(nextState, aAction, random.random()-0.5)
                getQ = Qdic.getNestedItem(nextState, aAction)
                if maxQ < getQ:
                    maxQ = getQ
            
            if Qdic.isContain(turnState, turnAction):
                oldQ = Qdic.getNestedItem(turnState, turnAction)
            else:
                oldQ = random.random()-0.5
            oldQ = oldQ + self.alpha*(aMatchHistory[1][i][2] + aLearningObject.Lamda*maxQ - oldQ)
            Qdic.setNestedItem(turnState, turnAction, oldQ)
        #last reward learning
        lastState = aLearningObject.StateChanger.getStatebyMap(aMatchHistory[1][len(aMatchHistory[1])-1][0], LO1side)
        if aLearningObject.ActionType.getName() == LO1.ActionType.getName():
            lastAction = aMatchHistory[1][len(aMatchHistory[1])-1][1]
        else:
            lastAction = aLearningObject.ActionType.decodePhase()
        Qdic.setNestedItem(lastState, lastAction, aMatchHistory[1][len(aMatchHistory[1])-1][2])
            
        #Learning from LO2
        for i in range(0, len(aMatchHistory[2])-1):
            turnState = aLearningObject.StateChanger.getStatebyMap(aMatchHistory[2][i][0], LO2side)
            if aLearningObject.ActionType.getName() == LO2.ActionType.getName():
                turnAction = aMatchHistory[2][i][1]
            else:
                turnAction = aLearningObject.ActionType.decodePhase()
            
            nextState = aLearningObject.StateChanger.getStatebyMap(aMatchHistory[2][i+1][0], LO2side)
            
            maxQ = -1
            for aAction in aLearningObject.ActionType.getActionList(aMatchHistory[2][i+1][0]):
                if not Qdic.isContain(nextState, aAction):
                    Qdic.setNestedItem(nextState, aAction, random.random()-0.5)
                getQ = Qdic.getNestedItem(nextState, aAction)
                if maxQ < getQ:
                    maxQ = getQ
            
            if Qdic.isContain(turnState, turnAction):
                oldQ = Qdic.getNestedItem(turnState, turnAction)
            else:
                oldQ = random.random()-0.5
            oldQ = oldQ + self.alpha*(aMatchHistory[2][i][2] + aLearningObject.Lamda*maxQ - oldQ)
            Qdic.setNestedItem(turnState, turnAction, oldQ)
        #last reward learning
        lastState = aLearningObject.StateChanger.getStatebyMap(aMatchHistory[2][len(aMatchHistory[2])-1][0], LO2side)
        if aLearningObject.ActionType.getName() == LO2.ActionType.getName():
            lastAction = aMatchHistory[2][len(aMatchHistory[2])-1][1]
        else:
            lastAction = aLearningObject.ActionType.decodePhase()
        Qdic.setNestedItem(lastState, lastAction, aMatchHistory[2][len(aMatchHistory[2])-1][2])    
            
        
