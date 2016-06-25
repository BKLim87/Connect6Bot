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
    def randomProbList(size):
        plist = []
        for i in range(0,size):
            plist.append(random.random())
        
        ssum = sum(plist)
        for i in range(0,size):
            plist[i] = plist[i]/ssum
        
        return plist
    
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
        if asize == 0:
            return []
        else:
            return alist[random.randrange(0,asize)]
    
    @staticmethod
    def pickFromItemProbList(item_list, plist):
        nth = ProbUtils.getOnefromProblist(plist)
        return item_list[nth]
    
    @staticmethod
    def pickByArgmax(item_list, plist):
        maxth = 0
        maxvalue = plist[maxth]
        for i in range(0,len(plist)):
            if maxvalue <= plist[i]:
                maxth = i
                maxvalue = plist[i]
        return item_list[maxth]
    
    @staticmethod
    def pickByEGreedy(item_list, plist, ee):
        maxth = 0
        maxvalue = plist[maxth]
        eplist = []
        Nitem = len(item_list)
        
        for i in range(0,Nitem):
            eplist.append(ee/Nitem)
            if maxvalue <= plist[i]:
                maxth = i
                maxvalue = plist[i]
                
        eplist[maxth] = eplist[maxth] + 1 - ee
        
        return ProbUtils.pickFromItemProbList(item_list, eplist)
    
    @staticmethod
    def pickByGLIE(item_list, plist, kth_episode):
        return ProbUtils.pickByEGreedy(item_list, plist, 1/kth_episode)
    
    @staticmethod
    def changetoGLIE(item_list, vlist, kth_episode):
        ee = 1/kth_episode
        maxth = 0
        maxvalue = vlist[maxth]
        eplist = []
        Nitem = len(item_list)
        
        for i in range(0,Nitem):
            eplist.append(ee/Nitem)
            if maxvalue <= vlist[i]:
                maxth = i
                maxvalue = vlist[i]
                
        eplist[maxth] = eplist[maxth] + 1 - ee
        
        return [item_list, eplist] 
        