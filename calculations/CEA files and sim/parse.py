import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import sys


def annot_max(x,y, ax=None):
    xmax = x[np.argmax(y)]
    ymax = y.max()
    text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)



file_name = input("Please input the file name:\n")
fuel_name = input("Please input the name of the fuel:\n")
file = open(os.path.join(sys.path[0],file_name)).read()
outputs = file.split('THEORETICAL')
outputs = outputs[1:]
df = pd.DataFrame()
Of_ratio = []
Imp = []
Kelvin = []
for output in outputs:
    dic = {}
    Pin = output.split('Pin =')[1].split('PSIA')[0].strip()
    O_F = output.split('O/F=')[1].split('%FUEL')[0].strip()
    Temp = output.split('T, K')[1].split('RHO')[0].strip().split()[0]
    #print(Temp)
    Isp = output.split('Isp, M/SEC')[1].split('MOLE')[0].strip().split()[1]
    #dic['Pin'] = float(Pin)
    #dic['O_F'] = float(O_F)
    #dic['Isp'] = float(Isp)/9.
    Of_ratio.append(float(O_F))
    Imp.append(float(Isp)/9.81)
    Kelvin.append(float(Temp))

    #dic['Temp'] = float(Temp)
    
    df1 = pd.DataFrame(dic, index=[0])
    df = pd.concat([df, df1], ignore_index=True)


#Pins = list(df['Pin'].unique())
#colors = ['o-r','o-b','o-g','o-c','o-m','o-y','o-k','o-r','o-b','o-g','o-c','o-m','o-y','o-k']
#cnt = 0

#for Pin in Pins:
    #color = colors[cnt]
    #val = df[df['Pin']==Pin]
    #plt.plot(val['O_F'],val['Isp'],color)
    #plt.plot(val['O_F'],val['Temp'],color)
    #cnt += 1

#plt.legend([str(Pin)+'(psia)' for Pin in Pins])
#plt.xlabel('O/F ratio')
#plt.ylabel('Isp')
#plt.show()

fig, axs = plt.subplots(2)
fig.suptitle(f'{fuel_name} plus gas oxygen')
axs[0].plot(Of_ratio,Kelvin)
axs[0].set(ylabel='Temp(K)')
axs[0].set_title('Temperature against oxodizer-fuel ratio')
axs[1].plot(Of_ratio,Imp)
axs[1].set(ylabel='Isp(s)')
axs[1].set_title('Temperature against oxodizer-fuel ratio')

annot_max(np.array(Of_ratio),np.array(Kelvin))

plt.show()