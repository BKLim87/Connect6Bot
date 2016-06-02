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
    def getSideLines(aMap, side):
        SideMA = MapUtils.getSideMapArray(aMap, side)
        
        Lines = {}
        
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
        Lines.put('vertical', tempvertical)
        
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
        Lines.put('horizontal', temphorizontal)
        
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
        Lines.put('diagonal', tempdiagonal)
                                
                            