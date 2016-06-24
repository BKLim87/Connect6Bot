'''
Created on 2016. 6. 24.

@author: bklim
'''
import sys
import os

sys.path.append('../')

from Resource.LearningObject import LearningObject

print('Print Saved Learning Object')
print()

tempLO = LearningObject('', '','')
for file in os.listdir('../../LearningData'):
    if file.endswith('.LO'):
        print('File Name: '+file)
        tempLO.load_object('../../LearningData/'+file)
        tempLO.print()
        print()
