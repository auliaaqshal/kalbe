# -*- coding: utf-8 -*-
"""Kalbe_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WyStUq3aFFPRbQhslcx1jLln3PcokPqR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df_transaction = pd.read_csv('/content/drive/MyDrive/Case Study - Transaction.csv', delimiter=';')
df_product = pd.read_csv('/content/drive/MyDrive/Case Study - Product.csv', delimiter=';')
df_transaction.info()
df_product.info()

df_transaction = df_transaction.astype({
    'Date': 'datetime64[ns]'
})

df_product = df_product.astype({
    'Product Name' : 'category'
})
df_transaction.info()
df_product.info()

df_merge = df_transaction.merge(df_product, how='outer', left_on='ProductID', right_on='ProductID')
df_merge.info()

df_merge.head()

df = df_merge.groupby(['Date']).agg({
    'Qty': 'sum'
})
df.info()

from statsmodels.tsa.stattools import adfuller
from numpy import log
results = adfuller(df.Qty)
print('ADF Statistic: %f' % results[0])
print('p-value: %f' % results[1])
print('Critical Values:', results[4])

plt.figure(figsize=(10, 6))
plt.plot(df)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()

import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_predict

model = ARIMA(df, order=(0,1,1))
model = model.fit()

# best_aic = float('inf')
# best_order = None
# for p in range(3):
#     for d in range(3):
#         for q in range(3):
#             try:
#                 model = ARIMA(df, order=(p,d,q))
#                 results = model.fit()
#                 aic = results.aic
#                 if aic < best_aic:
#                     best_aic = aic
#                     best_order = (p,d,q)
#                     print(best_aic)
#                     print('----------------')
#                     print(best_order)
#             except:
#                 continue

print(model.summary())

fig, ax = plt.subplots()
ax = df.loc['2022-01-01':].plot(ax=ax)

plot_predict(model, start='2022-12-01', end='2023-01-31', ax=ax,dynamic=False)
plt.show()