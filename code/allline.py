# 读取输出文件，绘制应力应变曲线
'''
violet
├── code
│   ├── data
│   │   ├── size
│   │   ├── stress_strain
│   │   └── surf
│   └── pict
└── draft
    ├── bkp
    ├── img
    ├── material
    └── ref
'''
import os
import os.path
from os import listdir
import matplotlib.pyplot as plt
import pandas as pd
#csfont = {'fontname':'Times New Roman'}
#plt.rcParams["font.family"] = "Times New Roman"
WDIR = os.path.dirname(__file__)
loadpath = os.path.join(WDIR,'data','stress_strain')
writepath = os.path.join(WDIR,'..','draft','img')
# pre-set head name
prop = ['step', 'strain', 'stress', 'energy']
# import data from .csv file:
ds1 = pd.read_csv(os.path.join(loadpath,'aa.csv'), sep=' ', skiprows=1, names=prop)
ds2 = pd.read_csv(os.path.join(loadpath,'ag.csv'), sep=' ', skiprows=1, names=prop)
ds3 = pd.read_csv(os.path.join(loadpath,'pf.csv'), sep=' ', skiprows=1, names=prop)
ds4 = pd.read_csv(os.path.join(loadpath,'ia.csv'), sep=' ', skiprows=1, names=prop)
# plot lines
p1 = plt.plot(ds1.step, ds1.stress, label='aa')
p2 = plt.plot(ds2.step, ds2.stress, label='ag')
p3 = plt.plot(ds3.step, ds3.stress, label='pf')
p4 = plt.plot(ds4.step, ds4.stress, label='ia')
# config title and label

plt.title('stress-strain curve')
plt.xlabel('Step')
plt.xlim(xmax=3e5)
plt.ylabel('Stress (GPa)')
plt.legend(frameon=False)
plt.savefig(os.path.join(writepath, 'allline.pdf'))

# plt.show()
# /home/alex/violet/all.line.pdf
# /home/alex/violet/code/pict/area.png
# /home/alex/violet/draft/img/ag.png