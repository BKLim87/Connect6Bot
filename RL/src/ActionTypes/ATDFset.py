'''
Created on 2016. 6. 8.

@author: bklim
'''
from utils.MapUtils import MapUtils
from Resource.HistoryList import History

class MyClass(object):
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
        
    def doAction(self, aAction, aMap, aSide):
        if aSide == 1:
                myside = 1
                enside = 2
        else:
                myside = 2
                enside = 1
        ActionResult = []
        
        if aAction == 'two attack':
            MyLL = MapUtils.getSideLiveLongestLine(aMap, myside)
            LLtips = MapUtils.getTips(MyLL)
            
            for atip in LLtips:
                ActionResult.append(History(atip[0], atip[1], myside))
            
            if len(ActionResult) < 2:
                MyLL2 = MapUtils.getSideLiveSecondLongestLine(aMap, myside)
                LL2tips = MapUtils.getTips(MyLL2)
                ActionResult.append(History(LL2tips[0][0], LL2tips[0][1], myside))
            
        elif aAction == 'one attack one defence':            
            MyLL = MapUtils.getSideLiveLongestLine(aMap, myside)
            MyLLtips = MapUtils.getTips(MyLL)
            
            EnLL = MapUtils.getSideLiveLongestLine(aMap, enside)
            EnLLtips = MapUtils.getTips(EnLL)
            
            ActionResult.append(History(MyLLtips[0][0], MyLLtips[0][1], myside))
            ActionResult.append(History(EnLLtips[0][0], EnLLtips[0][1], myside))
        
        else:
            EnLL = MapUtils.getSideLiveLongestLine(aMap, enside)
            LLtips = MapUtils.getTips(EnLL)
            
            for atip in LLtips:
                ActionResult.append(History(atip[0], atip[1], myside))
            
            if len(ActionResult) < 2:
                EnLL2 = MapUtils.getSideLiveSecondLongestLine(aMap, enside)
                LL2tips = MapUtils.getTips(EnLL2)
                ActionResult.append(History(LL2tips[0][0], LL2tips[0][1], myside))
                
        return ActionResult
