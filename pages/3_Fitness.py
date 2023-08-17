import streamlit as st
import pandas as pd

st.title("Physical Activity Tracker")

# Display the stored data
conn = st.experimental_connection('db', type='sql')

# Query to retrieve all data from a specific table
query = "SELECT * FROM fitness"  # Replace with your table name

# Execute the query and fetch the results
data = conn.session.execute(query).fetchall()

# Create a Pandas DataFrame from the fetched data
activity_df = pd.DataFrame(data)

# Close the database connection
conn.session.close()

# # Collect input for recording activity
# st.header("Record Activity")
# activity_date = st.date_input("Date", pd.Timestamp.now())
# exercise_modality = st.selectbox("Exercise Modality", ["Cycling", "Running"])
# exercise_duration = st.number_input("Exercise Duration (minutes)", min_value=0)
# if st.button("Record Activity"):
#     activity_df.loc[len(activity_df)] = [activity_date, exercise_modality, exercise_duration]

# Display activity records
st.subheader("Activity Records")
st.dataframe(activity_df)