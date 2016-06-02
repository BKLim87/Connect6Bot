'''
Created on 2016. 6. 2.

@author: Administrator
'''
from src.utils.MapUtils import MapUtils

class LongistLineStateChanger(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    @staticmethod
    def getState(aMap):
        BlackSideMA = MapUtils.getSideMapArray(aMap, 1)
        WhiteSideMA = MapUtils.getSideMapArray(aMap, 2)
        
        