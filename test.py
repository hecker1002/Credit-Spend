import streamlit as st 
import pickle 


st.title( " My First App ") # web page title 

st.write('Hello, Predict your this MOnth expenditure and we will suggeat you Savings ')

st.image("money1.jpg")


def imput_user() :
    # take input from user and store in dict( key-value pair 
    pass

def output_user() :
    # take input and give output form ML model in Backend 
    pass


# Only button should eb uesd with if(TRue) , no need to ceclare it sepletely 
if ( st.button('PREDICT!')) : 
    # Load the modle , give the input 
    model = pickle.load( open('forest_reg.pkl' , 'rb'))
    sample  = [ [ 1  , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,2014 , 10 , 0 , 126 ] ]
    prediction = model.predict( sample)
    st.write(prediction[0])
