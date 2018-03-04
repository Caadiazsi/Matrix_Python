import random;
from time import time;


for s in range(1, 10):
  size = s* 50
  matrixA = [[0 for j in range(size)] for j in range(size)];
  matrixB = [[0 for j in range(size)] for j in range(size)];
  matrixAxB = [[0 for j in range(size)] for j in range(size)];
  Operations = size*size*((2*size)-1)
  print("Size: ", size)
  print("Operations: ", Operations)
  for j in range(size):
    for k in range(size):
      matrixA[j][k] = 1;
      matrixB[k][j] = 2;
      matrixAxB[j][k] = 0;
  initial_Time = time();
  for times in range (0, 10):
    for i in range(size):
      for j in range(size):
        count = 0;
        for k in range(size):
          count = count + (matrixA[i][k] * matrixB[k][j])
        matrixAxB[i][j] = count;
  execution_Time = time() - initial_Time;
  print ('Execution_Time: ', execution_Time/(Operations*10))
  print ('-------------------------------')