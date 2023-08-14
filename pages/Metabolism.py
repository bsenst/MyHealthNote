import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create or load a DataFrame to store meal and glucose data
def create_empty_data():
    return pd.DataFrame(columns=['Date', 'Meal', 'Glucose'])

if 'meal_glucose_data' not in st.session_state:
    st.session_state.meal_glucose_data = create_empty_data()

# Sidebar for data input
st.sidebar.header("Enter Meal and Glucose Data")
date = st.sidebar.date_input("Date")
meal = st.sidebar.text_input("Meal", "")
glucose = st.sidebar.number_input("Glucose Reading", min_value=0)

if st.sidebar.button("Add Data"):
    st.session_state.meal_glucose_data = st.session_state.meal_glucose_data.append({
        'Date': date,
        'Meal': meal,
        'Glucose': glucose
    }, ignore_index=True)

# Display the stored data
st.header("Stored Meal and Glucose Data")
st.dataframe(st.session_state.meal_glucose_data)

# Plot glucose readings over time
st.header("Glucose Reading Trend")
if not st.session_state.meal_glucose_data.empty:
    fig, ax = plt.subplots()
    ax.plot(st.session_state.meal_glucose_data['Date'], st.session_state.meal_glucose_data['Glucose'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Glucose Reading')
    ax.set_title('Glucose Reading Trend')
    st.pyplot(fig)
else:
    st.warning("No data available for plotting.")
