import os
import matplotlib.pyplot as plt
import pandas as pd

def mplt(pos):
    plt.title('stress-strain curve')
    plt.xlabel('Step')
    plt.ylabel('Stress (GPa)')
    plt.xlim(xmax=2.5e5)
    plt.plot(pos.step, pos.stress, label='%s' %pos)
    plt.savefig('/home/alex/violet/draft/img/%sline.pdf' %pos)
    #plt.cla()
    #plt.show()

# pre-set head name
prop = ['step', 'strain', 'stress', 'energy']
# import data from .csv file:
d_aa = pd.read_csv('~/violet/code/data/stress_strain/aa.csv', sep=' ', skiprows=1, names=prop)
d_ag = pd.read_csv('~/violet/code/data/stress_strain/ag.csv', sep=' ', skiprows=1, names=prop)
d_pf = pd.read_csv('~/violet/code/data/stress_strain/pf.csv', sep=' ', skiprows=1, names=prop)
d_ia = pd.read_csv('~/violet/code/data/stress_strain/ia.csv', sep=' ', skiprows=1, names=prop)

pos = [d_aa, d_ag, d_pf, d_ia]


map(mplt(pos),pos)
    #plt.savefig('/home/alex/HDD/str-pict/frame%s.png' % frame)
    