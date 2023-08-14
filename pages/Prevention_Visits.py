import streamlit as st
import pandas as pd
from datetime import datetime

# Create or load a DataFrame to store prevention visit data
def create_empty_data():
    return pd.DataFrame(columns=['Date', 'Age', 'Sex', 'Family History', 'Risk Factors', 'Nation'])

if 'prevention_visit_data' not in st.session_state:
    st.session_state.prevention_visit_data = create_empty_data()

# Sidebar for data input
st.sidebar.header("Enter Prevention Visit Data")
date = st.sidebar.date_input("Date", datetime.today())
age = st.sidebar.number_input("Age", min_value=0, max_value=150)
sex = st.sidebar.radio("Sex", ["Male", "Female"])
family_history = st.sidebar.checkbox("Family History of Conditions")
risk_factors = st.sidebar.text_area("Risk Factors", "")
nation = st.sidebar.text_input("Nation", "")

if st.sidebar.button("Add Data"):
    st.session_state.prevention_visit_data = st.session_state.prevention_visit_data.append({
        'Date': date,
        'Age': age,
        'Sex': sex,
        'Family History': family_history,
        'Risk Factors': risk_factors,
        'Nation': nation
    }, ignore_index=True)

# Display the stored data
st.header("Stored Prevention Visit Data")
st.dataframe(st.session_state.prevention_visit_data)

# Recommendation based on age, sex, family history, risk factors, and nation
recommended_examinations = []

# Placeholder for recommendation logic
if st.session_state.prevention_visit_data.shape[0] > 1:
    recommended_examinations = ["Blood Test", "Cholesterol Screening"]

st.subheader("Recommended Examinations")
for exam in recommended_examinations:
    st.write(exam)
