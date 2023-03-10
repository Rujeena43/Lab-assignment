# -*- coding: utf-8 -*-
"""KNN Algorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pkDbNeHQEJoB8cGEJaoWNFHr8KjWi9kK

1) Implement k-NN algorithm on Python.
 a) Install Anaconda3-2022.10
 b) Generate points in 2-dimensional space randomly using random number
 generator function of python. Consider that no point extends beyond 50 on     both  x and y axis i.e. If P1 = (x1, y1) then |x1| ≤ 50 and |y1| ≤ 50. Number of points to be generated must be at least 200 and at most 500.
 c) Taking different cases for k = 3, 5, and 7, run k-NN algorithm on the generated
points.
 d) Now generate 10 new points and categorize these points to the suitable nearest
neighbor.
 e) Extend the code to consider points of N-dimensional space
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

list1=[]
list2=[]
for i in range(0,350):
  x=random.randint(-50,50)
  y=random.randint(-50,50)
  list1.append(x)
  list2.append(y)
  print(x,y)

plt.scatter(list1,list2)
plt.show()

output=[]
for i, j in zip(list1,list2):
  if ((i+j)/2)>0:
    output.append(0)
  else:
    output.append(1)

print(list1)
print(list2)
print(output)

print(list1)
print(list2)
print(len(output)) 



fig = plt.figure()
er = fig.add_subplot(111)

er.scatter(list1, list2, c=output)

from sklearn.model_selection import train_test_split


list1_train, list1_test, list2_train, list2_test,output_train, output_test = train_test_split(list1, list2,output, test_size = 0.2)
# output_train, z_test=train_test_split(z,test_size=0.2)

print(list1_train)
print(list1_test)
print(list2_train)
print(list2_test)
print(output_train)
print(output_test)

print(list1_train)
print(list1_test)
print(list2_train)
print(list2_test)
print(len(output_train))
print(len(output_test))

distance=[]
output_pred=[]
def KNN(list1_1,list2_1,list1_2,list2_2,k):
  a1=len(list1_2)
  for i in range(0,a1):
    output_pred_temp=[]
    distance=[]
    b1=len(list1_1)
    for j in range(0,b1):
           
      r=((list1_2[i]-list1_1[j])**2+(list2_2[i]-list2_1[j])**2)**0.5
      distance.append(r)
    
    rank = [sorted(distance).index(list1_list1) for list1_list1 in distance]
    

    for n in range(0,k):
      c= rank.count(n)
      

      if c==1 and c>0:
        d=rank.index(n)

        output_pred_temp.append(output_train[d])
        
      elif c>0:
       
        for z in rank:
          if n==z:
            d=rank.index(z)
            output_pred_temp.append(output_train[d])



    
    output_pred_temp = output_pred_temp[:k]
    
    if output_pred_temp.count(0)>=output_pred_temp.count(1):
      output_pred.append(0)
    
    else:
      output_pred.append(1)
    
   
    
  

  Accr = (sum(1 for x_i,y_i in zip(output_pred,output_test) if x_i == y_i) / float(len(output_test)))*100
  print("Predicted value of output is:",output_pred)
  print("Actual value of output is:",output_test)
  
  print("Percentage of correctly classification is %: ", Accr)

      

  

KNN(list1_train,list2_train,list1_test,list2_test,3)
KNN(list1_train,list2_train,list1_test,list2_test,5)
KNN(list1_train,list2_train,list1_test,list2_test,7)