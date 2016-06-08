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
        self.Ndic = {}
        self.Qdic = {}
    
    def getAction(self, state):
        
        if state in self.Policy:
            apl = self.Policy.get(state)
            actionnumber = ProbUtils.getOnefromProblist(apl)
            return self.ActionType.getActionName(actionnumber)
        
        else:
            return ProbUtils.pickUniform(self.ActionType.getActionList())
        
    def update(self, StateActionRewardList, side):
        # MC first seen
        FirstSeenState = []
        
        lastReward = StateActionRewardList[len(StateActionRewardList)-1][2]
        
        for aSAR in StateActionRewardList:
            aState = self.StateChanger.getStatebyMap(aSAR[0], side)
            if aState in FirstSeenState:
                pass
            else:                
                FirstSeenState.append(aState)
                aAction = aSAR[1]
                aReward = aSAR[2]
                
                SApair = (aState, aAction)
                
                #update Ndic
                if aState in self.Ndic:
                    self.Ndic[aState] = self.Ndic.get[SApair] + 1
                else:
                    self.Ndic[SApair] = 1
                
                #update Qdic
                if aState in self.Qdic:
                    self.Qdic[SApair] = self.Qdic[SApair] + (lastReward - self.Qdic[SApair])/self.Ndic[SApair]
                else:
                    self.Qdic[SApair] = lastReward
                    
                
                  
                     
                
            
            
