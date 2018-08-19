import os
from os import listdir
import matplotlib.pyplot as plt
import pandas as pd

dirlist = listdir(os.getcwd())
txtlist = []

for i in dirlist:
    if os.path.splitext(i)[1] == ".txt":
        txtlist.append(i)
print(txtlist)

for node in txtlist:
    prop = ['step', 'stress', 'strain']
    ds1 = pd.read_csv(node, sep=' ', skiprows=2, names=prop)
    plt.scatter(ds1.step, ds1.stress)
    plt.ylim(ymax=6)
    plt.xlim(xmax=4.5e5)
    plt.title(node)
    plt.show()
