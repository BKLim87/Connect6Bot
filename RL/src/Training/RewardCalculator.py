'''
Created on 2016. 6. 8.

@author: Administrator
'''
from utils.MapUtils import MapUtils
from Resource.Map import Map

class RewardCalculator(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    @staticmethod
    def getReward(aMap, aAction, abot):
        winflag = MapUtils.getWinSide(aMap)
        
        #not finished
        if winflag == 0:
            return 0
        #this bot win
        elif winflag == abot.side:
            return 1
        #other bot win
        else:
            return -1
        
    @staticmethod
    def getRewardbyHistory(aHistory, aAction, abot):
        aMap = Map()
        aMap.setFromHistoryList(aHistory)
        return RewardCalculator.getReward(aMap, aAction, abot)
    
    @staticmethod
    def getLoseReward():
        return -1