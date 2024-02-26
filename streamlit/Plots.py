import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

chart_data=pd.DataFrame(np.random.randn(20,3),columns=['Line-1','Line-2','Line-3'])
st.header("Charts with random number")
st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar chart")
st.bar_chart(chart_data)

#If u want to do this with matplotlib and seaborn library

st.header("Data visualization with matplotlib and seaborn")
st.subheader("Loading the DataFrame: Products.csv")
df=pd.read_csv(r'C:\Users\HP\Downloads\iris.csv')
#to display df
st.dataframe(df)

#Bar plot with matplotlib
st.subheader("Bar plot with matplotlib")
fig=plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

#Distribution plot with seaborn
st.subheader("Distribution plot with seaborn")
fig=plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

#Multiple Graphs in 1 column
st.subheader("Multiple Graphs in 1 column")
col1,col2= st.columns(2)
with col1:
    col1.header='KDE=False'
    col1.write("KDE=False")
    fig=plt.figure()
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig)

    col1.header='KDE=True'
    col1.write("KDE=True")
    fig=plt.figure()
    sns.distplot(df['sepal_length'],kde=True)
    st.pyplot(fig)

with col2:
    col2.header='Hist=False'
    col2.write("hist=False")
    fig1=plt.figure()
    sns.distplot(df['sepal_length'],hist=False)
    st.pyplot(fig1)

    col2.header='Hist=True'
    col2.write("hist=True")
    fig2=plt.figure()
    sns.distplot(df['sepal_length'],hist=True)
    st.pyplot(fig2)

# Changing the style
st.header(" Changing the style")
col1,col2= st.columns(2)
with col1:
    fig=plt.figure()
    sns.set_context('notebook')
    sns.set_style('darkgrid')
    sns.set_palette('dark')
    sns.distplot(df['petal_length'],hist=False)
    plt.tight_layout()
    st.pyplot(fig)

with col2:
    fig1=plt.figure()
    sns.set_theme(context='poster',style='darkgrid')
    sns.distplot(df['petal_length'],hist=False)
    plt.tight_layout()
    st.pyplot(fig1)

#Exploring the different graphs
    #Scatter Plot
st.header("Exploring the different graphs")
st.subheader("Scatter Plot")
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

#Count Plot
st.subheader("Count Plot")
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df ,x='species')
st.pyplot(fig)

#Box plot
st.subheader("Box plot")
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x='species',y='petal_length')
st.pyplot(fig)

#Violin plot
st.subheader("Violin plot")
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df, x='species', y='petal_length')
st.pyplot(fig)