'''
Created on 2016. 6. 8.

@author: Administrator
'''

class LongestLineState(object):
    '''
    classdocs
    state = [my longest line size, enemy longest line size]
    ex)
    [3,2]
    
    all case(may be)
    [0~6, 0~6]
    '''

    def __init__(self, myL, enL):
        '''
        Constructor
        '''
        self.myLL = myL
        self.enLL = enL
        
    def __hash(self):
        return hash(self.__key())
    
    def __key(self):
        return (self.myLL, self.enLL)
    
    def getState(self):
        return  (self.myLL, self.enLL)