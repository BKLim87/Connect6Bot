'''
Created on 2016. 6. 8.

@author: bklim
'''
import random
import time
from Resource.Bot import Bot
from Resource.LearningObject import LearningObject
from Resource.Map import Map
from utils.MapUtils import MapUtils
from Resource.HistoryList import HistoryList
from StateChanger.LongistLineStateChanger import LongistLineStateChanger
from ActionTypes.ATDFset import ATDFset
from ActionTypes.ATDFRset import ATDFRset
from Training.RewardCalculator import RewardCalculator
from utils.HistoryUtils import HistoryUtils
from utils.MatchResult import MatchResult
from Learning.OnPolicy.GLIE import GLIE
from Learning.OnPolicy.EGreedy import EGreedy

class BotTraining(object):
    '''
    classdocs
    '''
    def __init__(self, LO1, LF1, LO2, LF2, NoG):
        '''
        Constructor
        '''
        self.LearningObject1 = LO1
        self.LearningFlag1 = LF1
        self.LearningObject2 = LO2
        self.LearningFlag2 = LF2
        self.NumberOfGame = NoG
        self.TimeResult = [0,0]
        self.MatchResult = MatchResult(LO1, LO2)
        
    def printTimeResult(self):
        TotalTime = sum(self.TimeResult)
        SimulateTime = self.TimeResult[0]
        UpdateTime = self.TimeResult[1]
        RatioSU = SimulateTime/UpdateTime
        
        print('TotalTime:'+str(TotalTime)+'s, SimulateTime: '+str(SimulateTime)+'s, UpdateTime:'+str(UpdateTime)+'s, Ratio(S/R):'+str(RatioSU))
        
    def start(self):
        for n in range(0,self.NumberOfGame):
            bot1side = random.randrange(1,3)
            if bot1side == 1:
                bot2side = 2
            else:
                bot2side = 1
            
            #set to start
            bot1 = Bot(self.LearningObject1, bot1side)
            bot2 = Bot(self.LearningObject2, bot2side)
            aHistory = HistoryList('9,9,1')
            aMap = Map()
            aMap.setFromHistoryList(aHistory)            
            Turn = 2
            
            SimulTimeStart = time.time()
            #start one match
            while(MapUtils.getWinSide(aMap) == 0):
                if HistoryUtils.isDraw(aHistory):
                    break
                
                else:
                    turnbot = bot1
                    if bot1.side != Turn:
                        turnbot = bot2
                        
                    turnstate = turnbot.LearningObject.StateChanger.getStatebyHistory(aHistory, Turn)
                    turnaction = turnbot.LearningObject.getAction(turnstate)
                    turnphase = turnbot.LearningObject.ActionType.doActionByHistory(turnaction, aHistory, Turn)
                    turnMap = aMap.Copy()
                    
                    aHistory.updatePhase(turnphase)
                    aMap.setFromHistoryList(aHistory)
                    
                    turnbot.StateActionRewardList.append([turnMap, turnaction, RewardCalculator.getReward(aMap, turnaction, turnbot)])
                    
                    if Turn == 2:
                        Turn = 1
                    else:
                        Turn = 2
            self.TimeResult[0] = self.TimeResult[0] + (time.time() - SimulTimeStart)
            
            #print this match
            print('Length:'+str(aHistory.size())+' Log:'+str(aHistory))
            
            WinResult = MapUtils.getWinSide(aMap)
            if WinResult == 0:
                pass
            else:
                if bot1.side == WinResult:
                    losebot = bot2
                else:
                    losebot = bot1
                losebot.putLoseReward()
                
            self.MatchResult.update(bot1, bot2, WinResult)
            
            UpdateTimeStart = time.time()
            
            #learning this match
            if self.LearningFlag1:
                bot1.update()
            if self.LearningFlag2:
                bot2.update()
            
            self.TimeResult[1] = self.TimeResult[1] + (time.time() - UpdateTimeStart)
            
        #print training result
        self.printTimeResult()
        self.MatchResult.print()
            
        #print learning object
        self.LearningObject1.print()
        self.LearningObject2.print()
        
        if self.LearningFlag1:
            print('save LearningObject1')
            self.LearningObject1.save_object()
        if self.LearningFlag2:
            print('save LearningObject2')
            self.LearningObject2.save_object()
                


if __name__ == "__main__":
    print('start training')
    
    LLATDF1 = LearningObject(LongistLineStateChanger(), ATDFset, 0.95, GLIE(0))
    LLATDFR1 = LearningObject(LongistLineStateChanger(), ATDFRset(), 0.95, EGreedy(0.2, 0.003))
    LO1 = LLATDF1
    LO2 = LLATDFR1
    
    BT = BotTraining(LO2, True, LO2, True, 2000)
    
    BT.start()
            
        