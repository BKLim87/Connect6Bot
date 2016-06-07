'''
Created on 2016. 6. 2.

@author: Administrator
'''

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
            if aMA[atip[0]][atip[1]] != aline[2]:
                bflag = True
            else:
                bflag = False
        
        return bflag 
    
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
            Tips = [[aline[1][0][0],aline[1][0][1]-1],[aline[1][0][0],aline[1][1]+aline[1][1]]]
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
    def getSideLiveLongestLineSize(aMap, side):
        return MapUtils.getSideLiveLongestLine(aMap, side)[1][1]
            
    @staticmethod
    def getSideLiveLongestLine(aMap, side):
        livelines = MapUtils.getSideLiveLines(aMap, side)
        
        aLongest = livelines[0]
        
        for aline in livelines:
            if aLongest[1][1] < aline[1][1]:
                aLongest = aline
        
        return aline
    
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
        SideMA = MapUtils.getSideMapArray(aMap, side)
        
        Lines = []
        
        tempvertical = []
        for i in range(0,14):
            for j in range(0,19):
                if SideMA[i][j] == side:
                    for x in range(0,6):
                        if SideMA[i+x][j] == side:
                            SideMA[i+x][j] = 0
                            if x == 5:
                                tempvertical.append([i,j], 6)
                                break
                            
                        else:
                            tempvertical.append([[i,j],x])
                            break
        for ttemp in tempvertical:
            Lines.append(['vertical', ttemp, side])
        
        temphorizontal = []
        for i in range(0,19):
            for j in range(0,14):
                if SideMA[i][j] == side:
                    for x in range(0,6):
                        if SideMA[i][j+x] == side:
                            SideMA[i][j+x] = 0
                            if x == 5:
                                temphorizontal.append([i,j], 6)
                                break
                            
                        else:
                            temphorizontal.append([[i,j],x])
                            break
        for ttemp in temphorizontal:
            Lines.append(['horizontal', ttemp, side])
        
        tempdiagonal = []
        for i in range(0,14):
            for j in range(0,14):
                if SideMA[i][j] == side:
                    for x in range(0,6):
                        if SideMA[i+x][j+x] == side:
                            SideMA[i+x][j+x] = 0
                            if x == 5:
                                tempdiagonal.append([i,j], 6)
                                break
                            
                        else:
                            tempdiagonal.append([[i,j],x])
                            break
        for ttemp in tempdiagonal:
            Lines.append(['diagonal', ttemp, side])
        
        tempcross = []
        for i in range(5,19):
            for j in range(0,14):
                if SideMA[i][j] == side:
                    for x in range(0,6):
                        if SideMA[i-x][j+x] == side:
                            SideMA[i-x][j+x] = 0
                            if x == 5:
                                tempcross.append([i,j], 6)
                                break
                            
                        else:
                            tempcross.append([[i,j],x])
                            break
        for ttemp in tempcross:
            Lines.append(['cross', ttemp, side])
        
        return Lines
                                
                            