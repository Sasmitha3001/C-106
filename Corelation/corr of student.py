import numpy as np
import csv
import plotly.express as px
import pandas as pd

def setup():
    path='Student Marks vs Days Present.csv'
    dataSrc=getDataSrc(path)
    findCorelation(dataSrc)
    plotFigure(path)

def getDataSrc(path):
    newData,newData1=[],[]
    f=open(path)
    read=csv.DictReader(f)
    
    for i in read:
        newData.append(float(i['Marks In Percentage']))
        newData1.append(float(i['Days Present']))

    return({
        'x':newData,
        'y':newData1
    })
    

def findCorelation(dataSrc):
    corr=np.corrcoef(dataSrc["x"],dataSrc["y"])
    print("The corelation b/w marks and attendance is: "+str(corr[0,1]))


def plotFigure(path):
    with open(path) as f:
        read=csv.DictReader(f)
        graph=px.scatter(read,x='Marks In Percentage',y='Days Present',color='Roll No')
        graph.show()
        
setup()
