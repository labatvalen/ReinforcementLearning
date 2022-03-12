#Exercice 4 : 'Un premier Gridworld'

import numpy as np



#Liste des mouvements
tabStates = ['s1', 's2', 's3', 's4']
tabMoves = ['Left', 'Up', 'Right', 'Down']
tabStatesMoves = np.array([[0,0,1,2],[0,1,1,3],[2,0,3,2],[0,0,0,0]])
tabRewards = np.array([[-1,-1,0,0],[0,-1,-1,-0.5],[-1,0,0,-1],[1,1,1,1]])

nbEtats = len(tabStates)
nbActions = len(tabMoves)


#Cette partie du programme sert à afficher une description du système.
#On peut la "décommenter" si on le souhaite

'''for numetat in range(nbEtats):
  for numaction in range(nbActions):
    numetat2 = tabStatesMoves[numetat][numaction]
    print(tabStates[numetat], tabMoves[numaction], tabStates[numetat2], tabRewatds[numetat][numaction])
'''
#Lecture d'une valeur de gamma

gamma = float(input('Donnez la vaLEUR de gamma : '))

#Corps du programme value Iteration
#Critère d'arrêt : un nombre d'itérations mais ce critère 
#peut être par un critère du type max(écart entre valeurs successives de V) < epsilon

nbIter = 10

V = np.zeros(4)
for numiter in range(nbIter):
  for numetat in range(nbEtats):
    tabQ = []
    for numaction in range(nbActions):
      numetat2 = tabStatesMoves[numetat][numaction]
      q = tabRewards[numetat][numaction]+gamma*V[numetat2]
      tabQ.append(q)
    V[numetat]=max(tabQ)
  print(V)
	  


