'''
Created on 2016. 6. 26.

@author: Administrator
'''

class BotArena(object):
    '''
    classdocs
    '''


    def __init__(self, OnLOlist, OFFLOlist, numberofmatch):
        '''
        Constructor
        '''
        self.OnLineLOs = OnLOlist
        self.OffLineLOs = OFFLOlist
        self.Nmatch = numberofmatch