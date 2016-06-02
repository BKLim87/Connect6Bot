'''
Created on 2016. 6. 2.

@author: Administrator
'''

class HistoryList(object):
    '''
    classdocs
    '''

    def __init__(self, strr):
        '''
        Constructor
        string example
        9,9,1;10,10,2;11,11,2
        '''
        
        self.historylist = []
        
        lines = strr.split(';')
        for aline in lines:
            temp = aline.split(',')
            self.historylist.append(History(int(temp[0]), int(temp[1]), int(temp[2])))
        
        
class History(object):
    def __init__(self, tx, ty, tvalue):
        self.x = tx
        self.y = ty
        self.value = tvalue
        
