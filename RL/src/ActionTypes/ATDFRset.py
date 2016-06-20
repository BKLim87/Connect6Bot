'''
Created on 2016. 6. 20.

@author: bklim
'''

from utils.MapUtils import MapUtils
from Resource.HistoryList import History
from Resource.Map import Map
from utils.ProbUtils import ProbUtils
from ActionTypes.ATDFset import ATDFset

class ATDFRset(object):
    '''
    classdocs
    list: two attack, one attack one defence, two defence
    two attack: use all 2 stones to my side longest line
    one attack one defence: use to my side longest line and enemy's side longest line
    two defence: use all 2 stones to enemy's side longest line
    Random: use all 2 stones randomly 
    '''

    def __init__(self):
        '''
        self.actionlist = ['2A', '1A1D','2D', 'R']
        self.name = 'ATDFR action type'
        '''
    
    @staticmethod
    def getName():
        return 'ATDFR action type'
    
    @staticmethod
    def randomAction():
        ProbUtils.pickUniform( ATDFRset.getActionList())
    
    @staticmethod
    def getActionList():
        return ['2A', '1A1D','2D', 'R']
    
    @staticmethod
    def getActionName(num):
        actionlist =  ATDFRset.getActionList()
        return actionlist[num]
    
    @staticmethod 
    def doActionByHistory(aAction, aHistory, aSide):
        aMap = Map()
        aMap.setFromHistoryList(aHistory)
        return ATDFRset.doActionByMap(aAction, aMap, aSide)
    
    @staticmethod 
    def doActionByMap(aAction, aMap, aSide):
        if aSide == 1:
                myside = 1
                enside = 2
        else:
                myside = 2
                enside = 1
        ActionResult = []
        POs = [[],[]]
        
        if aAction in ATDFset.getActionList():
            return ATDFset.doActionByMap(aAction, aMap, aSide)
                        
        else:
            POs[0] = MapUtils.getRandomEmptySpace(aMap)
            POs[1] = MapUtils.getRandomEmptySpaceExceptOne(aMap, POs[0])
            ActionResult.append(History(POs[0][0], POs[0][1], myside))
            ActionResult.append(History(POs[1][0], POs[1][1], myside))
            return ActionResult
