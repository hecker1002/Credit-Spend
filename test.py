import streamlit as st 
import pickle 


st.title( " My First App ")
st.write("Hello World")
st.image("D://Downloads//t1.png")
st.radio( 'Select any one' , ['Male' , 'Female'])
st.number_input( 'Number' , 0 , 100)
# st.button('Predict')

if ( st.button('Predict')) : 
    # Load the modle , give the input 
    model = pickle.load( open('forest_reg.pkl' , 'rb'))
    sample  = [ [ 1  , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,2014 , 10 , 0 , 126 ] ]
    model.predict( sample)
    st.write(model.predict( sample)[0])
