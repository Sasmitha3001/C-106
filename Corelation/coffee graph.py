import numpy as np
import csv
import plotly.express as px
import pandas as pd


with open('cups of coffee vs hours of sleep.csv') as f:
    df=csv.DictReader(f)
    figure1=px.scatter(df,x='sleep in hours',y='Coffee in ml',color='week')
    figure1.show()