import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

elements=['TDS', 'CA', 'MG','NA','K','CL','HCO3','SO2','NO3']
measures=[
[100,0,0,0,0,0,0,0,0],
[400, 75, 50, 200, 10, 200, 300, 400, 45],
[1000,125,100,0,0,400,300,0,0],
[100,1400,1450,1400,1590,1000,1000,1200,1555],
]

x=np.arange(9)
plt.bar(x, measures[0], bottom=np.sum(measures[:0], axis=0), width=0.75, color='m', label='very_low')
plt.bar(x, measures[1], bottom=np.sum(measures[:1], axis=0), width=0.75, color='g', label='most_desirable')
plt.bar(x, measures[2], bottom=np.sum(measures[:2], axis=0), width=0.75, color='y', label='allowable')
plt.bar(x, measures[3], bottom=np.sum(measures[:3], axis=0), width=0.75, color='r',label='not-permisible')
plt.title("Drinking Water Analysis", fontsize=20)
plt.xticks(x,elements)
plt.legend(fontsize=10)
plt.xlabel('Elements')
plt.ylabel('quality')
plt.show()
