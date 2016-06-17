import sys

sys.path.append('../')

from Resource.LearningObject import LearningObject
from ActionTypes.ATDFset import ATDFset
from Training.BotTraining import BotTraining
from StateChanger.LongistLineStateChanger import LongistLineStateChanger

print('start simple training')

if len(sys.argv) == 2:
    print('start training')
    
    TrainingLength = int(sys.argv[1])
    
    LLATDF = LearningObject(LongistLineStateChanger(), ATDFset(), 1)
    
    BT = BotTraining(LLATDF, LLATDF, TrainingLength)
    
    BT.start()
    
    LLATDF.save_object()
    

else:
    print('usage: python TrainingScript #size')
    pass

