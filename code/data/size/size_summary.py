import os
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = 'Times New Roman'
size = [0, 2, 5, 10, 15, 20]
iamax = [5.2, 5.16, 5.27, 5.22, 5.19, 4.96]
agmax = [5.2, 5.19, 5.10, 5.11, 5.09, 4.87]

plt.plot(size, iamax, linestyle='--', marker='s', color='r')
plt.plot(size, agmax, linestyle='--', marker='^', color='b')

plt.legend(['ia', 'ag'], frameon=False)
# plt.ylim(ymin=0)
plt.xlabel('Radius of Void/A')
plt.ylabel('Strength/GPa')
plt.savefig('effect_of_vol.pdf')
plt.show()

# comments

'''
UserWarning: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans
  (prop.get_family(), self.defaultFamily[fontext]))
'''
