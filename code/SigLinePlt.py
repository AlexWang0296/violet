import os
import numpy as np
import matplotlib.pyplot as plt
file_path = os.path.join('data', 'inflammation-01.csv')
# pre-set head name
wdir = os.path.abspath('.')
pyy = np.loadtxt("wdir/code/data/crack_surf/ig_10.txt")
pxx = np.linspace(0, 0.4, (len(pyy)))

plt.plot(pxx, pyy)
plt.title('Area of Crack Surface')
plt.xlabel('strain')
plt.ylabel('Area/A2')
plt.savefig('area.png')
plt.show()
#plt.savefig()



