import os
import os.path

#plt.rcParams["font.family"] = 'Times New Roman'
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 16})
from matplotlib import rc
rc('text', usetex=True)
#csfont = {'fontname':'Times New Roman'}
plt.rcParams["font.family"] = "Times New Roman"
WDIR = os.path.dirname(__file__)
# loadpath = os.path.join(WDIR,'data','stress_strain')
writepath = os.path.join(WDIR,'..','draft','img')
import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0,1100,100)
key = 20*np.e**(-150/298)/20
key1=[298,298]
key2=[0,1]
# u = 20*np.e**(-300/T)/20
# v = 20*np.e**(-350/T)/20
# w = 20*np.e**(-450/T)/20
u = 20*np.e**(-350/T)/20
v = 20*np.e**(-400/T)/20
w = 20*np.e**(-450/T)/20
plt.xlabel('Temperature / K')
plt.ylabel('Normalized velocity of dislocation motion')
plt.ylim(ymax=1)
plt.plot(T,u, color='R')
plt.plot(T,v, color='G')
plt.plot(T,w, color='B')
plt.legend([r'$v_1 (\tau_1^*)$', r'$v_2 (\tau_2^*)$',r'$v_3 (\tau_3^*)$'], frameon=False,loc='best')
plt.text(450,0.85,r'$\tau_1^*>\tau_2^*>\tau_3^*$')
plt.annotate('298 K',xy=(290,0.35),xytext=(80,0.45),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
plt.plot(key1,key2,linestyle='--',color='black')

plt.savefig(os.path.join(writepath, 'temp.pdf'))

plt.show()

