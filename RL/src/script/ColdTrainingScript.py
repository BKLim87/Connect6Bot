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

LLATDF09 = LearningObject(LongistLineStateChanger(), ATDFset, 0.9, GLIE(0))
LLATDFR09 = LearningObject(LongistLineStateChanger(), ATDFRset, 0.9, GLIE(0))

BT = BotTraining(LLATDF09, True, LLATDF09, True, 10000)
BT.start()
BT = BotTraining(LLATDFR09, True, LLATDFR09, True, 10000)
BT.start()
