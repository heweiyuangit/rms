import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# 读取五张图片
img0 = mpimg.imread('C:/Users/wazi/Desktop/杂图/field_setup.png')
img1 = mpimg.imread('C:/Users/wazi/Desktop/杂图/page_1.png')

# 创建一个3x1的子图布局
plt.subplot(1, 2, 1)
plt.imshow(img0)
plt.text(125, 515, '(a)', fontsize=16, ha='center', va='center', color='black')
plt.axis('off')


plt.subplot(1,2, 2)
plt.imshow(img1)
plt.text(190, 880, '(b)', fontsize=16, ha='center', va='center', color='black')
plt.axis('off')

# 调整布局，以防止子图重叠
plt.subplots_adjust(wspace=0.05)

# 显示图形
plt.show()
