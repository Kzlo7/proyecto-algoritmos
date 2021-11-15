##proyecto inicio 05-11-2021
from pandas.core.indexing import _iLocIndexer
import requests
import pandas as pd
"""l1=pd.read_excel("esta.xlsx")
asd1=l1.columns.array
xx=[]
for j in asd1:
    xx.append(j)
print(xx)"""


"""k1="AIzaSyD_VKKZ2ZyZIJ9DaBto4IpK2Z8lj2HInJ0"

url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Metro%Einstein&destinations=Metro%Zapadores&key=AIzaSyD_VKKZ2ZyZIJ9DaBto4IpK2Z8lj2HInJ0"


response = requests.get(url).json()

ll=response["rows"][0]
l1=ll["elements"][0]
print(l1["distance"]["value"])
import pandas as pd"""
ññ=["dsad",1,2,3]
l1=pd.read_excel("metro1.xlsx")
"""asd1=l1.columns.array
xx=[]

for j in asd1:
    xx.append(j)
xx.pop(0)
for i in range(0,len(xx)):
    for j in range(0,len(xx)):
        if(xx[i]==xx[j]):
            break
            
        #print("la estacion"+str(xx[i]))
        #print("Con destino"+str(xx[j]))
"""   
#for i in range(0,len(xx)-1):
as1=l1.iat[0,1]

print(as1)  
l1.iat[0,1]=132
print(as1)
    
#el numero 1 representa el indice 0 de xx
asd2=l1.iloc[118][1]#representa la estacion de inicio

#print(asd2)

l1.iloc[118][1]=123

#print(l1.iloc[118][1])
"""xx=[]


for j in asd1:
    xx.append(j)

xx.pop(0)
print(xx)
grafo=[]"""
"""for k in xx:
    t1=l1[k]
    t2=[]
    for j in t1:
        t2.append(j)
    grafo.append(t2)
print(grafo)"""
"""MAX_value = 999999

l1=pd.read_excel("kk.xlsx")

asd1=l1.columns.array

xx=[]


for j in asd1:
    xx.append(j)

xx.pop(0)

grafo=[]
for k in xx:
    t1=l1[k]
    t2=[]
    for j in t1:
        t2.append(j)
    grafo.append(t2)
print(grafo)"""

#print("holaaa")






