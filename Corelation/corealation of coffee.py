import numpy as np
import csv
import plotly.express as px
import pandas as pd

def setup():
    path='cups of coffee vs hours of sleep.csv'
    dataSrc=getDataSrc(path)
    findCorelation(dataSrc)
    plotFigure(path)

def getDataSrc(path):
    newData,newData1=[],[]
    f=open(path)
    read=csv.DictReader(f)
    
    for i in read:
        newData.append(float(i['Coffee in ml']))
        newData1.append(float(i['sleep in hours']))

    return({
        'x':newData,
        'y':newData1
    })
    

def findCorelation(dataSrc):
    corr=np.corrcoef(dataSrc["x"],dataSrc["y"])
    print("The corelation b/w coffee and sleep is: "+str(corr[0,1]))


def plotFigure(path):
    with open(path) as f:
        read=csv.DictReader(f)
        graph=px.scatter(read,x='Coffee in ml',y='sleep in hours',color='week')
        graph.show()
        
setup()