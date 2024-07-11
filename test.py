import streamlit as st 
import pickle 


st.title( " My First App ") # web page title 

st.write('Hello, Predict your this Month expenditure and we will suggeat you Savings ')

st.image("money1.jpg")

card = st.selectbox('Pick your Card Type', ['Gold' , 'Platinum' , 'Signature' , 'Silver'])

month = st.selectbox('Pick the Month', ['January','February','MArch','April' ,'May','June',
                                'July','August','September','OCtober','November','December'])

gender = st.selectbox('Gender', ['Male','Female'])

city = st.selectbox( 'City' , ['1','2'])

st.progress(5)

# Map the values to dictionary 

Cards = {'Gold':[1,0,0,0], 'Platinum':[0,1,0,0], 'Signature':[0,0,1,0], 'Silver':[0,0,0,1]}

Genders = { 'Male':0 , 'Female':1 }



def output_user() :
    # take input and give output form ML model in Backend 
    pass

model = pickle.load( open('forest_reg.pkl' , 'rb'))

app_mode = st.siderbar.selectbox('Select PAge' , ['Predict Transaction' ,'Monthly Expenditure'])


# Only button should eb uesd with if(TRue) , no need to ceclare it sepletely 
if ( st.button('PREDICT!')) : 
    # Load the modle , give the input 
    
    sample  = [ Cards[card], 2014 , 4.0 , 0.0, Genders[gender] ] 

    prediction = model.predict( sample)
    st.success(prediction[0])
    st.image("gender_.png")


