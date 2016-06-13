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
        
        if strr != '':
            lines = strr.split(';')
            for aline in lines:
                temp = aline.split(',')
                self.historylist.append(History(int(temp[0]), int(temp[1]), int(temp[2])))
    
    def updatePhase(self, phases):
        for aph in phases:
            self.historylist.append(aph)
    
    def __str__(self):
        astr = ''
        for a in self.historylist:
            astr = astr + a.__str__() + ';'
        return astr
    
    def size(self):
        return len(self.historylist)
        
        
class History(object):
    def __init__(self, tx, ty, tvalue):
        self.x = tx
        self.y = ty
        self.value = tvalue
        
    def __str__(self):
        return str(self.x)+','+str(self.y)+','+str(self.value)
