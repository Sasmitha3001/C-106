import numpy as np
import csv
import plotly.express as px
import pandas as pd

f=open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")
file=pd.read_csv("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")
figure=px.scatter(file,x='Temperature',y='Ice-cream Sales( ₹ )')
figure.show()

with open('cups of coffee vs hours of sleep.csv') as f:
    df=csv.DictReader(f)
    figure1=px.scatter(df,x='Coffee in ml',y='sleep in hours',color='week')
    figure.show()
