import matplotlib.pyplot as plt
import numpy as np

# pre-set head name
pyy = np.loadtxt('ig_10.txt')
pxx = np.linspace(0, 0.4, (len(pyy)))

plt.plot(pxx, pyy)
plt.title('Area of Crack Surface')
plt.xlabel('strain')
plt.ylabel('Area/A2')
plt.savefig('area.png')
plt.show()




