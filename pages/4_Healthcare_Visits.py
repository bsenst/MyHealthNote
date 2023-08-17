import streamlit as st
import pandas as pd

# Create or load a DataFrame to store doctor visit data
def create_empty_data():
    return pd.DataFrame(columns=['Date', 'Notes', 'Diagnosis', 'Treatment'])

# if 'doctor_visit_data' not in st.session_state:
#     st.session_state.doctor_visit_data = create_empty_data()

# # Sidebar for data input
# st.sidebar.header("Enter Doctor Visit Data")
# date = st.sidebar.date_input("Date")
# notes = st.sidebar.text_area("Notes", "")
# diagnosis = st.sidebar.text_input("Diagnosis", "")
# treatment = st.sidebar.text_input("Treatment", "")

# if st.sidebar.button("Add Data"):
#     st.session_state.doctor_visit_data = st.session_state.doctor_visit_data.append({
#         'Date': date,
#         'Notes': notes,
#         'Diagnosis': diagnosis,
#         'Treatment': treatment
#     }, ignore_index=True)

# Display the stored data
st.header("Stored Doctor Visit Data")
# st.dataframe(st.session_state.doctor_visit_data)

# Display the stored data
conn = st.experimental_connection('db', type='sql')

# Query to retrieve all data from a specific table
query = "SELECT * FROM healthcarevisit"  # Replace with your table name

# Execute the query and fetch the results
data = conn.session.execute(query).fetchall()

# Create a Pandas DataFrame from the fetched data
doctor_visit_data = pd.DataFrame(data)

# Close the database connection
conn.session.close()

st.dataframe(doctor_visit_data)
