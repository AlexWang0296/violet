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
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as fit
plt.rcParams.update({'font.size': 14})
from matplotlib import rc
rc('text', usetex=True)
plt.rcParams["font.family"] = 'Times New Roman'

WDIR = os.path.dirname(__file__)
writepath = os.path.join(WDIR,'..','..','..','draft','img')

size = np.array([0, 2, 5, 10, 15, 20])
iamax = np.array([5.3, 5.26, 5.25, 5.22, 5.19, 4.96])
agmax = np.array([5.3, 5.25, 5.17, 5.11, 5.09, 4.87])
fac = (1-(np.pi*(size/2)**2)/(210*180))*iamax[0]
# pia = fit.gaussian(size,iamax)
plt.plot(size, fac, marker='o',linestyle='--',color='R')
plt.plot(size, iamax,marker='s',color='G')
plt.plot(size, agmax, marker='^',color='B')

# color='darkorange'
# color='steelblue'
plt.legend(['calculated value',r'void inside $\alpha$ phase', r'void at \textbf{$\alpha$-$\gamma$} phase boundary'], frameon=False)
plt.ylim(4.8,5.5)
plt.xlabel(r'Radius of Void/ \AA')
plt.ylabel('Strength/GPa')
plt.savefig(os.path.join(writepath,'effect_of_vol.pdf'))
plt.show()

# import matplotlib as plt
# print(plt.get_cachedir())
# comments

'''
UserWarning: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans
  (prop.get_family(), self.defaultFamily[fontext]))
'''
