# 读取输出文件，绘制应力应变曲线
import os
import matplotlib.pyplot as plt
import pandas as pd
#csfont = {'fontname':'Times New Roman'}
WDIR = os.getcwd()
loadpath = os.path.join(WDIR,'code','data','stress_strain')
writepath = os.path.join(WDIR,'draft','img')
# pre-set head name
prop = ['step', 'strain', 'stress', 'energy']
# import data from .csv file:
ds1 = pd.read_csv(os.path.join(loadpath,'ia.csv'), sep=' ', skiprows=1, names=prop)

# plot lines
p1 = plt.plot(ds1.step, ds1.stress, label='ia')

# config title and label

plt.title('stress-strain curve')
plt.xlabel('Step')
plt.ylabel('Stress (GPa)')
plt.xlim(1e5,2e5)

#plt.lim(-6,6)
#plt.legend()
plt.savefig(os.path.join(writepath,'ialine.pdf'))
#plt.show()
#/home/alex/violet/all.line.pdf
#/home/alex/violet/code/pict/area.png
#/home/alex/violet/draft/img/ag.png