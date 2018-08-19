
import os
import os.path
import numpy as np
import matplotlib.pyplot as plt


WDIR = os.getcwd()
loadpath = os.path.join(WDIR,'code','data','surf')
writepath = os.path.join(WDIR,'draft','img')

#plt.savefig(os.path.join(WDIR,'draft','img','surf.pdf'))
#loadpath = os.path.join(WDIR,'code','data','surf')
ag =np.loadtxt(os.path.join(loadpath,'surf_ag.txt'))
ia =np.loadtxt(os.path.join(loadpath,'surf_ia.txt'))
ig =np.loadtxt(os.path.join(loadpath,'surf_ig.txt'))
pf =np.loadtxt(os.path.join(loadpath,'surf_pf.txt'))
#d_pf = np.gradient(pf)
imglist = ([ag, ia,  ig, pf])
dv1st = list(map(np.gradient,imglist))
for img in dv1st:
    pxx = range(len(img))
    plt.plot(pxx, img)
plt.title('1st Deviation of Area of Surface of Crack')
plt.xlabel('strain')
plt.ylabel('area of crack surface')
plt.xlim(xmax=50)
plt.legend(["ag", "ia", "ig", "pf"],frameon=False)
plt.savefig(os.path.join(writepath,'1stdiv.pdf'))

plt.show()
plt.cla
plt.clf()


