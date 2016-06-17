import sys

sys.path.append('../')

from Resource.Bot import Bot
from Resource.HistoryList import HistoryList
from Resource.Map import Map

print('start get a action from saved policy')

if len(sys.argv) == 4:
    SavedLOpath = sys.argv[1]
    Side = sys.argv[2]
    HistoryTxt = sys.argv[3]
    
    aBot = Bot('','')
    aBot.loadSavedLearningObject(SavedLOpath, Side)
    
    aHistoryList = HistoryList(HistoryTxt)
    aMap = Map()
    aMap.setFromHistoryList(aHistoryList)
    
    turnstate = aBot.LearningObject.StateChanger.getStatebyHistory(aHistoryList, Side)
    turnaction = aBot.LearningObject.getAction(turnstate)
    turnphase = aBot.LearningObject.ActionType.doActionByHistory(turnaction, aHistoryList, Side)
    
    print(str(turnphase[0])+';'+str(turnphase[1]))
    

else:
    print('usage: python getOneActionScript "Learning Object file path" "Side" "History Text"')
    pass

