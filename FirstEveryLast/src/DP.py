'''
Created on 2016. 5. 12.

@author: bklim
'''

class DP(object):
    '''
    classdocs
    '''


    def __init__(self, pro):
        '''
        Constructor
        '''
        self.Pro = pro
        
    def runDP(self, N):
        Vlist = [0]*len(self.Pro.States)
        Vlistbefore = [0]*len(self.Pro.States)
        
        for i in range(0,N):
            for j in range(0,len(Vlist)):
                Vlist[j] = self.Pro.Reward[j] + self.Pro.Lamda*self.listsum(self.listmulti(self.Pro.Trans[j], Vlistbefore))
            
            for j in range(0,len(Vlist)):
                Vlistbefore[j] = Vlist[j]
        return Vlist
                
    def listmulti(self, A, B):
        alist = []
        for i in range(0,len(A)):
            alist.append(A[i]*B[i])        
        return alist
    def listsum(self, A):
        sum = 0
        for a in A:
            sum+=a
        return sum