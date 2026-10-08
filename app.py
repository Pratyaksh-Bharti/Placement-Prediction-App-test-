import streamlit as st
import joblib

model = joblib.load('model.pkl')

st.title('Placement Prediction App ')
st.subheader('(just for testing purposes)')

cgpa = st.number_input('Enter your CGPA:', min_value=0.0, max_value=10.0, step=0.01)
internships = st.selectbox('Number of Internships:', options=list(range(0, 3)))
projects = st.selectbox('Number of Projects:', options=list(range(0, 4)))
skills = st.slider('Number of Skills:', min_value=0, max_value=10, step=1)
communication = st.slider('Communication Skills (1-10):', min_value=1, max_value=10, step=1)

def predict_placement(cgpa, internships, projects, skills, communication):
    features = [[cgpa, internships, projects, skills, communication]]
    prediction = model.predict(features)
    return prediction[0]

if st.button('Predict Placement'):
    result = predict_placement(cgpa, internships, projects, skills, communication)
    if result == 1:
        st.success('Congratulations! You are likely to get placed.')
    else:
        st.error('Unfortunately, you may not get placed. Keep improving your skills!')
