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
import matplotlib
import os.path
from os import listdir
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})

# rc('text', usetex=True)
#csfont = {'fontname':'Times New Roman'}
#plt.rcParams["font.family"] = "Times New Roman"
WDIR = os.path.dirname(__file__)
loadpath = os.path.join(WDIR,'data','stress_strain')
writepath = os.path.join(WDIR,'..','draft','img')
# pre-set head name



prop = ['step', 'strain', 'stress', 'energy']
# import data from .csv file:
#ds1 = pd.read_csv(os.path.join(loadpath,'aa.csv'), sep=' ', skiprows=1, names=prop)
ds2 = pd.read_csv(os.path.join(loadpath,'ag.csv'), sep=' ', skiprows=1, names=prop)
ds3 = pd.read_csv(os.path.join(loadpath,'pf.csv'), sep=' ', skiprows=1, names=prop)
ds4 = pd.read_csv(os.path.join(loadpath,'ia.csv'), sep=' ', skiprows=1, names=prop)
fct = 10e6*0.75
px2=ds2.step/fct
px3=ds3.step/fct
px4=ds4.step/fct

# plot lines
#p1 = plt.plot(ds1.step, ds1.stress, label='aa')
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8, 3)

p3 = plt.plot((ds3.strain-0.015)*1.2, ds3.stress, color = 'R')
p2 = plt.plot((ds2.strain-0.015)*1.2, ds2.stress, color = 'G')
p4 = plt.plot((ds4.strain-0.015)*1.2, ds4.stress, color = 'B')

plt.legend([ 'no void','void at boundary','void inside grain'], frameon=False)

# config title and label

#plt.title('stress-strain curve')
plt.xlabel('Strain')
plt.xlim(xmax=0.18)
plt.ylim(ymax=5.5)
plt.ylabel('Stress/GPa')
plt.savefig(os.path.join(writepath, 'alllineL.png'),dpi=300)
plt.show()
# /home/alex/violet/all.line.pdf
# /home/alex/violet/code/pict/area.png
# /home/alex/violet/draft/img/ag.pngf