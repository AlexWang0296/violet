import numpy as np
import matplotlib.pyplot as plt
WDIR = os.path.dirname(__file__)
# loadpath = os.path.join(WDIR,'data','stress_strain')
writepath = os.path.join(WDIR,'..','draft','img')
T = np.linspace(0,1000,1500)
key = 20*np.e**(-150/298)/20
key1=[298,298]
key2=[0,key]
u = 20*np.e**(-150/T)/20
v = 20*np.e**(-250/T)/20
w = 20*np.e**(-100/T)/20
plt.xlabel('Temperature/K')
plt.ylabel('Normalized Velocity of Dislocation')
plt.plot(key1,key2)
plt.plot(T,u,label='T1')
plt.plot(T,v,label='T2')
plt.plot(T,w,label='T3')
plt.show()