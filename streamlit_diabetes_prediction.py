import pickle
import streamlit as st
import numpy as np
import pandas as pd
import time

# Load model
model_diabetes = pickle.load(open('model_diabetes.sav', 'rb'))

# Define a function for prediction
def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age):
    if pregnancies == 0 or glucose == 0 or blood_pressure == 0 or skin_thickness == 0 or insulin == 0 or bmi == 0.0 or diabetes_pedigree_function == 0.0 or age == 0:
        return "Please fill in all the fields."
    elif glucose > 200 and blood_pressure > 150:
        return "Please check glucose and blood pressure values, they seem high. Consult a healthcare professional."
    else:
        diabetes_prediction = model_diabetes.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        if diabetes_prediction[0] == 1:
            return 'The patient has diabetes'
        else:
            return 'The patient does not have diabetes'

# Function to save feedback to a CSV file
def save_feedback(feedback):
    feedback_df = pd.DataFrame({'Feedback': [feedback]})
    feedback_df.to_csv('feedback.csv', mode='a', index=False, header=not st.session_state.feedback_saved)

# Additional Features page
def additional_features_page():
    st.title('Additional Features')

    # Display Model Information
    st.write('**Model Information:**')
    st.write('- Model Name: Diabetes Prediction Model')
    st.write('- Model Type: Logistic Regression')
    st.write('- Accuracy: 85%')

    # Include External Resources
    st.write('**External Resources:**')
    st.write('- [American Diabetes Association](https://www.diabetes.org)')
    st.write('- [National Institute of Diabetes and Digestive and Kidney Diseases](https://www.niddk.nih.gov)')

    # Diabetes Awareness
    st.subheader('Diabetes Awareness')
    st.write('It\'s important for individuals to be aware of diabetes and its impact on health. Some key points to consider include:')
    st.write('- Diabetes is a chronic condition that affects how the body processes blood sugar (glucose).')
    st.write('- There are different types of diabetes, including Type 1, Type 2, and gestational diabetes.')
    st.write('- Diabetes can lead to serious health complications such as heart disease, stroke, kidney failure, and blindness if not properly managed.')
    st.write('- Early detection and management of diabetes through lifestyle changes, medication, and regular monitoring can help prevent complications.')

    # User Feedback
    st.subheader('Feedback')
    feedback = st.text_area('Please provide your feedback or comments:')
    if st.button('Submit Feedback'):
        save_feedback(feedback)
        st.write('Thank you for your feedback!')

# Main function to run the app
def main():
    # Set page width to full size
    st.set_page_config(layout="wide")

    additional_features_page()

    st.sidebar.markdown("---")
    st.sidebar.write("Developed with ❤️ by Your Name")

if __name__ == "__main__":
    main()
