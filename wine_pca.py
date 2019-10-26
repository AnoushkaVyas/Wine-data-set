import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
data=[]
data = [i.strip().split(',') for i in open("wine.data").readlines()]
arr=np.array(data,float)
cov=np.cov(arr[:,1:14], rowvar=False)
eigv, ev= LA.eig(cov)
eigv_sort=np.sort(eigv)
index=np.argsort(eigv)
ev_sort=ev.transpose()[index].transpose()
print(eigv_sort)
plt.scatter(range(1,len(eigv_sort)+1),eigv_sort)
plt.ylabel('Eigen Values')
plt.show()
classx1=[]
classx2=[]
classx3=[]
classy1=[]
classy2=[]
classy3=[]
for i in range(0,178):
    if arr[i:i+1,0]==1:
        classx1.append(np.matmul(arr[i,1:14], ev_sort[:,12]))
        classy1.append(np.matmul(arr[i,1:14], ev_sort[:,11]))
    if arr[i:i+1,0]==2:
        classx2.append(np.matmul(arr[i,1:14], ev_sort[:,12]))
        classy2.append(np.matmul(arr[i,1:14], ev_sort[:,11]))
    if arr[i:i+1,0]==3:
        classx3.append(np.matmul(arr[i,1:14], ev_sort[:,12]))
        classy3.append(np.matmul(arr[i,1:14], ev_sort[:,11]))
plt.scatter(np.array(classx1),np.array(classy1),c='r',label='Class 1')
plt.scatter(np.array(classx2),np.array(classy2),c='g', label='Class 2')
plt.scatter(np.array(classx3),np.array(classy3),c='b', label='Class 3')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend()
plt.show()