# 读取输出文件，绘制应力应变曲线
import os
import os.path
import matplotlib.pyplot as plt
import pandas as pd
from os import listdir
plt.rcParams.update({'font.size': 12})

WDIR = os.path.dirname(__file__)
loadpath = os.path.join(WDIR,'data')
writepath = os.path.join(WDIR,'..','draft','img')
# pre-set head name
prop = ['step', 'strain', 'stress', 'energy']
# import data from .csv file:
ds1 = pd.read_csv(os.path.join(loadpath,'pfct.txt'), sep=' ', skiprows=1, names=prop)
plt.figure(figsize=(8.5,2.5))
# plot lines
p1 = plt.plot(ds1.strain, ds1.stress, label='ag')
vlinex = [130000, 130000]
vliney = [4, 6]
# p2 = plt.plot(vlinex,vliney)
# config title and label

#plt.title('stress-strain curve')
plt.xlabel('Strain')
plt.ylabel('Stress (GPa)')
#plt.xlim(0,2e5)


plt.savefig(os.path.join(writepath,'perfect-line.pdf'))
plt.show()
