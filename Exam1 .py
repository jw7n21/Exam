#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


# **Download Monthly Stock Price Data**

# Utilizing the yfinance library to fetch Walmart stock data between specified dates.

# In[2]:


wmt_stock_data = yf.download('WMT', start='2015-01-01', end='2019-12-31', interval='1mo')


# **Calculate Monthly Log Returns**

# In[3]:


wmt_stock_data['Log_Returns'] = np.log(wmt_stock_data['Adj Close'] / wmt_stock_data['Adj Close'].shift(1))


# **Calculate Annualised Return**

# In[4]:


annualized_return = wmt_stock_data['Log_Returns'].mean() * 12


# **Calculate Annualised Volatility**

# In[5]:


annualized_volatility = wmt_stock_data['Log_Returns'].std() * np.sqrt(12)


# In[6]:


print(f'Annualized Return: {annualized_return * 100:.2f}%')
print(f'Annualized Volatility: {annualized_volatility * 100:.2f}%')


# **Download ESG Data and Handle Missing Values** 

# In[7]:


pip install yesg


# In[20]:


import yesg


# In[21]:


ESG = yesg.get_historic_esg('WMT')
ESG


# In[22]:


ESG.new = pd.DataFrame.dropna(ESG)
ESG.new


# In[23]:


ESG_new_filtered = ESG.new['2015-01-01':'2019-12-31']


# **Plot for ESG Score**

# In[26]:


ESG_new_filtered[['E-Score', 'S-Score', 'G-Score','Total-Score']].plot(kind='line', figsize=(10, 5))
plt.title('ESG Scores from 2015 to 2019')
plt.xlabel('Date')
plt.ylabel('Scores')
plt.show()


# # Question 2 

# **Climate Analysis Based on Beijing in May,2022

# In[9]:


import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily


# setting the time period

# In[10]:


start = datetime(2022, 5, 1)
end = datetime(2022, 5, 31)


# specifying the location 

# For this analysis, we'll focus on Beijing, China. The geographical coordinates (latitude, longitude, and altitude) for Beijing are provided to the Point class:

# In[11]:


location = Point(39.9042, 116.4074, 43.5)


# Fetching the Daily Data
# 
# Using the specified location and time range, we fetch the daily weather data:

# In[12]:


data = Daily(location, start, end)
data = data.fetch()


# Calculating Cooling Degree Days (CDD)
# 

# In[13]:


T_base = 18
cdds = [max(temp - T_base, 0) for temp in data.tavg]


# In[14]:


cdds


# In[ ]:




