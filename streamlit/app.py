#to run this program open cmd and type: streamlit run file_path_by draging_the file_to_cmd
import streamlit as st
st.title('This is title Hello World bye')
st.header('Header-> hi')
st.subheader('Subheader-> Hi')
st.text('Text->Hi')
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('Hi')

st.success('Data is submitted')
st.info('Information')
st.warning('Warning')
st.error('error')

st.exception(ZeroDivisionError('Division is not possible with zero'))
#Help will documentation
st.help(ZeroDivisionError)
st.write("range(1,10)")
st.write(1+2+3)
# If u want to write code that can be copied
# Checkbox with validation
st.code('x=10\n'
        'for i in range(x):\n'
        '\tprint(i)')
#checkbox in this we select multiple option
st.checkbox('Male')
st.checkbox('Female')

#radio
st.radio('Select: ' ,('Check','Uncheck'))
#only one option we can choose
radiobutton=st.radio('Select:',('Male','Female','Other'))
if(radiobutton=='Male'):
    st.write("You're a male")
elif(radiobutton=='Female'):
    st.write("You'r a female")
elif(radiobutton=='Other'):
    st.write("You'r a other gender")

#selectbox
st.subheader("Select Box")

selectBox= st.selectbox("Data Science:",['Data Analysis','Web scraping','Machine Learning','Deep learning',
                             'Natural Learning Processing','Image Processing','Computer vision'])
st.write("You have selected:",selectBox)

#Multiselect
st.subheader("Multiselectbox")
multiselectBox=st.multiselect( "Data Science:",['Data Analysis','Web scraping','Machine Learning','Deep learning',
                             'Natural Learning Processing','Image Processing','Computer vision'])
st.write("YOu have selected", len(multiselectBox),"courses",multiselectBox)

#button
st.subheader("Button")
#st.button("Click me")
if(st.button('Click me')):
    st.write("Thanks for clicking me")

#slider
st.subheader("Slider")
vol=st.slider("Select volume: ",0,100,step=1)
st.write("volume is: ",vol)

#Text user input
st.subheader('User input:text_input')
name=st.text_input("Name: ")
st.write()

surname=st.text_input("Surname: ")
if(surname):
    st.write("Hi", name," ",surname)

# for writing password
psswrd=st.text_input("Password: ", type='password')

# text_area
st.subheader("text_area")
textarea=st.text_area("Write something about yourself: ")
st.write(textarea)

#input the number
st.subheader("Input number: number_input")
st.number_input("Enter your age: ")
st.number_input("Parents age: ",20,110)

#date_input
st.date_input("Birthday date: ")

#time_input
st.time_input("Time: ")

