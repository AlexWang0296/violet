# 读取输出文件，绘制应力应变曲线
import os
import matplotlib.pyplot as plt
import pandas as pd

# pre-set head name
prop = ['step', 'strain', 'stress', 'energy']
# import data from .csv file:
ds1 = pd.read_csv('~/violet/code/data/stress_strain/aa.csv', sep=' ', skiprows=1, names=prop)
ds2 = pd.read_csv('~/violet/code/data/stress_strain/ag.csv', sep=' ', skiprows=1, names=prop)
ds3 = pd.read_csv('~/violet/code/data/stress_strain/pf.csv', sep=' ', skiprows=1, names=prop)
ds4 = pd.read_csv('~/violet/code/data/stress_strain/ia.csv', sep=' ', skiprows=1, names=prop)
# plot lines
p1 = plt.plot(ds1.step, ds1.stress, label='aa')
p2 = plt.plot(ds2.step, ds2.stress, label='ag')
p3 = plt.plot(ds3.step, ds3.stress, label='pf')
p4 = plt.plot(ds4.step, ds4.stress, label='ia')
# config title and label

plt.title('stress-strain curve')
plt.xlabel('Step')
plt.ylabel('Stress (GPa)')
plt.legend()
plt.show()

