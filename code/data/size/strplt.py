# plot step-stress line

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#txtpath=['stagsz2','stagsz5','stagsz15','stagsz20'\
           'stiasz2','stiasz5', 'stiasz15','stiasz20']

prop = ['step', 'stress', 'strain']
ds1 = pd.read_csv(txtpath, sep=' ', skiprows=2, names=prop)
p1 = plt.scatter(ds1.step, ds1.stress)
# maxstep = np.max(ds1.step)
# maxstre = np.max(ds1.stress)
# print('max step is %d\nmax stress is %f\n' %(maxstep, maxstre))
# plt.xlabel('Step')
# plt.ylabel('Stress (GPa)')
# plt.legend()
# plt.show()


