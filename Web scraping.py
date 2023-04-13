#!/usr/bin/env python
# coding: utf-8

# In[1]:


#INSTALL PACKAGES


# In[2]:




pip install beautifulsoup4


# In[3]:


pip install requests


# In[4]:


#IMPORT PACKAGES


# In[5]:


import requests
import csv


# In[6]:


from bs4 import BeautifulSoup


# In[7]:


import pandas as pd


# In[8]:


req = requests.get('https://esportsparra.com/collections/zapatillas-running-hombre')

soup = BeautifulSoup(req.text, "html.parser")


# In[9]:


soup.title


# In[10]:


soup.title.string


# In[11]:


product_names = soup.find_all('div','grid-product__title')


# In[12]:


print(product_names)


# In[13]:



product_names = [elem.text.strip() for elem in soup.find_all('div', {'class': 'grid-product__title'})]

print(product_names)


# In[14]:


original_prices = soup.find_all('del','grid-product__price--original')


# In[15]:


print(original_prices)


# In[16]:


original_prices = [elem.text.strip() for elem in soup.find_all('del', {'class': 'grid-product__price--original'})]

print(original_prices)


# In[17]:


sale_price = soup.find_all('span','sale-price')
print(sale_price)


# In[18]:


sale_price = [elem.text.strip() for elem in soup.find_all('span', {'class': 'sale-price'})]

print(sale_price)


# In[19]:


print(len(product_names))
print(len(sale_price))
print(len(original_prices))


# In[20]:


if len(sale_price) < len(product_names):
    diff = len(product_names) - len(sale_price)
    for i in range(diff):
        sale_price.append(None)

if len(original_prices) < len(product_names):
    diff = len(product_names) - len(original_prices)
    for i in range(diff):
        original_prices.append(None)

# Update data dictionary with the new lists
data = {'Product': product_names, 'Price with discount': sale_price, 'Original Price': original_prices}

# Create the DataFrame
df = pd.DataFrame(data)


# In[21]:


print(df)


# In[22]:


# Save the DataFrame to a CSV file
df.to_csv('product_data.csv', index=False)


# In[ ]:




