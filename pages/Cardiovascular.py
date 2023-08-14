import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create or load a DataFrame to store blood pressure values
def create_empty_data():
    blood_pressure_data = pd.DataFrame()
    blood_pressure_data["Date"] = ["2023-8-08", "2023-8-09", "2023-8-10", "2023-8-11", "2023-8-12"]
    blood_pressure_data["Systolic"] = [120,135,125,140,130]
    blood_pressure_data["Diastolic"] = [80,90,70,100,90]
    return blood_pressure_data

dummy_df = create_empty_data()

if 'blood_pressure_data' not in st.session_state:
    st.session_state.blood_pressure_data = create_empty_data()

# Sidebar for data input
st.sidebar.header("Enter Blood Pressure Values")
# date = st.sidebar.date_input("Date")
date = str(st.sidebar.date_input("Date"))
systolic = st.sidebar.number_input("Systolic", min_value=0)
diastolic = st.sidebar.number_input("Diastolic", min_value=0)

if st.sidebar.button("Add Data"):
    new_entry = pd.DataFrame()
    new_entry["Date"] = [date]
    new_entry["Systolic"] = [systolic]
    new_entry["Diastolic"] = [diastolic]
    st.session_state.blood_pressure_data = pd.concat([st.session_state.blood_pressure_data, new_entry], ignore_index=True)

# Display the stored data
st.header("Stored Blood Pressure Data")
st.dataframe(st.session_state.blood_pressure_data)

# Plot blood pressure values
st.header("Blood Pressure Trend")
if not st.session_state.blood_pressure_data.empty:
    fig, ax = plt.subplots()
    ax.plot(st.session_state.blood_pressure_data['Date'], st.session_state.blood_pressure_data['Systolic'], label='Systolic')
    ax.plot(st.session_state.blood_pressure_data['Date'], st.session_state.blood_pressure_data['Diastolic'], label='Diastolic')
    ax.set_xlabel('Date')
    ax.set_ylabel('mmHg')
    ax.set_title('Blood Pressure Trend')
    ax.legend()
    st.pyplot(fig)
else:
    st.warning("No data available for plotting.")
