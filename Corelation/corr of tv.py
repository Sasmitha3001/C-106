import numpy as np
import csv
import plotly.express as px
import pandas as pd

def setup():
    path='Size of TV,_Average time spent watching TV in a week (hours).csv'
    plotFigure(path)
    dataSrc=getDataSrc(path)
    findCorelation(dataSrc)
    

def getDataSrc(path):
    newData,newData1=[],[]
    f=open(path)
    read=csv.DictReader(f)
    
    for i in read:
        newData.append(float(i['Size of TV']))
        newData1.append(float(i['Average time spent watching TV in a week (hours)']))

    return({
        'x':newData,
        'y':newData1
    })
    

def findCorelation(dataSrc):
    corr=np.corrcoef(dataSrc["x"],dataSrc["y"])
    print("The corelation b/w tv and watching time is: "+str(corr[0,1]))


def plotFigure(path):
    with open(path) as f:
        read=csv.DictReader(f)
        graph=px.scatter(read,x='Size of TV',y='Average time spent watching TV in a week (hours)')
        graph.show()
        
setup()
