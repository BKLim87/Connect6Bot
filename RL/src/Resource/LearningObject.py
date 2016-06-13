'''
Created on 2016. 6. 8.

@author: bklim
'''
from utils.ProbUtils import ProbUtils
from Resource.NestedDictionary import NestedDictionary
from Resource.Policy import Policy

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
        
        self.Policy = Policy()
        self.Ndic = NestedDictionary()
        self.Qdic = NestedDictionary()
    
    def getAction(self, state):
        return self.Policy.getAction(state, self.ActionType)
        
    def update(self, StateActionRewardList, side, kth_episode):
        # MC first seen
        FirstSeenState = []
        
        lastReward = StateActionRewardList[len(StateActionRewardList)-1][2]
        
        for aSAR in StateActionRewardList:
            aState = self.StateChanger.getStatebyMap(aSAR[0], side)
            aAction = aSAR[1]
            aReward = aSAR[2]

            if aState in FirstSeenState:
                pass
            else:                
                FirstSeenState.append(aState)                
                SApair = (aState, aAction)
                
                #update Ndic
                if aState in self.Ndic:
                    self.Ndic.setNestedItem(aState, aAction, self.Ndic.getNestedItem(aState, aAction)+1)
                else:
                    self.Ndic.setNestedItem(aState, aAction, 1)
                
                #update Qdic
                if aState in self.Qdic:
                    oldQ = self.Qdic.getNestedItem(aState, aAction)
                    self.Qdic.setNestedItem(aState, aAction, oldQ + (lastReward - oldQ)/self.Ndic.getNestedItem(aState, aAction))
                else:
                    self.Qdic.setNestedItem(aState, aAction, lastReward)
                    
        #update Policy
        for aState in self.Ndic.keys():
            tempqvlist = []
            tempactionlist = self.ActionType.getActionList()
            for aAction in tempactionlist:
                if self.Qdic.containNestedItem(aState, aAction):
                    tempqvlist.append(self.Ndic.getNestedItem(aState, aAction))
                else:
                    tempqvlist.append(0)
            
            #update as GLIE
            self.Policy.update(aState, ProbUtils.changetoGLIE(tempactionlist, tempqvlist, kth_episode))
            
    def print(self):
        print('State Type:'+self.StateChanger.name)
        print('Action Type:'+self.ActionType.name)
        print('Lamda:' + str(self.Lamda))
        print('N dic' + str(self.Ndic))
        print('Q dic' + str(self.Qdic))
        print('Policy' + str(self.Policy))
                
                    
                
                  
                     
                
            
            
