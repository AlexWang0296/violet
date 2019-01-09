import os
import os.path
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})


#WDIR = os.getcwd()
WDIR = os.path.dirname(__file__)
loadpath = os.path.join(WDIR,'data','surf')
#writepath = os.path.join(WDIR,'draft','img')
writepath = os.path.join(WDIR,'..','draft','img')

#plt.savefig(os.path.join(WDIR,'draft','img','surf.pdf'))
#loadpath = os.path.join(WDIR,'code','data','surf')
ag =np.loadtxt(os.path.join(loadpath,'surf_ag.txt'))
ia =np.loadtxt(os.path.join(loadpath,'surf_ia.txt'))
ig =np.loadtxt(os.path.join(loadpath,'surf_ig.txt'))
pf =np.loadtxt(os.path.join(loadpath,'surf_pf.txt'))
#d_pf = np.gradient(pf)
imglist =[ag, ig, pf]
dv1st = list(map(np.gradient,imglist))
#colorlist = ['g','b','r']
# markerlist = ['s','^','o']
max = list(map(np.max,dv1st))
min = np.min(np.abs(ag))
for img in dv1st:
    pxx = np.linspace(0,np.dot(0.005,len(img)),len(img))/10
    plt.plot(pxx, img/np.max(max))
# plt.title('1st Deviation of Area of Surface of Crack')
plt.xlabel('Strain')
plt.ylabel('Relative Crack Propagation Indicator')
plt.xlim(xmax=0.03)
plt.legend(["ag","ig", "pf"],frameon=False)
# plt.legend()
plt.savefig(os.path.join(writepath,'1stdiv.pdf'))

plt.show()
plt.cla
plt.clf()

