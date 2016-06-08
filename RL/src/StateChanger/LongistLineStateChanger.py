'''
Created on 2016. 6. 2.

@author: Administrator
'''
from utils.MapUtils import MapUtils
from Resource.Map import Map
from StateChanger.LongestLineState import LongestLineState

class LongistLineStateChanger(object):
    '''
    classdocs
    state = [my longest line size, enemy longest line size]
    ex)
    [3,2]
    
    all case(may be)
    [0~6, 0~6]
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    @staticmethod
    def getStatebyHistory(aHistory, myside):
        aMap = Map()
        aMap.setFromHistoryList(aHistory)
        return LongistLineStateChanger.getStatebyMap(aMap, myside)
        
    @staticmethod
    def getStatebyMap(aMap, myside):
        BlackSideLL = MapUtils.getSideLiveLongestLineSize(aMap, 1)
        WhiteSideLL = MapUtils.getSideLiveLongestLineSize(aMap, 2)
        
        if myside == 1:
            return LongestLineState(BlackSideLL, WhiteSideLL)
        else:
            return LongestLineState(WhiteSideLL, BlackSideLL)
        
        