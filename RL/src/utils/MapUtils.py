'''
Created on 2016. 6. 2.

@author: Administrator
'''

import random

class MapUtils(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    @staticmethod
    def getSideMapArray(aMap, side):
        SideMA = aMap.copyMapArray()
        
        for i in range(0,19):
            for j in range(0,19):
                if side != SideMA[i][j]:
                    SideMA[i][j] = 0
        
        return SideMA
    
    @staticmethod
    def isStopped(aMap, aline):
        '''
        aline example:
        ['vertical',[[3,5],3],1]
        direction, start point, size, side
        '''
        
        aMA = aMap.copyMapArray()
        aTips = MapUtils.getTips(aline)
        
        bflag = True
        
        for atip in aTips:
            if aMA[atip[0]][atip[1]] == 0:
                bflag = bflag & False
            else:
                bflag = bflag & True
        
        return bflag 
    
    @staticmethod
    def getLiveTips(aMap, aline):
        tips = MapUtils.getTips(aline)
        livetips = []
        for ati in tips:
            if MapUtils.isEmpty(aMap, ati):
                livetips.append(ati)
        return livetips
        
    
    @staticmethod
    def getTips(aline):
        '''
        aline example:
        ['vertical',[[3,5],3],1]
        direction, start point, size, side
        '''
        Tips = []
        if aline[0] == 'vertical':
            Tips = [[aline[1][0][0]-1,aline[1][0][1]],[aline[1][0][0]+aline[1][1],aline[1][0][1]]]
            pass
        elif aline[0] == 'horizontal':
            Tips = [[aline[1][0][0],aline[1][0][1]-1],[aline[1][0][0],aline[1][0][1]+aline[1][1]]]
            pass
        elif aline[0] == 'diagonal':
            Tips = [[aline[1][0][0]-1,aline[1][0][1]-1],[aline[1][0][0]+aline[1][1],aline[1][0][1]+aline[1][1]]]
            pass
        elif aline[0] == 'cross':
            Tips = [[aline[1][0][0]+1,aline[1][0][1]-1],[aline[1][0][0]-aline[1][1],aline[1][0][1]+aline[1][1]]]
            pass
        
        for i in [1,0]:
            for j in [0,1]:
                if Tips[i][j] == -1 or Tips[i][j] == 19:
                    del Tips[i]
        
        return Tips
    
    @staticmethod
    def getSideLiveSecondLongestLine(aMap, side):
        livelines = MapUtils.getSideLiveLines(aMap, side)
        
        if len(livelines) < 2:
            return []
        
        aLongest = livelines[0]
        aSecond = livelines[1]
        
        for aline in livelines:
            if aLongest[1][1] <= aline[1][1]:
                aSecond = aLongest
                aLongest = aline
            elif aSecond[1][1] < aline[1][1]:
                aSecond = aline
        
        return aSecond
    
    @staticmethod
    def getSideLiveLongestLineSize(aMap, side):
        aLL = MapUtils.getSideLiveLongestLine(aMap, side)
        if aLL == []:
            return 0
        else:
            return aLL[1][1]
            
    @staticmethod
    def getSideLiveLongestLine(aMap, side):
        livelines = MapUtils.getSideLiveLines(aMap, side)
        
        if len(livelines) == 0:
            return []
        
        aLongest = livelines[0]
        
        for aline in livelines:
            if aLongest[1][1] < aline[1][1]:
                aLongest = aline
        
        return aLongest
    
    @staticmethod
    def getSideLiveLines(aMap, side):
        allLines = MapUtils.getSideLines(aMap, side)
        livelines = []
        
        for aline in allLines:
            if MapUtils.isStopped(aMap, aline) == False:
                livelines.append(aline)
        
        return livelines
    
    @staticmethod
    def getSideLines(aMap, side):
        SideMA1 = MapUtils.getSideMapArray(aMap, side)
        SideMA2 = MapUtils.getSideMapArray(aMap, side)
        SideMA3 = MapUtils.getSideMapArray(aMap, side)
        SideMA4 = MapUtils.getSideMapArray(aMap, side)
        
        Lines = []
        
        tempvertical = []
        for i in range(0,14):
            for j in range(0,19):
                if SideMA1[i][j] == side:
                    for x in range(0,6):
                        if SideMA1[i+x][j] == side:
                            SideMA1[i+x][j] = 0
                            if x == 5:
                                tempvertical.append([[i,j], 6])
                                break
                            
                        else:
                            tempvertical.append([[i,j],x])
                            break
        for ttemp in tempvertical:
            Lines.append(['vertical', ttemp, side])
        
        temphorizontal = []
        for i in range(0,19):
            for j in range(0,14):
                if SideMA2[i][j] == side:
                    for x in range(0,6):
                        if SideMA2[i][j+x] == side:
                            SideMA2[i][j+x] = 0
                            if x == 5:
                                temphorizontal.append([[i,j], 6])
                                break
                            
                        else:
                            temphorizontal.append([[i,j],x])
                            break
        for ttemp in temphorizontal:
            Lines.append(['horizontal', ttemp, side])
        
        tempdiagonal = []
        for i in range(0,14):
            for j in range(0,14):
                if SideMA3[i][j] == side:
                    for x in range(0,6):
                        if SideMA3[i+x][j+x] == side:
                            SideMA3[i+x][j+x] = 0
                            if x == 5:
                                tempdiagonal.append([[i,j], 6])
                                break
                            
                        else:
                            tempdiagonal.append([[i,j],x])
                            break
        for ttemp in tempdiagonal:
            Lines.append(['diagonal', ttemp, side])
        
        tempcross = []
        for i in range(5,19):
            for j in range(0,14):
                if SideMA4[i][j] == side:
                    for x in range(0,6):
                        if SideMA4[i-x][j+x] == side:
                            SideMA4[i-x][j+x] = 0
                            if x == 5:
                                tempcross.append([[i,j], 6])
                                break
                            
                        else:
                            tempcross.append([[i,j],x])
                            break
        for ttemp in tempcross:
            Lines.append(['cross', ttemp, side])
        
        return Lines
    
    @staticmethod
    def isEmpty(aMap, loc):
        if aMap.MapArray[loc[0]][loc[1]] == 0:
            return True;
        return False;
    
    @staticmethod
    def getStone(aMap, loc):
        return aMap.MapArray[loc[0]][loc[1]]
    
    @staticmethod
    def getRandomEmptySpace(aMap):
        aloc = [random.randrange(0,19), random.randrange(0,19)]
        while MapUtils.isEmpty(aMap, aloc) == False:
            aloc = [random.randrange(0,19), random.randrange(0,19)]
        return aloc
    
    @staticmethod
    def getWinSide(aMap):
        if MapUtils.getSideLiveLongestLineSize(aMap, 1) >= 6:
            return 1
        elif MapUtils.getSideLiveLongestLineSize(aMap, 2) >= 6:
            return 2
        return 0
                                
                            