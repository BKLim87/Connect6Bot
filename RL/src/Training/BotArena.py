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
from Learning.NoLearningPolicy import NoLearningPolicy

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
        self.saveLearningObjects()
        
        LOlist = []
        for aLOset in self.OnLineLOs:
            LOlist.append(aLOset[0])
        for aLO in self.OffLineLOs:
            LOlist.append(aLO)
        
        self.Arena(LOlist, 10)
                
    def printResult(self):
        print('On Policy')
        for aLOset in self.OnLineLOs:
            aLOset[0].print()
        print('Off Policy')
        for aLO in self.OffLineLOs:
            aLO.print()
            
    def Arena(self, LOlist, Nmatch):
        LOLength = len(LOlist)
        for aLO in LOlist:
            aLO.LearningPolicy = NoLearningPolicy()
        
        MatchResult = []
        for j in range(0, LOLength):
            templist = []
            for i in range(0, LOLength):
                templist.append(0)        
            MatchResult.append(templist)
        
        for i in range(0, LOLength):
            for j in range(i, LOLength):
                if not i == j:
                    BT = BotTraining(LOlist[i], False, LOlist[j], False, Nmatch)
                    BT.start()
                    MatchResult[i][j] = round(BT.MatchResult.getNwin()[0]/Nmatch,3)
                    MatchResult[j][i] = round(BT.MatchResult.getNwin()[1]/Nmatch,3)
                    
        print(MatchResult)
    
    def saveLearningObjects(self):
        for aLOset in self.OnLineLOs:
            if aLOset[1]:
                aLOset[0].save_object()    
        for aLO in self.OffLineLOs:
            aLO.save_object()    
            
if __name__ == "__main__":
    print('start training')
    
    LLATDF1 = LearningObject(LongistLineStateChanger(), ATDFset, 0.95, GLIE(0))
    OFFLO1 = LearningObject(LongistLineStateChanger(), ATDFset, 0.95, QLearning(0.005))
    OFFLO2 = LearningObject(LongistLineStateChanger(), ATDFset, 1, QLearning(0.005))
    
    aBA = BotArena([[LLATDF1, True]], [OFFLO1, OFFLO2], 100)
    aBA.start()
    
                     
        