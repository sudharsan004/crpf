import matplotlib.pyplot as plt 
import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb = mysql.connect(
  host="localhost",
  user='root',
  passwd="{sudha}",
  database='water'
)

mycursor=mydb.cursor()
#df = pd.DataFrame(columns=['WATER_SAMPLE', 'TDS', 'PH', 'CALCIUM', 'MAGNESIUM','SODIUM','POTASSIUM','NITRATE','CHLORIDE','SULPHATE','FLUORIDE'])
df=pd.DataFrame(columns=['ELEMENT','QUALITY'])
elements=['TDS', 'CA', 'MG','NA','K','CL','HCO3','SO2','NO3']
leg=['VERY-LOW','MOST-DESIRABLE','ALLOWABLE','NOT-PERMISIBLE']
C=['rose','green','yellow','red']
count=0
quality=[500,300,200,180,20,50,660,0,50]
elements=['TDS', 'CA', 'MG','NA','K','CL','HCO3','SO2','NO3']
#measure- qualities
#very_low=[100,0,0,0,0,0,0,0,0]
#most_desirable=[500,75,50,200,10,200,0,400,45]
#allowable=[1500,200,150,0,0,600,0,0,0]
#not_permisible=[1500,200,150,200,10,600,0,400,45]
#most_desirable=[400, 75, 50, 200, 10, 200, 0, 400, 45]
#allowable=[1000,125,100,0,0,400,0,0,0]
#not_permisible=[0,0,0,0,0,0,0,0,0]
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
plt.legend(fontsize=10,loc=(1.0,0.2))
plt.xlabel('Elements')
plt.ylabel('quality')
plt.show()



'''
x=np.arange(9)
plt.bar(x+0.0, very_low, color='m', width=0.2, label='very_low')
plt.bar(x+0.25, most_desirable, color='g', width=0.2, label='most_desirable')
plt.bar(x+0.5, allowable, color='r', width=0.2, label='allowable')
plt.bar(x+0.75, not_permisible, color='y', width=0.2, label='not-permisible')
plt.title("Drinking Water Analysis", fontsize=20)
plt.xticks(x,elements)
plt.legend(fontsize=15)
plt.show()'''



'''
print(x)
register=list(range(9))
plt.figure(figsize=(8,5))
bar=plt.bar(register,quality,color=('m','g','y','r'))
plt.title('WATER QUALITY',fontsize=20)
plt.xticks(register,elements)
plt.legend(bar,leg,fontsize=(12))
#plt.show()
'''





'''
for i in elements:
    df.loc[count]=(i,quality[count])
    count=count+1
print(df)'''

'''
x = ['TDS', 'CA', 'MG','NA','K','CL','HCO3','SO2','NO3'] 
# corresponding y axis values 
y = [10,50,100,200,400,500,1000,1500,2000] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('elements') 
# naming the y axis 
plt.ylabel('Value') 
  
# giving a title to my graph 
plt.title('Drinking Water') 
  
# function to show the plot 
plt.show() 

'''
#mycursor.execute("create database water;")
#mycursor.execute("use water;")
#mycursor.execute('''create table data( WATER_SAMPLE varchar(20),TDS integer(5),PH integer(5),CALCIUM integer(5),MAGNESIUM integer(5), SODIUM integer(5), POTASSIUM integer(5), NITRATE integer(5),CHLORIDE integer(5), SULPHATE integer(5), FLUORIDE integer(5));''')
