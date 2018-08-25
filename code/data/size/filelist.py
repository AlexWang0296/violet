import os
import os.path
from os import listdir
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.rcParams["font.family"] = 'Times New Roman'

dirlist = listdir(os.path.dirname(__file__))
print('Scaning dir: %s' %dirlist)
txtlist = []
itemlist = []
strmax = []
plt.rcParams["font.family"] = 'Times New Roman'
for i in dirlist:
    if os.path.splitext(i)[1] == ".txt":
        print('%s found' %i)
        txtlist.append(i)
        itemlist.append(os.path.splitext(i)[0])
count = 0
for node in txtlist:
    label = node.split('.')[0]
    prop = ['step', 'stress', 'strain']
    ds1 = pd.read_csv(node, sep=' ', skiprows=2, names=prop)
    strmax.append(np.max(ds1.stress))
    plt.plot(ds1.step, ds1.stress)
    plt.ylim(ymax=6)
    plt.xlim(xmax=4.5e5)
    #plt.title()
    plt.title([label,max(ds1.stress)])
    plt.savefig('fig.%s.pdf' % label)
    plt.clf()
    plt.cla
    print('%s over'%label)
    count +=count


