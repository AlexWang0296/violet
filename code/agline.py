# 读取输出文件，绘制应力应变曲线
import os
import os.path
import matplotlib.pyplot as plt
import pandas as pd

WDIR = os.getcwd()
loadpath = os.path.join(WDIR,'code','data','stress_strain')
writepath = os.path.join(WDIR,'draft','img')



# pre-set head name
prop = ['step', 'strain', 'stress', 'energy']
# import data from .csv file:
ds1 = pd.read_csv(os.path.join(loadpath,'ag.csv'), sep=' ', skiprows=1, names=prop)

# plot lines
p1 = plt.plot(ds1.step, ds1.stress, label='ag')

# config title and label

plt.title('stress-strain curve')
plt.xlabel('Step')
plt.ylabel('Stress (GPa)')
plt.xlim(1e5,2e5)


plt.savefig(os.path.join(writepath,'agline.pdf'))
plt.show()
