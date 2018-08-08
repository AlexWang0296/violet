
import numpy as np

import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt.rc('font',family='Times New Roman')
#/home/alex/violet/code/data/crack_surf
ag = np.loadtxt('/home/alex/violet/code/data/crack_surf/ag_10.txt')
ia = np.loadtxt('/home/alex/violet/code/data/crack_surf/ia_10.txt')
ig = np.loadtxt('/home/alex/violet/code/data/crack_surf/ig_10.txt')
pf = np.loadtxt('/home/alex/violet/code/data/crack_surf/pf_10.txt')
imglist = [ag, ia, ig, pf]
for img in imglist:
    pxx = range(len(img))
    plt.plot(pxx, img)
plt.title('Growth of Crack')
plt.xlabel('strain')
plt.ylabel('area of crack surface')
plt.legend(["ag", "ia", "ig", "pf"],frameon=False)
plt.savefig('/home/alex/violet/draft/img/crack_surf.pdf')

plt.show()



