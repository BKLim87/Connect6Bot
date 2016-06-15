'''
Created on 2016. 6. 8.

@author: bklim
'''
from utils.MapUtils import MapUtils
from Resource.HistoryList import History
from Resource.Map import Map
from utils.ProbUtils import ProbUtils

class ATDFset(object):
    '''
    classdocs
    list: two attack, one attack one defence, two defence
    two attack: use all 2 stones to my side longest line
    one attack one defence: use to my side longest line and enemy's side longest line
    two defence: use all 2 stones to enemy's side longest line 
    '''

    def __init__(self):
        '''
        Constructor
        '''
        '''
        self.actionlist = ['2A', '1A1D','2D']
        self.name = 'ATDF action type'
        '''
    
    @staticmethod
    def getName():
        return 'ATDF action type'
    
    @staticmethod
    def randomAction():
        ProbUtils.pickUniform( ATDFset.getActionList())
    
    @staticmethod
    def getActionList():
        return ['2A', '1A1D','2D']
    
    @staticmethod
    def getActionName(num):
        actionlist =  ATDFset.getActionList()
        return actionlist[num]
    
    @staticmethod 
    def doActionByHistory(aAction, aHistory, aSide):
        aMap = Map()
        aMap.setFromHistoryList(aHistory)
        return ATDFset.doActionByMap(aAction, aMap, aSide)
    
    @staticmethod 
    def doActionByMap(aAction, aMap, aSide):
        if aSide == 1:
                myside = 1
                enside = 2
        else:
                myside = 2
                enside = 1
        ActionResult = []
        POs = []
        
        if aAction == ATDFset.getActionList()[0]:
            MyLL = MapUtils.getSideLiveLongestLine(aMap, myside)
            
            if len(MyLL) == 0:
                POs.append(MapUtils.getRandomEmptySpace(aMap))
                POs.append(MapUtils.getRandomOneNearLiveLocation(aMap, POs[0]))
                if POs[1] == []:
                    POs[1] = MapUtils.getRandomEmptySpace(aMap)
                
            else:    
                LLtips = MapUtils.getLiveTips(aMap, MyLL)            
                for atip in LLtips:
                    POs.append(atip)
                
                if len(POs) < 2:
                    aTE = MapUtils.getLiveTipExtension(aMap, MyLL, POs[0])
                    if not aTE == []:
                        POs.append(aTE)
                    else:
                        MyLL2 = MapUtils.getSideLiveSecondLongestLine(aMap, myside)
                        if MyLL2 == []:
                            POs.append(MapUtils.getRandomEmptySpace(aMap))
                        else:
                            POs.append(MapUtils.getLiveTips(aMap, MyLL2)[0])
            
            
            
        elif aAction ==  ATDFset.getActionList()[1]:            
            MyLL = MapUtils.getSideLiveLongestLine(aMap, myside)
            if len(MyLL) == 0:
                POs.append(MapUtils.getRandomEmptySpace(aMap))
            else:
                POs.append(MapUtils.getLiveTips(aMap, MyLL)[0])
            
            EnLL = MapUtils.getSideLiveLongestLine(aMap, enside)
            if len(EnLL) == 0:
                POs.append(MapUtils.getRandomEmptySpace(aMap))
            else:
                POs.append(MapUtils.getLiveTips(aMap, EnLL)[0])
                
        else:
            EnLL = MapUtils.getSideLiveLongestLine(aMap, enside)
            
            if len(EnLL) == 0:
                POs.append(MapUtils.getRandomEmptySpace(aMap))
                POs.append(MapUtils.getRandomOneNearLiveLocation(aMap, POs[0]))
                if POs[1] == []:
                    POs[1] = MapUtils.getRandomEmptySpace(aMap)
                
            else:    
                LLtips = MapUtils.getLiveTips(aMap, EnLL)            
                for atip in LLtips:
                    POs.append(atip)
                
                if len(POs) < 2:
                    EnLL2 = MapUtils.getSideLiveSecondLongestLine(aMap, enside)
                    if EnLL2 == []:
                        POs.append(MapUtils.getRandomEmptySpace(aMap))
                    else:
                        POs.append(MapUtils.getLiveTips(aMap, EnLL2)[0])
        
        ActionResult.append(History(POs[0][0], POs[0][1], myside))
        if POs[0] == POs[1]:
            POs[1] = MapUtils.getRandomEmptySpaceExceptOne(aMap, POs[0])
        ActionResult.append(History(POs[1][0], POs[1][1], myside))
        
        return ActionResult
