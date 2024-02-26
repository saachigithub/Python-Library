import pandas as pd
import altair as alt
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff

#Altair scatter plot
st.header("Altair Scatter plot")
chart_data=pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
chart=alt.Chart(chart_data).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(chart)

#Interactive chart
# Line chart
df=pd.read_csv(r"C:\Users\HP\Downloads\lang_data.csv")
lang_list=df.columns.tolist()
lang_choices=st.multiselect("Choose your langauge: ",lang_list)
new_df=df[lang_choices]
st.line_chart(new_df)

#Area Chart
st.subheader("Area Plot")
st.area_chart(new_df)

#Data Visualization with plotly
st.header("Data visualization with plotly")
df=pd.read_csv(r"C:\Users\HP\Downloads\Products.csv")
st.dataframe(df.head())

#pie chart
st.subheader("Pie Chart")
fig=px.pie(df,values='ProductCost',names='Supplier')
st.plotly_chart(fig)

#pie chart with multiple parameter
st.subheader("pie chart with multiple parameter")
fig=px.pie(df,values='ProductCost',names='Supplier',opacity=0.8, 
           color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)

#Histogram
st.subheader("Histogram")
x1=np.random.randn(200)
x2=np.random.randn(200)
x3=np.random.randn(200)

hist_data=[x1,x2,x3]
grp_labels=['Grp1','Grp2','Grp3']
fig=ff.create_distplot(hist_data,grp_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)
#the small lines that are shown below the grp is the top view of the grp





