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
from matplotlib import rc
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 14})
plt.rcParams["font.family"] = 'Times New Roman'

rc('text', usetex=True)

# rc('text', usetex=True)
#csfont = {'fontname':'Times New Roman'}
#plt.rcParams["font.family"] = "Times New Roman"
WDIR = os.path.dirname(__file__)
loadpath = os.path.join(WDIR,'data')
writepath = os.path.join(WDIR,'..','draft','img')
# pre-set head name



prop = ['step', 'strain', 'stress', 'energy']
# import data from .csv file:
#ds1 = pd.read_csv(os.path.join(loadpath,'aa.csv'), sep=' ', skiprows=1, names=prop)
ds1 = pd.read_csv(os.path.join(loadpath,'bin-g'), sep=' ', skiprows=1,names=['position','strgrad'])
ds2 = pd.read_csv(os.path.join(loadpath,'bin-a'), sep=' ', skiprows=1,names=['position','strgrad'])

# plot lines
p1 = plt.scatter(ds1.position, ds1.strgrad, color = 'B')
p2 = plt.scatter(ds2.position, ds2.strgrad, color = 'G')

#p3 = plt.plot((ds.strain-0.015)*1.2, ds3.stress, color = 'R')
#p2 = plt.plot((ds2.strain-0.015)*1.2, ds2.stress, color = 'G')
#p4 = plt.plot((ds4.strain-0.015)*1.2, ds4.stress, color = 'B')

# plt.legend('stress gradient', frameon=False)

# config title and label

#plt.title('stress-strain curve')
plt.xlabel('Position')
plt.ylabel('Strain gradient')
#plt.ylim(ymin=0)
plt.legend([r'$\alpha_2$ phase', r'$\gamma$ phase',r'$v_3 (\tau_3^*)$'], frameon=False,loc='best')

#plt.ylim(ymax=5.5)
#plt.ylabel('Stress/GPa')
plt.savefig(os.path.join(writepath, 'strgrad-bkp.pdf'))
plt.show()
# /home/alex/violet/all.line.pdf
# /home/alex/violet/code/pict/area.png
# /home/alex/violet/draft/img/ag.pngf