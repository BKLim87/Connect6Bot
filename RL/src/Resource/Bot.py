'''
Created on 2016. 6. 8.

@author: bklim
'''
from Training.RewardCalculator import RewardCalculator

class Bot(object):
    '''
    classdocs
    '''


    def __init__(self, aLearningObject, aside):
        '''
        Constructor
        '''
        self.LearningObject = aLearningObject
        self.side = aside
        self.StateActionRewardList = []
        
    def putLoseReward(self):
        lastorder = len(self.StateActionRewardList)
        if lastorder > 0:
            self.StateActionRewardList[lastorder - 1][2] = RewardCalculator.getLoseReward() 
            
    #def update(self, LearningWay):
    def update(self, kth_episode):
        if len(self.StateActionRewardList) > 0:
            self.LearningObject.update(self.StateActionRewardList, self.side, kth_episode)