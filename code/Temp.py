import os
import os.path

#plt.rcParams["font.family"] = 'Times New Roman'
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12})
#csfont = {'fontname':'Times New Roman'}
#plt.rcParams["font.family"] = "Times New Roman"
WDIR = os.path.dirname(__file__)
# loadpath = os.path.join(WDIR,'data','stress_strain')
writepath = os.path.join(WDIR,'..','draft','img')
import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0,1200,1500)
key = 20*np.e**(-150/298)/20
key1=[298,298]
key2=[0,1]
u = 20*np.e**(-300/T)/20
v = 20*np.e**(-350/T)/20
w = 20*np.e**(-450/T)/20
plt.xlabel('Temperature / K')
plt.ylabel('Mobility of Dislocation')
plt.ylim(ymax=1)
plt.plot(key1,key2)
plt.plot(T,u,label='Case 1')
plt.plot(T,v,label='Case 2')
plt.plot(T,w,label='Case 3')
plt.legend(frameon=False)
plt.savefig(os.path.join(writepath, 'temp.pdf'))

plt.show()
