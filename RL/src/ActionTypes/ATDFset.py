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
        self.actionlist = ['two attack', 'one attack one defence','two defence']
        self.name = 'ATDF action type'
    
    @staticmethod
    def randomAction():
        ProbUtils.pickUniform(['two attack', 'one attack one defence','two defence'])
    
    @staticmethod
    def getActionList():
        return ['two attack', 'one attack one defence','two defence']
    
    @staticmethod
    def getActionName(num):
        actionlist = ['two attack', 'one attack one defence','two defence']
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
        
        if aAction == 'two attack':
            MyLL = MapUtils.getSideLiveLongestLine(aMap, myside)
            
            if len(MyLL) == 0:
                po1 = MapUtils.getRandomEmptySpace(aMap)
                po2 = MapUtils.getRandomOneNearLiveLocation(aMap, po1)
                if po2 == []:
                    po2 = MapUtils.getRandomEmptySpace(aMap)
                    while not (po1[0] == po2[0] & po1[1] ==po2[1]):
                        po2 = MapUtils.getRandomEmptySpace(aMap)
                
                ActionResult.append(History(po1[0], po1[1], myside))
                ActionResult.append(History(po2[0], po2[1], myside))
                
            else:    
                LLtips = MapUtils.getLiveTips(aMap, MyLL)            
                for atip in LLtips:
                    ActionResult.append(History(atip[0], atip[1], myside))
                
                if len(ActionResult) < 2:
                    MyLL2 = MapUtils.getSideLiveSecondLongestLine(aMap, myside)
                    if MyLL2 == []:
                        lo = MapUtils.getRandomEmptySpace(aMap)
                        ActionResult.append(History(lo[0], lo[1], myside))
                    else:
                        LL2tips = MapUtils.getLiveTips(aMap, MyLL2)
                        ActionResult.append(History(LL2tips[0][0], LL2tips[0][1], myside))
            
        elif aAction == 'one attack one defence':            
            MyLL = MapUtils.getSideLiveLongestLine(aMap, myside)
            if len(MyLL) == 0:
                po1 = MapUtils.getRandomEmptySpace(aMap)
                ActionResult.append(History(po1[0], po1[1], myside))
            else:
                MyLLtips = MapUtils.getLiveTips(aMap, MyLL)
                ActionResult.append(History(MyLLtips[0][0], MyLLtips[0][1], myside))
            
            EnLL = MapUtils.getSideLiveLongestLine(aMap, enside)
            if len(EnLL) == 0:
                po1 = MapUtils.getRandomEmptySpace(aMap)
                ActionResult.append(History(po1[0], po1[1], myside))
            else:
                EnLLtips = MapUtils.getLiveTips(aMap, EnLL)
                ActionResult.append(History(EnLLtips[0][0], EnLLtips[0][1], myside))
        
        else:
            EnLL = MapUtils.getSideLiveLongestLine(aMap, enside)
            
            if len(EnLL) == 0:
                po1 = MapUtils.getRandomEmptySpace(aMap)
                po2 = MapUtils.getRandomOneNearLiveLocation(aMap, po1)
                if po2 == []:
                    po2 = MapUtils.getRandomEmptySpace(aMap)
                    while not (po1[0] == po2[0] & po1[1] ==po2[1]):
                        po2 = MapUtils.getRandomEmptySpace(aMap)
                
                ActionResult.append(History(po1[0], po1[1], myside))
                ActionResult.append(History(po2[0], po2[1], myside))
            
            else:
                LLtips = MapUtils.getLiveTips(aMap, EnLL)
                
                for atip in LLtips:
                    ActionResult.append(History(atip[0], atip[1], myside))
                
                if len(ActionResult) < 2:
                    EnLL2 = MapUtils.getSideLiveSecondLongestLine(aMap, enside)
                    if EnLL2 == []:
                        lo = MapUtils.getRandomEmptySpace(aMap)
                        ActionResult.append(History(lo[0], lo[1], myside))
                    LL2tips = MapUtils.getLiveTips(aMap, EnLL2)
                    ActionResult.append(History(LL2tips[0][0], LL2tips[0][1], myside))
                
        return ActionResult
