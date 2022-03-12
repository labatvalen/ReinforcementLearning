#TD App. renforcement Exo3
import numpy as np
etats = ['Cours1', 'Cours2', 'Cours3', 'Pause', 'Sortir', 'Facebook', 'Dormir']
reward = np.array([-2, -2, -2, 10, 1, -1, 0])
P = np.zeros([7,7])
P[0][1]=0.5
P[0][5]=0.5
P[1][2]=0.8
P[1][6]=0.2
P[2][3]=0.4
P[2][4]=0.6
P[3][0]=0.2
P[3][1]=0.4
P[3][2]=0.4
P[4][6]=1.0
P[5][0]=0.1
P[5][5]=0.9
P[6][6]=1.0
I = np.identity(7)
#Programme principal
gamma = float(input('Donnez la valeur de gamma : '))
V =  np.dot(np.linalg.inv(I-gamma*P),reward)

for i in range(7):
  print(etats[i],':',round(V[i],2))


