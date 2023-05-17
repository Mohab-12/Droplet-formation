#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px


# In[2]:


Kristina=pd.read_excel(r"Copy of 1-4 priedai_INPUT-OUTPT- lenteles-pvz.xlsx",
                 sheet_name='1 Kristina', header=11);

Mohab=pd.read_excel(r"Copy of 1-4 priedai_INPUT-OUTPT- lenteles-pvz.xlsx",
                 sheet_name='2 Mohab', header=11);

Lukas=pd.read_excel(r"Copy of 1-4 priedai_INPUT-OUTPT- lenteles-pvz.xlsx",
                 sheet_name='3 Lukas', header=11);

Povilas=pd.read_excel(r"Copy of 1-4 priedai_INPUT-OUTPT- lenteles-pvz.xlsx",
                 sheet_name='4 Povilas', header=11);


# In[3]:


df = st.sidebar.selectbox(label='Choose you dataset', options=['Kristina', 'Mohab', 'Lukas', 'Povilas'])

if df=='Kristina':
    df=Kristina
elif df=='Povilas':
    df=Povilas
elif df=='Lukas':
    df=Lukas
else:
    df=Mohab


# In[4]:


df.drop(axis=0, index=0, inplace=True);
df.drop(axis=0, index=61, inplace=True);
df.drop(axis=1, columns='No', inplace=True);
df.rename(columns = {'Fo':'Frequency','τ':'Time'}, inplace = True)


# In[5]:


for i in df.columns:
    df[i]= df[i].astype('float');


# In[6]:


# df[df.isna().any(axis=1)];
# df['gradTR'].fillna('0');


# In[7]:


# df.columns[2:]


# In[8]:


st.write("""
            # HEAT AND MASS TRANSFER PRCOESSES OF DROPLET
            ## The data
            """)

Column1 = st.sidebar.selectbox(label='Columns', options=df.columns[2:])
Column2 = st.sidebar.selectbox(label='Choose your domain', options=['Frequency', 'Time'])

st.write(df)

fig = px.line(x=df[Column2], y=df[Column1], title= Column1)

fig.update_layout(
        xaxis_title=Column2,
        yaxis_title=Column1)

st.write(fig)


# In[ ]:





# In[ ]:




