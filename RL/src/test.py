'''
Created on 2016. 6. 8.

@author: bklim
'''
from Resource.HistoryList import HistoryList
from Resource.Map import Map
from StateChanger.LongistLineStateChanger import LongistLineStateChanger

if __name__ == "__main__":
    testString = '9,9,1;10,10,2;11,11,2'
    
    aHL = HistoryList(testString)
    print(aHL)
    aMap = Map()
    aMap.setFromHistoryList(aHL)
    print(aMap)
    
    llst = LongistLineStateChanger.getState(aMap, 1)
    print(llst)
    
    print('hello world')