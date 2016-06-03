'''
Created on 2016. 5. 12.

@author: bklim
'''
from src.Estimator import Estimator
from src.Problem import Problem
from src.Simulator import Simulator
from src.DP import DP

if __name__ == '__main__':
    
    ast = [0,1,2,3,4]
    atrans = [[0.5,0.5,0,0,0],[0.5,0,0.5,0,0],[0,0.5,0,0.5,0],[0,0,0.5,0,0.5],[0,0,0,0,1]]
    aLamda = 1
    aReward = [-1,-1,-1,-1,0]
    
    aPro = Problem(ast, atrans, aLamda, aReward)
    
    aDP = DP(aPro)
    print('DP result:')
    print(aDP.runDP(1000))
    print('---------------------------------------------')
    
    aSim = Simulator(aPro, 4)
    Historys = aSim.batchSimulate(0, 100)
    aEsti = Estimator(aPro, Historys)
    
    print('TD result a=N:')
    print(aEsti.TD(Historys))
    print('---------------------------------------------')
    
    alpha = 0.05
    print('TD result a='+str(alpha))
    print(aEsti.TDalpha(Historys,alpha))
    print(aEsti.TDalphaLast(Historys, alpha))
    print(aEsti.TDalphaNstep(Historys, 0, 200))
    
    print('---------------------------------------------')
    
    print('MC result:')
    print('Every:')
    print(aEsti.Every(Historys))
    print('Last:')
    print(aEsti.Last(Historys))
    print('Random:')
    print(aEsti.Random(Historys))
    for i in range(1, 15, 3):
        print('order='+str(i)+':')
        print(aEsti.Order(Historys, i))
    print('---------------------------------------------')
    
    pass