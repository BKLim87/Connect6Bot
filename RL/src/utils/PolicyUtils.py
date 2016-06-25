'''
Created on 2016. 6. 25.

@author: Administrator
'''
from utils.ProbUtils import ProbUtils 
import random

class PolicyUtils(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod
    def EGreedy(Qdic, aState, ActionType, E):
        itemlist = []
        vlist = []
        for aAction in ActionType.getActionList():
            itemlist.append(aAction)
            if Qdic.isContain(aState, aAction):
                vlist.append(Qdic.getNestedItem(aState, aAction))
            else:
                vlist.append(random.random() - 0.5)
                
        return ProbUtils.pickByEGreedy(itemlist, vlist, E)
    
    @staticmethod
    def Greedy(Qdic, aState, ActionType):
        itemlist = []
        vlist = []
        for aAction in ActionType.getActionList():
            itemlist.append(aAction)
            if Qdic.isContain(aState, aAction):
                vlist.append(Qdic.getNestedItem(aState, aAction))
            else:
                vlist.append(random.random() - 0.5)
                
        return ProbUtils.pickByArgmax(itemlist, vlist)
