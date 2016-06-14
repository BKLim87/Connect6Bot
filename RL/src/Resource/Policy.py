'''
Created on 2016. 6. 13.

@author: bklim
'''
from utils.ProbUtils import ProbUtils

class Policy(object):
    '''
    classdocs
    a probability to pick action A in state S
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.dict = dict()
        
    def getAction(self, state, ActionType):
        if state in self.dict:
            apl = self.dict.get(state)
            return ProbUtils.pickFromItemProbList(apl[0], apl[1])
        
        else:
            return ProbUtils.pickUniform(ActionType.getActionList())
        
    def update(self, state, aplist):
        self.dict[state] = aplist
        
    def __str__(self):
        astr = '{'
        
        for akey in self.dict.keys():
            astr = astr + str(akey) + '=' + str(self.dict.get(akey))+', '
        
        astr = astr + '}'
        return astr
    
    def toStringSimply(self):
        astr = '{'
        
        for akey in self.dict.keys():
            aplist = self.dict.get(akey)
            astr = astr + str(akey) + '=' + ProbUtils.pickByArgmax(aplist[0], aplist[1])+', '
        
        astr = astr + '}'
        return astr
        