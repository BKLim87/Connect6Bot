'''
Created on 2016. 6. 8.

@author: bklim
'''
from utils.ProbUtils import ProbUtils

class LearningObject(object):
    '''
    classdocs
    '''


    def __init__(self, aStateChanger, aActionType, alamda):
        '''
        Constructor
        '''
        self.StateChanger = aStateChanger
        self.ActionType = aActionType
        self.Lamda = alamda 
        self.Policy = {}
    
    def getAction(self, state):
        
        if state in self.Policy:
            apl = self.Policy.get(state)
            actionnumber = ProbUtils.getOnefromProblist(apl)
            return self.ActionType.getActionName(actionnumber)
        
        else:
            return ProbUtils.pickUniform(self.ActionType.getActionList())
            