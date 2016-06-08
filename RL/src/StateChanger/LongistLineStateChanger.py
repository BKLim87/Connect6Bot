'''
Created on 2016. 6. 2.

@author: Administrator
'''
from utils.MapUtils import MapUtils

class LongistLineStateChanger(object):
    '''
    classdocs
    state = [my longest line size, enemy longest line size]
    ex)
    [3,2]
    
    all case(may be)
    [0~6, 0~6] - [6,6]
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    @staticmethod
    def getState(aMap, myside):
        BlackSideLL = MapUtils.getSideLiveLongestLineSize(aMap, 1)
        WhiteSideLL = MapUtils.getSideLiveLongestLineSize(aMap, 2)
        
        if myside == 1:
            return [BlackSideLL, WhiteSideLL]
        else:
            return [WhiteSideLL, BlackSideLL]
        
        