import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
strmax = np.zeros(17)
u = np.linspace(20, 35, 16)
k = 1
for i in u:

    nami = str(int(i))
    ds = pd.read_csv('%s'%nami, sep=' ',skiprows=1)
    maxst = np.array(ds.values)
    np.nan_to_num(maxst,0)
    np.max(maxst)
    print(nami)
    print(np.max(maxst))
    strmax[k] = np.max(maxst)
    k=k+1

v = np.array(
        [3.36, 3.69, 4.33, 5.02, 6.39, 8.03, 10.16, 12.6, 15.36, 18.15, 21.23, 23.91, 25.38, 26.27, 26.13, 25.56,
         25.71])
plt.plot(v,strmax,marker='o')
np.savetxt('crack-str.txt',[v,strmax])
plt.show()