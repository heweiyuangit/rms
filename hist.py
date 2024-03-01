import numpy as np
import matplotlib.pyplot as plt


analytical_solution = np.loadtxt('marine000.rsp',skiprows=560,usecols=4)  
initial_prediction = np.loadtxt('marine000.rsp',skiprows=560,usecols=6)  
final_prediction = np.loadtxt('marine106.rsp',skiprows=561,usecols=6)  

# 计算残差
initial_residual = analytical_solution / initial_prediction
final_residual = analytical_solution / final_prediction

# 计算归一化残差
initial_residual_normalized = initial_residual  / np.sqrt(np.mean(initial_residual ** 2))
final_residual_normalized = final_residual  /np.sqrt(np.mean(initial_residual ** 2))
# initial_residual_normalized = (initial_residual - np.mean(initial_residual)) / np.std(initial_residual)
# final_residual_normalized = (final_residual - np.mean(final_residual)) / np.std(final_residual)


# 绘制直方图
plt.figure(figsize=(10, 6))
plt.subplot(1,2,2)
# plt.hist(initial_residual, bins=100, alpha=0.5, label='Initial', color='black')
# plt.hist(final_residual, bins=50, alpha=0.5, label='Final iteration', color='lightgreen')
plt.yscale('log')
plt.hist(initial_residual, bins=50, alpha=0.5, label='Initial', color='black')
plt.hist(final_residual, bins=50, alpha=0.5, label='Final iteration', color='lightgreen')
plt.xlabel('Normalized residuals',fontsize=15)
plt.ylabel('Frequency of occurence',fontsize=15)
plt.text(-18, 5*1e4, '(b)', fontsize=16, ha='center', va='center', color='black')
plt.legend(fontsize=15)


rms_csem = np.loadtxt('marinecsem.txt',skiprows=1,usecols=(0,1))
rms_mt = np.loadtxt('marinemt.txt',skiprows=1,usecols=(0,1))
joint = np.loadtxt('marinejoint.txt',skiprows=1,usecols=(0,1))

x1 = [point[0] for point in rms_csem]
y1 = [point[1] for point in rms_csem]

x2 = [point[0] for point in rms_mt]
y2 = [point[1] for point in rms_mt]

x3= [point[0] for point in joint]
y3 = [point[1] for point in joint]

plt.subplot(1,2,1)
plt.xlim([0,120])
plt.plot(x1,y1,'-.',label='CSEM')
plt.plot(x2,y2,'-.',label='MT')
plt.plot(x3,y3,'-.',label='joint CSEM and MT')
plt.ylabel('Rms',fontsize=15)
plt.xlabel('Iteration',fontsize=15)
plt.text(6, 72, '(a)', fontsize=16, ha='center', va='center', color='black')
plt.legend(fontsize=15)


plt.subplots_adjust(wspace=0.3)
plt.show()
