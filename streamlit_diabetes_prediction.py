import pickle
import streamlit as st
import numpy as np
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

# Home page
def home_page():
    st.title('Diabetes Prediction')
    st.markdown("""<style>.reportview-container .main .block-container{padding-top: 0rem !important;}</style>""", unsafe_allow_html=True)
    st.markdown('<h1 style="text-align: center;">Diabetes Prediction</h1>', unsafe_allow_html=True)
    st.sidebar.subheader('Navigation')
    page = st.sidebar.radio('Go to', ['Home', 'Additional Features'])

    if page == 'Home':
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

        # Prediction
        if st.sidebar.button('Diabetes Prediction Test'):
            result = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
            st.sidebar.write(result)

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

    # Indian Diabetes Information
    st.subheader('Diabetes in India')
    st.write('Diabetes is a growing concern in India, with the country being called the "diabetes capital of the world". According to the International Diabetes Federation (IDF), India is home to over 77 million adults with diabetes.')

    # Indian Diet Recommendations
    st.subheader('Indian Diet Recommendations')
    st.write('Diet plays a crucial role in managing diabetes. Some dietary recommendations for Indian diabetes patients include:')
    st.write('- Emphasize whole grains such as brown rice, whole wheat, and millets.')
    st.write('- Include plenty of fiber-rich foods like fruits, vegetables, and legumes.')
    st.write('- Limit intake of refined carbohydrates and sugars.')
    st.write('- Choose healthy fats such as nuts, seeds, and olive oil.')

    # Indian Lifestyle Tips
    st.subheader('Indian Lifestyle Tips')
    st.write('In addition to diet, adopting a healthy lifestyle is essential for managing diabetes:')
    st.write('- Engage in regular physical activity such as walking, yoga, or swimming.')
    st.write('- Maintain a healthy weight by balancing calorie intake and expenditure.')
    st.write('- Monitor blood sugar levels regularly and consult healthcare professionals for guidance.')

    # User Feedback
    st.subheader('Feedback')
    feedback = st.text_area('Please provide your feedback or comments:')
    if st.button('Submit Feedback'):
        st.write('Thank you for your feedback!')

# Main function to run the app
def main():
    # Set page width to full size
    st.set_page_config(layout="wide")

    home_page()

    st.sidebar.markdown("---")
    st.sidebar.write("Developed with ADYPSOE Students")

    if st.sidebar.button('Additional Features'):
        additional_features_page()

if __name__ == "__main__":
    main()
