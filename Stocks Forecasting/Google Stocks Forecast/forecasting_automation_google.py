# -*- coding: utf-8 -*-
"""Forecasting_Automation_Google

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OEsn8HSSldvYsecrCPHC7rqZb_-Ap_Ri
"""

from prophet import Prophet
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='colab'

df=pd.read_csv("GOOG.csv")
df

df.info()

df.describe()

px.area(df, x="Date", y="Close")

px.area(df, x="Date", y="Volume")

px.line(df, x="Date", y="Close")

px.bar(df, y='Volume')

px.bar(df, y='Close')

columns = ['Date','Close']
ndf = pd.DataFrame(df, columns=columns)
ndf

prophet_df = ndf.rename(columns={'Date':'ds', 'Close':'y'})
prophet_df

m=Prophet()
m.fit(prophet_df)

future=m.make_future_dataframe(periods=30)
forecast=m.predict(future)
forecast

px.line(forecast, x='ds', y='yhat')

from matplotlib import figure
figure=m.plot(forecast, xlabel='ds', ylabel='y')

figure_2 = m.plot_components(forecast)

from google.colab import files
forecast.to_csv('forecast.csv')
files.download('forecast.csv')