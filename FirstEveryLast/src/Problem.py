'''
Created on 2016. 5. 12.

@author: bklim
'''

class Problem(object):
    '''
    classdocs
    '''
    
    def __init__(self, sts, trs, lam, reward):
        '''
        Constructor
        '''
        self.States = sts
        self.Trans = trs
        self.Lamda = lam
        self.Reward = reward
        
    def setStates(self, sts):
        self.States = sts
    def setTransition(self, trs):
        self.Trans = trs
    def setLamda(self, lam):
        self.Lamda = lam
    def setReward(self, re):
        self.Reward = re;
    
    