import numpy as np 
import matplotlib.pyplot as plt

rms_csem = np.loadtxt('marinecsem.txt',skiprows=1,usecols=(0,1))
rms_mt = np.loadtxt('marinemt.txt',skiprows=1,usecols=(0,1))
joint = np.loadtxt('marinejoint.txt',skiprows=1,usecols=(0,1))

x1 = [point[0] for point in rms_csem]
y1 = [point[1] for point in rms_csem]

x2 = [point[0] for point in rms_mt]
y2 = [point[1] for point in rms_mt]

x3= [point[0] for point in joint]
y3 = [point[1] for point in joint]
plt.figure(figsize=(7, 6))
plt.xlim([0,120])
plt.plot(x1,y1,'-.',label='CSEM')
plt.plot(x2,y2,'-.',label='MT')
plt.plot(x3,y3,'-.',label='joint CSEM and MT')
plt.ylabel('Rms',fontsize=15)
plt.xlabel('Iteration',fontsize=15)
plt.legend(fontsize=15)
plt.show()