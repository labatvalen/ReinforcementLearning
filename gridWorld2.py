#On suppose que nous avons un GridWorld de taille 3*3
#que l'objectif se trouve en L1, C3 et que le "contre-objectif" (case interdite)
#se trouve en L2,C2

import numpy as np

#On note 0, 1, 2 et 3 les directions Up, Right, Down, Left
def Move(pos, dir):
  new_x = pos[0]
  new_y = pos[1]
  if dir==0:
    new_x -=1
  elif dir==1:
    new_y +=1
  elif dir==2:
    new_x +=1
  elif dir==3:
    new_y -=1
  else:
    print('Direction invalide')  

  if (new_x<0):
    new_x = 0
  elif (new_x>2):
    new_x = 2
  elif (new_y<0):
    new_y = 0
  elif (new_y>2):
    new_y = 2
	
  return (new_x, new_y)
  
#La meilleure direction est (l'une de) celle(s) qui
#contien(nen)t la plus grande valeur de Q
#dans le voisinage de la position pos

def bestDirection(tabQ, pos):
  x = pos[0]
  y = pos[1]
  best = []
  mx   = max(tabQ[x][y][0], tabQ[x][y][1], tabQ[x][y][2], tabQ[x][y][3])
  for i in range(3):
    if (tabQ[x][y][i]==mx): 
      best.append(i)
	
  choice = np.random.randint(len(best))
  
  return best[choice], tabQ[x][y][best[choice]]
  
#Valeur du reward correspondant à une case

#Coeur de l'algorithme : mise-à-jour de la table Q
#Q(s,a) = Q(s,a) + alpha(r+maxQ(s',a')-Q(s,a)) 

def updateQ(tabQ, alpha, gamma, start, nbIter, tauxExplor, obj, cobj):
   for numiter in range(nbIter):
     pos = start
     while((pos!=obj)and(pos!=cobj)):
       rnd = np.random.rand()
       if (rnd<tauxExplor):
         dir = np.random.randint(3)
       else:
         dir = bestDirection(tabQ,pos)[0]
	   
       new_x, new_y = Move(pos, dir)

       r = tabReward[new_x][new_y]
       maxQ = max(tabQ[new_x][new_y][0], tabQ[new_x][new_y][1], tabQ[new_x][new_y][2], tabQ[new_x][new_y][3])
       tabQ[pos[0]][pos[1]][dir] =tabQ[pos[0]][pos[1]][dir]+alpha*(r+maxQ-tabQ[pos[0]][pos[1]][dir])
       pos = (new_x, new_y)
      
def afficherTabQ(tabQ):
   for x in range(3):
     for y in range(3):
       print(x,y,np.argmax((tabQ[x][y][0], tabQ[x][y][1], tabQ[x][y][2], tabQ[x][y][3])))


#Programme principal
#gridWorld = np.zeros(3,3,4)

tabQ = np.zeros([3,3,4])
tabReward = np.zeros([3,3])
tabReward[0][2]=1
tabReward[1][1]=-1

alpha = 0.2
gamma = 0.9
start = (2,0)
nbIter = 100
tauxExplor = 0.7
obj = (0,2)
cobj = (1,1)

updateQ(tabQ, alpha, gamma, start, nbIter, tauxExplor, obj, cobj)
afficherTabQ(tabQ)
