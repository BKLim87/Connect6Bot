'''
Created on 2016. 6. 24.

@author: bklim
'''
from utils.PolicyUtils import PolicyUtils

class EGreedy(object):
    '''
    classdocs
    '''


    def __init__(self, ee, alpha):
        '''
        Constructor
        '''
        self.E = ee
        self.Alpha = alpha
    
    @staticmethod
    def getName(self):
        return 'EGreedy'
    
    def getAction(self, Qdic, aState, ActionType):
        return PolicyUtils.EGreedy(Qdic, aState, ActionType, self.E)
    
    def update(self, targetLO, StateActionRewardList, side):
        # MC first seen
        FirstSeenState = []
        
        lastReward = StateActionRewardList[len(StateActionRewardList) - 1][2]
        
        Glist = []
        whereflag = len(StateActionRewardList) - 1
        for i in range(0, len(StateActionRewardList)):
            if i == 0:
                Glist.append(lastReward)
            else:
                
                Glist.insert(0, StateActionRewardList[whereflag][2] + (targetLO.Lamda * Glist[0]))
            whereflag -= 1
        
        whereflag = 0
        for aSAR in StateActionRewardList:
            aState = targetLO.StateChanger.getStatebyMap(aSAR[0], side)
            aAction = aSAR[1]
            
            if aState in FirstSeenState:
                pass
            else:                
                FirstSeenState.append(aState)                
                
                # update Ndic
                if targetLO.Ndic.isContain(aState, aAction):
                    targetLO.Ndic.setNestedItem(aState, aAction, targetLO.Ndic.getNestedItem(aState, aAction) + 1)
                else:
                    targetLO.Ndic.setNestedItem(aState, aAction, 1)
                
                # update Qdic
                if targetLO.Qdic.isContain(aState, aAction):
                    oldQ = targetLO.Qdic.getNestedItem(aState, aAction)
                    targetLO.Qdic.setNestedItem(aState, aAction, oldQ + self.Alpha*(Glist[whereflag] - oldQ))
                else:
                    targetLO.Qdic.setNestedItem(aState, aAction, Glist[whereflag])
            whereflag += 1
                    