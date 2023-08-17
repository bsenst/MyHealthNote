import streamlit as st
import pandas as pd

st.title("Allergy Record")

# Display the stored data
conn = st.experimental_connection('db', type='sql')

# Query to retrieve all data from a specific table
query = "SELECT * FROM allergies"  # Replace with your table name

# Execute the query and fetch the results
data = conn.session.execute(query).fetchall()

# Create a Pandas DataFrame from the fetched data
allergies = pd.DataFrame(data)

# Query to retrieve all data from a specific table
query = "SELECT * FROM treatment"  # Replace with your table name

# Execute the query and fetch the results
data = conn.session.execute(query).fetchall()

# Create a Pandas DataFrame from the fetched data
treatments = pd.DataFrame(data)

# Close the database connection
conn.session.close()

# # Collect input for allergies
# st.header("Document Allergy")
# allergy_date = st.date_input("Date of Allergy", pd.Timestamp.now())
# allergen = st.text_input("Allergen")
# reaction = st.text_input("Reaction")
# if st.button("Add Allergy"):
#     allergies_df.loc[len(allergies_df)] = [allergy_date, allergen, reaction]

# Display allergy table
st.subheader("Allergies")
st.dataframe(allergies)

# # Collect input for treatments
# st.header("Document Treatment")
# treatment_date = st.date_input("Date of Treatment", pd.Timestamp.now())
# treatment = st.text_input("Treatment")
# if st.button("Add Treatment"):
#     treatments_df.loc[len(treatments_df)] = [treatment_date, treatment]

# Display treatment table
st.subheader("Treatments")
st.dataframe(treatments)
