import streamlit as st
import pandas as pd

# Display the stored data
conn = st.experimental_connection('db', type='sql')

# Query to retrieve all data from a specific table
query = "SELECT * FROM vaccinations"  # Replace with your table name

# Execute the query and fetch the results
data = conn.session.execute(query).fetchall()

# Create a Pandas DataFrame from the fetched data
vaccinations = pd.DataFrame(data)

# Close the database connection
conn.session.close()

# if 'vaccination_data' not in st.session_state:
#     st.session_state.vaccination_data = create_empty_data()

# # Sidebar for data input
# st.sidebar.header("Enter Vaccination Data")
# date = st.sidebar.date_input("Date")
# identifier = st.sidebar.text_input("Identifier", "")
# location = st.sidebar.text_input("Location", "")
# doctor = st.sidebar.text_input("Doctor", "")

# if st.sidebar.button("Add Data"):
#     st.session_state.vaccination_data = st.session_state.vaccination_data.append({
#         'Date': date,
#         'Identifier': identifier,
#         'Location': location,
#         'Doctor': doctor
#     }, ignore_index=True)

# Display the stored data
st.header("Stored Vaccination Data")
st.dataframe(vaccinations)

# # Recommendation based on age, sex, occupation, and nation
# age = st.selectbox("Select Age", range(1, 101))
# sex = st.radio("Select Sex", ["Male", "Female"])
# occupation = st.text_input("Occupation", "")
# nation = st.text_input("Nation", "")

# # Placeholder for recommendation logic
# recommended_vaccinations = ["Vaccine A", "Vaccine B", "Vaccine C"]

# st.subheader("Recommended Vaccinations")
# for vaccine in recommended_vaccinations:
#     st.write(vaccine)
