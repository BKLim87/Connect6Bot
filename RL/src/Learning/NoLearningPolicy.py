'''
Created on 2016. 6. 24.

@author: bklim
'''
from utils.PolicyUtils import PolicyUtils

class NoLearningPolicy(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    @staticmethod
    def getName(self):
        return 'No Learning Policy'
    
    #pick action by greedy
    def getAction(self, Qdic, aState, ActionType):
        return PolicyUtils.Greedy(Qdic, aState, ActionType)
    
    #no update
    def update(self, targetLO, StateActionRewardList, side):
        pass