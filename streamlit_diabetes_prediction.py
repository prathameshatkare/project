import pickle
import streamlit as st
import numpy as np
import time

# Load model
model_diabetes = pickle.load(open('model_diabetes.sav', 'rb'))

# Web Title
st.title('Diabetes Prediction')

# Sidebar
st.sidebar.subheader('About')
st.sidebar.write('This app predicts the likelihood of diabetes based on various health parameters.')

# Input fields with validation
st.sidebar.subheader('Enter Patient Details')
with st.sidebar:
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, step=1)
    glucose = st.number_input('Glucose', min_value=0, max_value=300, step=1)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200, step=1)
    skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1)
    insulin = st.number_input('Insulin', min_value=0, max_value=1000, step=1)
    bmi = st.number_input('BMI', min_value=0.0, max_value=60.0, step=0.1)
    diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, step=0.01)
    age = st.number_input('Age', min_value=0, max_value=120, step=1)

# Animated element
st.subheader('Waiting for prediction...')
progress_bar = st.progress(0)

# Fake prediction process
for i in range(101):
    time.sleep(0.05)
    progress_bar.progress(i)

# Prediction
if st.sidebar.button('Diabetes Prediction Test'):
    if pregnancies == 0 or glucose == 0 or blood_pressure == 0 or skin_thickness == 0 or insulin == 0 or bmi == 0.0 or diabetes_pedigree_function == 0.0 or age == 0:
        st.sidebar.error("Please fill in all the fields.")
    elif glucose > 200 and blood_pressure > 150:
        st.sidebar.error("Please check glucose and blood pressure values, they seem high. Consult a healthcare professional.")
    else:
        diabetes_prediction = model_diabetes.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        
        if diabetes_prediction[0] == 1:
            st.sidebar.success('The patient has diabetes')
            st.subheader('Personalized Recommendations')
            st.write('It is recommended to consult a healthcare professional for further evaluation and management.')
        else:
            st.sidebar.success('The patient does not have diabetes')
            st.subheader('Healthy Lifestyle Tips')
            st.write('Maintain a balanced diet, engage in regular physical activity, and monitor your blood sugar levels regularly.')

# Additional Features
st.subheader('Additional Features')

# Display Model Information
st.write('**Model Information:**')
st.write('- Model Name: Diabetes Prediction Model')
st.write('- Model Type: Logistic Regression')
st.write('- Accuracy: 85%')

# Include External Resources
st.write('**External Resources:**')
st.write('- [American Diabetes Association](https://www.diabetes.org)')
st.write('- [National Institute of Diabetes and Digestive and Kidney Diseases](https://www.niddk.nih.gov)')

# User Feedback
st.subheader('Feedback')
feedback = st.text_area('Please provide your feedback or comments:')
if st.button('Submit Feedback'):
    st.write('Thank you for your feedback!')

# Footer

