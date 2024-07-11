import streamlit as st 
import pickle 


st.title( " My First App ") # web page title 

st.write('Hello, Predict your this Month expenditure and we will suggeat you Savings ')

st.image("money1.jpg")


def imput_user() :
    # take input from user and store in dict( key-value pair) 
    pass

def output_user() :
    # take input and give output form ML model in Backend 
    pass

model = pickle.load( open('forest_reg.pkl' , 'rb'))

# Only button should eb uesd with if(TRue) , no need to ceclare it sepletely 
if ( st.button('PREDICT!')) : 
    # Load the modle , give the input 
    
    sample  = [ [1.00, 0.0, 0.0, 0.0, 2014 , 4.0 , 0.0, 1.0] ]
    prediction = model.predict( sample)
    st.write(prediction[0])
