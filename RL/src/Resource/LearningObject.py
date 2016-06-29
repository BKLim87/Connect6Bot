'''
Created on 2016. 6. 8.

@author: bklim
'''
from utils.ProbUtils import ProbUtils
from Resource.NestedDictionary import NestedDictionary
from Resource.Policy import Policy
import pickle
import time

class LearningObject(object):
    '''
    classdocs
    '''


    def __init__(self, aStateChanger, aActionType, alamda, learningpolicy):
        '''
        Constructor
        '''
        self.StateChanger = aStateChanger
        self.ActionType = aActionType
        self.Lamda = alamda 
        
        self.Ndic = NestedDictionary()
        self.Qdic = NestedDictionary()
        
        self.LearningPolicy = learningpolicy
        
    def getName(self):
        return '('+self.StateChanger.getName()+','+self.ActionType.getName()+')'
    
    def getAction(self, state):
        return self.LearningPolicy.getAction(self.Qdic, state, self.ActionType)
        #return self.Policy.getAction(state, self.ActionType)
        
    def update(self, StateActionRewardList, side):
        self.LearningPolicy.update(self, StateActionRewardList, side)
            
    def print(self):
        print('State Type:'+self.StateChanger.getName())
        print('Action Type:'+self.ActionType.getName())
        print('Lamda:' + str(self.Lamda))
        print('N dic: ' + str(self.Ndic))
        print('Q dic: ' + str(self.Qdic))
        
        if self.StateChanger.getName() == 'Longest Line State Changer':
            astr = '{'
            for i in range(0,6):
                for j in range(0,6):
                    qlist = []
                    itemlist =[]
                    for aAction in self.ActionType.getActionList():
                        if self.Qdic.containNestedItem((i,j), aAction):
                            qlist.append(self.Qdic.getNestedItem((i,j), aAction))
                            itemlist.append(aAction)
                    if not qlist == []:        
                        maxflag = 0
                        for k in range(0,len(qlist)):
                            if qlist[maxflag] <qlist[k]:
                                maxflag = k
                        astr = astr + '('+str((i,j))+','+str(itemlist[maxflag])+')'
                    
            astr = astr + '}'
            print('Greedy Q:'+astr)
        
        
    def save_object(self):
        filedic = '../../LearningData/'
        filename = self.StateChanger.getName()+'-'+self.ActionType.getName()+'-'+str(self.Lamda)+'-'+str(time.time())+'.LO'
        f = open(filedic+filename, 'wb')
        pickle.dump(self, f)
        f.close()
        
    def load_object(self, filepath):
        f = open(filepath, 'rb')
        loadLO = pickle.load(f)
        
        self.StateChanger = loadLO.StateChanger
        self.ActionType = loadLO.ActionType
        self.Lamda = loadLO.Lamda         
        self.Policy = loadLO.Policy
        self.Ndic = loadLO.Ndic
        self.Qdic = loadLO.Qdic
         
        f.close()
                    
if __name__ == "__main__":
    print('start load saved data')
    
    aLL = LearningObject('','','')
    aLL.load_object('../../LearningData/test.LO')
    
    print('haha')
    
                
                  
                     
                
            
            
