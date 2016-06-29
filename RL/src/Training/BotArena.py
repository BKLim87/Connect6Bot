'''
Created on 2016. 6. 26.

@author: Administrator
'''
import random
from Resource.Bot import Bot
from Training.BotTraining import BotTraining
from Resource.LearningObject import LearningObject
from StateChanger.LongistLineStateChanger import LongistLineStateChanger
from ActionTypes.ATDFset import ATDFset
from Learning.OnPolicy.GLIE import GLIE
from Learning.OffPolicy.QLearning import QLearning

class BotArena(object):
    '''
    classdocs
    '''

    def __init__(self, OnLOlist, OFFLOlist, numberofmatch):
        '''
        Constructor
        '''
        self.OnLineLOs = OnLOlist
        self.OffLineLOs = OFFLOlist
        self.Nmatch = numberofmatch
        
    def start(self):
        for N in range(0,self.Nmatch):
            LOset1 = random.choice(self.OnLineLOs)
            LOset2 = random.choice(self.OnLineLOs)
            
            aBT = BotTraining(LOset1[0], LOset1[1], LOset2[0], LOset2[1], 1)
            aMatchHistory = aBT.start()
            
            for aOFFLO in self.OffLineLOs:
                aOFFLO.LearningPolicy.update(aOFFLO, aMatchHistory, LOset1[0], LOset2[0])
        
        self.printResult()
                
    def printResult(self):
        print('On Policy')
        for aLOset in self.OnLineLOs:
            aLOset[0].print()
        print('Off Policy')
        for aLO in self.OffLineLOs:
            aLO.print()
                
            
if __name__ == "__main__":
    print('start training')
    
    LLATDF1 = LearningObject(LongistLineStateChanger(), ATDFset, 0.95, GLIE(0))
    OFFLO1 = LearningObject(LongistLineStateChanger(), ATDFset, 1, QLearning(0.005))
    
    aBA = BotArena([[LLATDF1, True]], [OFFLO1], 25)
    aBA.start()
    
                     
        