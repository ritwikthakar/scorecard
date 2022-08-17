#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.express as px



# In[2]:


df = pd.read_csv('testfile.csv')


# In[31]:





# In[ ]:

team_code = list(df['Team_Code'].drop_duplicates())
Adivsor = list(df['Adivsor'])

# Sidebar - title & filters
st.sidebar.markdown('### Data Filters')
t_code = st.sidebar.multiselect(
    'Choose Team:', team_code, default=team_code)
advisor = st.sidebar.multiselect(
    "Choose Planner:", Adivsor, default=Adivsor)


df = df[df['Team_Code'].isin(t_code)]
df = df[df['Adivsor'].isin(advisor)]


# Main
st.title("Scorecard")

# Main - dataframes
st.markdown('### Advisors Scorecard')

st.dataframe(df.sort_values('Volume',
             ascending=False))

fig = px.bar(df, x=df['Adivsor'], y = df['Unit Target'], title='Units Scorecard', labels='Adivsor')
fig.add_bar(x=df['Adivsor'], y = df['Units'])
fig.update_layout(barmode='overlay', bargap=0.70)


# In[32]:


fig1 = px.bar(df, x=df['Adivsor'], y = df['Plan Target'], title='Plan Scorecard', labels='Adivsor')
fig1.add_bar(x=df['Adivsor'], y = df['Approved Plans'])
fig1.update_layout(barmode='overlay', bargap=0.70)



# In[33]:


fig2 = px.bar(df, x=df['Adivsor'], y = df['Volume Target'], title='Volume Scorecard', labels='Adivsor')
fig2.add_bar(x=df['Adivsor'], y = df['Volume'])
fig2.update_layout(barmode='overlay', bargap=0.70)



# In[35]:


fig3 = px.pie(df, values='Units', names='Adivsor', title='Units Contribution')


# In[37]:


fig4 = px.pie(df, values='Approved Plans', names='Adivsor', title='Plan Contribution')


# In[38]:


fig5 = px.pie(df, values='Volume', names='Adivsor', title='Volume Contribution')


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Units Vs Target", "Plans Vs Target", "Volume Vs Target", "Units", "Plans", "Volume"])

with tab1:
    st.header("Units Vs Target")
    st.plotly_chart(fig)

with tab2:
    st.header("Plans Vs Target")
    st.plotly_chart(fig1)

with tab3:
    st.header("Volume Vs Target")
    st.plotly_chart(fig2)

with tab4:
    st.header("Units")
    st.plotly_chart(fig3)

with tab5:
    st.header("Plans")
    st.plotly_chart(fig4)

with tab6:
    st.header("Volume")
    st.plotly_chart(fig5)
