import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Display the stored data
conn = st.experimental_connection('db', type='sql')

# Query to retrieve all data from a specific table
query = "SELECT * FROM metabolism"  # Replace with your table name

# Execute the query and fetch the results
data = conn.session.execute(query).fetchall()

# Create a Pandas DataFrame from the fetched data
meal_glucose_data = pd.DataFrame(data)

# Close the database connection
conn.session.close()

# if 'meal_glucose_data' not in st.session_state:
#     st.session_state.meal_glucose_data = create_empty_data()

# # Sidebar for data input
# st.sidebar.header("Enter Meal and Glucose Data")
# date = st.sidebar.date_input("Date")
# meal = st.sidebar.text_input("Meal", "")
# glucose = st.sidebar.number_input("Glucose Reading", min_value=0)

# if st.sidebar.button("Add Data"):
#     st.session_state.meal_glucose_data = st.session_state.meal_glucose_data.append({
#         'Date': date,
#         'Meal': meal,
#         'Glucose': glucose
#     }, ignore_index=True)

# Display the stored data
st.header("Stored Meal and Glucose Data")
st.dataframe(meal_glucose_data)

# Plot glucose readings over time
st.header("Glucose Reading Trend")
if not meal_glucose_data.empty:
    fig, ax = plt.subplots()
    ax.plot(meal_glucose_data['date'], meal_glucose_data['glucose'], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Glucose Reading')
    ax.set_title('Glucose Reading Trend')
    st.pyplot(fig)
else:
    st.warning("No data available for plotting.")
