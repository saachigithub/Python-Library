import streamlit as st
import pandas as pd
st.subheader("Uploading the csv file")

#there are 2 ways to it:
#1. file_uploader
df1 =st.file_uploader("Upload the file: ")
df2 =st.file_uploader("Upload the csv file: ",type=['csv','xlsx'])

#to show the file 
#if df2 is not None:
 #   st.dataframe(df2)
# st.table(df2)

#to display the file in the same format with the help of pandas
st.subheader('Loading the CSV File')
df2=pd.read_csv(r"C:\Users\HP\Downloads\Products.csv")
# st.table(df2)
if df2 is not None:
    st.table(df2.head())

#Dealing with images directly
#there are 2 ways to do it
#1st way
st.subheader("Dealing with images")

st.image(r"\Users\HP\Downloads\img.png")


# 2nd way
img=st.file_uploader("Upload the image file: ",type=['png','jpeg','jpg'])

#Dealing with images while uploading
st.subheader("Dealing with images while uploading")
if img is not None:
    st.image(img)

# Working with videos
st.subheader("Working with videos")
vid=st.file_uploader("Upload the video file: ",type=['mkv','mp4'])
if vid is not None:
    st.video(vid)

# Working with audio
st.subheader("Working with audio")
aud=st.file_uploader("Upload the audio file: ",type=['wav','mp3'])
if aud is not None:
    st.audio(aud.read())



