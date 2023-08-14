import streamlit as st
import pandas as pd

# Create or load a DataFrame to store doctor visit data
def create_empty_data():
    return pd.DataFrame(columns=['Date', 'Notes', 'Diagnosis', 'Treatment'])

if 'doctor_visit_data' not in st.session_state:
    st.session_state.doctor_visit_data = create_empty_data()

# Sidebar for data input
st.sidebar.header("Enter Doctor Visit Data")
date = st.sidebar.date_input("Date")
notes = st.sidebar.text_area("Notes", "")
diagnosis = st.sidebar.text_input("Diagnosis", "")
treatment = st.sidebar.text_input("Treatment", "")

if st.sidebar.button("Add Data"):
    st.session_state.doctor_visit_data = st.session_state.doctor_visit_data.append({
        'Date': date,
        'Notes': notes,
        'Diagnosis': diagnosis,
        'Treatment': treatment
    }, ignore_index=True)

# Display the stored data
st.header("Stored Doctor Visit Data")
st.dataframe(st.session_state.doctor_visit_data)

# Filter and display data based on selected date
selected_date = st.date_input("Select Date to View Details")
if not st.session_state.doctor_visit_data.empty:
    filtered_data = st.session_state.doctor_visit_data[st.session_state.doctor_visit_data['Date'] == selected_date]
    st.subheader(f"Details for {selected_date}")
    if not filtered_data.empty:
        st.write("Notes:", filtered_data.iloc[0]['Notes'])
        st.write("Diagnosis:", filtered_data.iloc[0]['Diagnosis'])
        st.write("Treatment:", filtered_data.iloc[0]['Treatment'])
    else:
        st.write("No data available for the selected date.")
