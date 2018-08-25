
import os
import os.path
import numpy as np
import matplotlib.pyplot as plt


WDIR = os.path.dirname(__file__)
loadpath = os.path.join(WDIR,'data','surf')
writepath = os.path.join(WDIR,'..','draft','img')
#plt.savefig(os.path.join(WDIR,'draft','img','surf.pdf'))
#loadpath = os.path.join(WDIR,'code','data','surf')
ag = np.loadtxt(os.path.join(loadpath,'surf_ag.txt'))
ia = np.loadtxt(os.path.join(loadpath,'surf_ia.txt'))
ig = np.loadtxt(os.path.join(loadpath,'surf_ig.txt'))
pf = np.loadtxt(os.path.join(loadpath,'surf_pf.txt'))

imglist = [ag, ia, ig, pf]
for img in imglist:
    pxx = range(len(img))
    plt.plot(pxx, img)
plt.title('Growth of Crack')
plt.xlabel('strain')
plt.ylabel('area of crack surface')
plt.legend(["ag", "ia", "ig", "pf"],frameon=False)
plt.savefig(os.path.join(writepath,'surf.pdf'))
plt.show()


