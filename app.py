import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('diabetes_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
    
st.title('🩺 Diabetes Prediction App')
st.write("Enter patient data to predict the likelihood of diabetes.")

# Create sidebar for user input
st.sidebar.header('Patient Data')

def user_input_features():
    preg = st.sidebar.slider('Pregnancies', 0, 17, 3)
    plas = st.sidebar.slider('Plasma Glucose', 0, 200, 120)
    pres = st.sidebar.slider('Blood Pressure', 0, 122, 70)
    skin = st.sidebar.slider('Skin Thickness', 0, 99, 20)
    test = st.sidebar.slider('Insulin Test', 0, 846, 79)
    mass = st.sidebar.slider('Body Mass Index (BMI)', 0.0, 67.1, 32.0)
    pedi = st.sidebar.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.3725)
    age = st.sidebar.slider('Age (years)', 21, 81, 29)
    
    data = {
        'preg': preg, 'plas': plas, 'pres': pres, 
        'skin': skin, 'test': test, 'mass': mass, 
        'pedi': pedi, 'age': age
    }
    features = pd.DataFrame(data, index=[0])
    return features
    
input_df = user_input_features()

st.subheader('Patient Input Data')
st.write(input_df)

if st.button('Predict'):
    prediction = model.predict(input_df)
    
    st.subheader('Prediction Result')
    if prediction[0] == 1:
        st.error('The patient is likely Diabetic.')
    else:
        st.success('The patient is likely Not Diabetic.')