import sys
import numpy as np
import matplotlib.pyplot as plt
v = np.array([3.36, 3.69, 4.33, 5.02, 6.39, 8.03, 10.16, 12.6, 15.36, 18.15, 21.23, 23.91, 25.38, 26.27, 26.13, 25.56, 25.71])
u = np.linspace(0, len(v)-1, len(v))
plt.plot(u,v)
plt.show()


plt.rcParams['figure.figsize'] = (5,2.5)
plt.xlabel('Position')
plt.ylabel('Temperatrue')
plt.rcParams.update({'font.size': 9})
plt.tight_layout()

# line color
# set1: red,green,blue
# set2: frebrick,forestgreen,darkgreen
plt.plot(u,v,color='firebrick',marker='o',markevery=1,mew=0.25)
# plt.plot(b,v,color='forestgreen',marker='o',markevery=10,mew=0.25)
# plt.plot(c,w,color='darkblue',marker='s',markevery=10,mew=0.25)
# create legend without frame
# plt.legend(['L1','L2','L3'],frameon=False)
# plt.xlim(0,8)
# plt.ylim(-3,3)
# plt.savefig('plt.svg')
# plt.savefig('plt.pdf',dpi=300)
plt.savefig('crackdis.pdf')

plt.show()
sys.exit(0)