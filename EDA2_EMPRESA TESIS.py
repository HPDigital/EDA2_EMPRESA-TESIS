"""
EDA2_EMPRESA TESIS
"""

#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import seaborn as sns
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df=pd.read_excel('C:/Users/HP/Desktop/TESIS/EMPRESA_NDA/DATOS/DATOS_NDA.xlsx', parse_dates=True)
df['Fecha']=pd.to_datetime(df['Fecha'])
df.head()


# In[5]:


df.info()


# In[40]:


def nombredia(colfecha):
    df1=pd.Timestamp(colfecha)
    return(df1.day_name())



df['Nombredia']=df['Fecha'].apply(nombredia)


# In[ ]:





# In[ ]:





# In[43]:


sns.set(style='darkgrid')


# In[51]:


sns.relplot(x='Fecha', y = 'MontoFinalProd', data=df, kind='line', sort=True, aspect=3)


# In[50]:


sns.relplot(x='Cantidad', y = 'MontoFinalProd', data=df, col='Departamento')


# In[ ]:






if __name__ == "__main__":
    pass
