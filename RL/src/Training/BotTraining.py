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
from Training.RewardCalculator import RewardCalculator
from utils.HistoryUtils import HistoryUtils


class BotTraining(object):
    '''
    classdocs
    '''
    def __init__(self, LO1, LO2, NoG):
        '''
        Constructor
        '''
        self.LearningObject1 = LO1
        self.LearningObject2 = LO2
        self.NumberOfGame = NoG
        self.TimeResult = [0,0]
        self.MatchResult = [0,0,0]
        
    def printWinResult(self):
        print('#draw:'+str(self.MatchResult[0])+', #BlackWin:'+str(self.MatchResult[1])+' #WhiteWin:'+str(self.MatchResult[2]))
    
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
                
            self.MatchResult[WinResult] = self.MatchResult[WinResult] + 1
            
            UpdateTimeStart = time.time()
            
            #learning this match
            bot1.update(n+1)
            bot2.update(n+1)
            
            self.TimeResult[1] = self.TimeResult[1] + (time.time() - UpdateTimeStart)
            
        #print training result
        self.printTimeResult()
        self.printWinResult()
            
        #print learning object
        self.LearningObject1.print()
                


if __name__ == "__main__":
    print('start training')
    
    LLATDF = LearningObject(LongistLineStateChanger(), ATDFset(), 1)
    
    BT = BotTraining(LLATDF, LLATDF, 1000)
    
    BT.start()
            
        