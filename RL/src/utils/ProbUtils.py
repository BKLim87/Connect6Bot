'''
Created on 2016. 6. 8.

@author: bklim
'''
import random

class ProbUtils(object):
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
    
    @staticmethod
    def getOnefromProblist(alist):
        arandom = random.random()
        
        for i in range(0,len(alist)):
            if arandom <= alist[i]:
                return i
            else:
                arandom = arandom - alist[i]
                
    @staticmethod
    def pickUniform(alist):
        asize = len(alist)
        return alist[random.randrange(0,asize)]