
import os
import os.path

#plt.rcParams["font.family"] = 'Times New Roman'
import matplotlib.pyplot as plt

#csfont = {'fontname':'Times New Roman'}
plt.rcParams["font.family"] = 'Times New Roman'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
plt.rcParams.update({'font.size': 16})
WDIR = os.path.dirname(__file__)
# loadpath = os.path.join(WDIR,'data','stress_strain')
writepath = os.path.join(WDIR,'..','draft','img')
pf = [744, 290, 212, 530]
shockley = [1343, 1470, 3581, 4367]
stair_rode = [0, 123, 259, 295]
hirth = [0, 407, 1100, 557]
frank = [0, 375, 211, 500]


# data to plot
n_groups = 4

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.22
opacity = 0.8

rects1 = plt.bar(index, pf, bar_width,
                 alpha=opacity,
                 color='R',
                 label='Perfect')

rects2 = plt.bar(index + bar_width, shockley, bar_width,
                 alpha=opacity,
                 color='B',
                 label='Shockley')

rects3 = plt.bar(index + 2*bar_width, stair_rode, bar_width,
                 alpha=opacity,
                 color='G',
                 label='Stair-rod')

rects4 = plt.bar(index + 3*bar_width, frank, bar_width,
                 alpha=opacity,
                 color='black',
                 label='Frank')

plt.xlabel('Strain')
plt.ylabel(r'Dislocation length / \AA')
plt.ylim(ymax=5000)
# plt.title('Scores by person')
plt.xticks(index + bar_width, ('0.005','0.092','0.101','0.112'))
plt.legend(frameon = False,title='Type of dislocation')

plt.savefig(os.path.join(writepath, 'dis-summary.pdf'))

#plt.tight_layout()
plt.show()
