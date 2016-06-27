'''
Created on 2016. 6. 23.

@author: bklim
'''
import sys

sys.path.append('../')

from Resource.LearningObject import LearningObject
from ActionTypes.ATDFset import ATDFset
from ActionTypes.ATDFRset import ATDFRset
from Training.BotTraining import BotTraining
from StateChanger.LongistLineStateChanger import LongistLineStateChanger
from Learning.OnPolicy.GLIE import GLIE


print('start training')

LLATDF1 = LearningObject(LongistLineStateChanger(), ATDFset(GLIE(0)), 1)
LLATDF09 = LearningObject(LongistLineStateChanger(), ATDFset(GLIE(0)), 0.9)
LLATDFR1 = LearningObject(LongistLineStateChanger(), ATDFRset(GLIE(0)), 1)
LLATDFR09 = LearningObject(LongistLineStateChanger(), ATDFRset(GLIE(0)), 0.9)

BT = BotTraining(LLATDF09, True, LLATDF09, True, 5000)
BT.start()
BT = BotTraining(LLATDFR09, True, LLATDFR09, True, 5000)
BT.start()
