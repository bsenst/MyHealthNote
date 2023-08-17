import streamlit as st
import pandas as pd
from datetime import datetime

# Display the stored data
conn = st.experimental_connection('db', type='sql')

# Query to retrieve all data from a specific table
query = "SELECT * FROM prevention"  # Replace with your table name

# Execute the query and fetch the results
data = conn.session.execute(query).fetchall()

# Create a Pandas DataFrame from the fetched data
prevention_visit_data = pd.DataFrame(data)

# Close the database connection
conn.session.close()

# if 'prevention_visit_data' not in st.session_state:
#     st.session_state.prevention_visit_data = create_empty_data()

# # Sidebar for data input
# st.sidebar.header("Enter Prevention Visit Data")
# date = st.sidebar.date_input("Date", datetime.today())
# age = st.sidebar.number_input("Age", min_value=0, max_value=150)
# sex = st.sidebar.radio("Sex", ["Male", "Female"])
# family_history = st.sidebar.checkbox("Family History of Conditions")
# risk_factors = st.sidebar.text_area("Risk Factors", "")
# nation = st.sidebar.text_input("Nation", "")

# if st.sidebar.button("Add Data"):
#     st.session_state.prevention_visit_data = st.session_state.prevention_visit_data.append({
#         'Date': date,
#         'Age': age,
#         'Sex': sex,
#         'Family History': family_history,
#         'Risk Factors': risk_factors,
#         'Nation': nation
#     }, ignore_index=True)

# Display the stored data
st.header("Stored Prevention Visit Data")
st.dataframe(prevention_visit_data)

# Recommendation based on age, sex, family history, risk factors, and nation
recommended_examinations = []

# Placeholder for recommendation logic
if prevention_visit_data.shape[0] > 1:
    recommended_examinations = ["Blood Test", "Cholesterol Screening"]

st.subheader("Recommended Examinations")
for exam in recommended_examinations:
    st.write(exam)
