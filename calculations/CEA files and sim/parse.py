import matplotlib.pyplot as plt
import pandas as pd
import os
import sys



#file_name = input("Please input the file name:")
file = open(os.path.join(sys.path[0],"output.txt")).read()
outputs = file.split('THEORETICAL')
outputs = outputs[1:]
df = pd.DataFrame()
for output in outputs:
    dic = {}
    Pin = output.split('Pin =')[1].split('PSIA')[0].strip()
    O_F = output.split('O/F=')[1].split('%FUEL')[0].strip()
    Isp = output.split('Isp, M/SEC')[1].split('MOLE')[0].strip().split()[0]
    dic['Pin'] = float(Pin)
    dic['O_F'] = float(O_F)
    print(Isp.split())
    dic['Isp'] = float(Isp)
    
    df1 = pd.DataFrame(dic, index=[0])
    df = pd.concat([df, df1], ignore_index=True)


Pins = list(df['Pin'].unique())
colors = ['o-r','o-b','o-g','o-c','o-m','o-y','o-k','o-r','o-b','o-g','o-c','o-m','o-y','o-k']
cnt = 0

for Pin in Pins:
    color = colors[cnt]
    val = df[df['Pin']==Pin]
    plt.plot(val['O_F'],val['Isp'],color)
    cnt += 1

plt.legend([str(Pin)+'(psia)' for Pin in Pins])
plt.xlabel('O/F ratio')
plt.ylabel('Isp')
plt.show()
