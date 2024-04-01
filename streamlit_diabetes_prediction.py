import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
model_diabetes = pickle.load(open('model_diabetes.sav', 'rb'))

# Web Title
st.title('Diabetes Prediction')

# Define a function for plotting feature distributions
def plot_distributions():
    # Sample data to display default distributions
    data = {
        'Pregnancies': [0],
        'Glucose': [0],
        'Blood Pressure': [0],
        'Skin Thickness': [0],
        'Insulin': [0],
        'BMI': [0.0],
        'Diabetes Pedigree Function': [0.0],
        'Age': [0]
    }
    df = pd.DataFrame(data)

    fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(18, 10))
    fig.suptitle('Feature Distributions', fontsize=20)

    for i, column in enumerate(df.columns):
        sns.histplot(df[column], ax=axes[i//4, i%4], kde=True, bins=20)
        axes[i//4, i%4].set_title(column)

    plt.tight_layout()
    st.pyplot(fig)

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

# Show feature distributions
st.sidebar.subheader('Feature Distributions')
if st.sidebar.button('Plot Distributions'):
    plot_distributions()

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
        else:
            st.sidebar.success('The patient does not have diabetes')
