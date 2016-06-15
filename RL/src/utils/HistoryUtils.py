'''
Created on 2016. 6. 15.

@author: bklim
'''
from utils.MapUtils import MapUtils
from Resource.Map import Map

class HistoryUtils(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    @staticmethod
    def isDraw(aHistory):
        if aHistory.size() == 19*19:
            aMap = Map()
            aMap.setFromHistoryList(aHistory)
            if MapUtils.getWinSide(aMap) == 0:
                return True
        return False