'''
Created on 2016. 6. 8.

@author: bklim
'''
import random
from Resource.Bot import Bot
from Resource.LearningObject import LearningObject
from Resource.Map import Map
from utils.MapUtils import MapUtils
from Resource.HistoryList import HistoryList
from StateChanger.LongistLineStateChanger import LongistLineStateChanger
from ActionTypes.ATDFset import ATDFset
from Training.RewardCalculator import RewardCalculator


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
            
            #start one match
            while(MapUtils.getWinSide(aMap) == 0):
                turnbot = bot1
                if bot1.side != Turn:
                    turnbot = bot2
                    
                turnstate = turnbot.LearningObject.StateChanger.getStatebyHistory(aHistory, Turn)
                turnaction = turnbot.LearningObject.getAction(turnstate)
                turnphase = turnbot.LearningObject.ActionType.doActionByHistory(turnaction, aHistory, Turn)
                aHistory.updatePhase(turnphase)
                aMap.setFromHistoryList(aHistory)
                
                turnbot.StateActionRewardList.append([aMap.Copy(), turnaction, RewardCalculator.getReward(aMap, turnaction, turnbot)])
                
                if Turn == 2:
                    Turn = 1
                else:
                    Turn = 2
            
            losebot = bot1
            if bot1.side != Turn:
                losebot = bot2
            losebot.putLoseReward()
            
            bot1.update()
            bot2.update()
            
            #print this match
            print(aHistory)
            
            #learning this match
            

if __name__ == "__main__":
    print('start training')
    
    LLATDF = LearningObject(LongistLineStateChanger(), ATDFset(), 1)
    
    BT = BotTraining(LLATDF, LLATDF, 100)
    
    BT.start()
            
        