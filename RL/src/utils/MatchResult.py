'''
Created on 2016. 6. 20.

@author: bklim
'''

class MatchResult(object):
    '''
    classdocs
    '''


    def __init__(self, L1, L2):
        '''
        Constructor
        Result
        [0][0] = LO1,black, [win, draw]
        [0][1] = LO1, white, ...
        [1][0] = LO2, black
        [1][1] = LO2, white
        '''
        self.LO1 = L1
        self.LO2 = L2
        self.Result = [[[0,0],[0,0]],[[0,0],[0,0]]]
        
    def update(self, bot1, bot2, winside):
        if winside == 0:
            self.Result[self.numLO(bot1)][self.numColor(bot1)][1] += 1
            self.Result[self.numLO(bot2)][self.numColor(bot2)][1] += 1
            
        else:
            if winside == bot1.side:
                self.Result[self.numLO(bot1)][self.numColor(bot1)][0] += 1
            else:
                self.Result[self.numLO(bot2)][self.numColor(bot2)][0] += 1
                
    def numLO(self, bot):
        if bot.LearningObject == self.LO1:
            return 0
        else:
            return 1
        
    def numColor(self, bot):
        if bot.side == 1:
            return 0
        else:
            return 1
    
    def getNwin(self):
        return [self.Result[0][0][0]+self.Result[0][1][0], self.Result[1][0][0]+self.Result[1][1][0]]
        
    def print(self):
        print('LO1:'+self.LO1.getName()+', LO2:'+self.LO2.getName())
        print("by color: #Black_win %d, #White_win %d, #Draw %d" % (self.Result[0][0][0]+self.Result[1][0][0], self.Result[0][1][0]+self.Result[1][1][0], self.Result[0][0][1]+self.Result[0][1][1]))
        print("by Learning Object: #LO1_win %d, #LO2_win %d, #Draw %d" % (self.Result[0][0][0]+self.Result[0][1][0], self.Result[1][0][0]+self.Result[1][1][0], self.Result[0][0][1]+self.Result[0][1][1]))
        
        
    