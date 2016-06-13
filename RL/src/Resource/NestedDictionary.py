'''
Created on 2016. 6. 13.

@author: bklim
'''

import collections


class NestedDictionary(collections.MutableMapping):
    '''
    for Q and N dictionary
    '''

    def __init__(self, *args, **kwargs):
        self.store = dict()
        self.update(dict(*args, **kwargs))  # use the free update to set keys

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)
    
    def getNestedItem(self, firstkey, secondkey):
        return self.__getitem__(firstkey).__getitem__(secondkey)
            
    
    def setNestedItem(self, firstkey, secondkey, value):
        if self.__contains__(firstkey):
            self.__getitem__(firstkey).__setitem__(secondkey, value)
        else:
            self.__setitem__(firstkey, dict())
            self.__getitem__(firstkey).__setitem__(secondkey, value)
            
    def containNestedItem(self, firstkey, secondkey):
        if self.__contains__(firstkey):
            return self.__getitem__(firstkey).__contains__(secondkey)
        else:
            return False
        
    def __str__(self):
        astr = '{'
        for akey in self.keys():
            for bkey in self.get(akey):
                astr = astr +'('+str(akey)+','+str(bkey)+')='+str(self.getNestedItem(akey, bkey))+', '
        return astr