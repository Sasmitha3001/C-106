import numpy as np
import csv
import plotly.express as px
import pandas as pd

f=open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")
read=csv.reader(f)
a=list(read)
a.pop(0)
#print(a)
newData=[]
newData1=[]

for i in range(len(a)):
    n1,n2=a[i][0],a[i][1]
    newData.append(float(n1)),newData1.append(float(n2))

corelation=np.corrcoef(newData,newData1)
print("Corelation is: ", corelation[0,1])