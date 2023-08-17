import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# if 'blood_pressure_data' not in st.session_state:
#     st.session_state.blood_pressure_data = create_empty_data()

# # Sidebar for data input
# st.sidebar.header("Enter Blood Pressure Values")
# # date = st.sidebar.date_input("Date")
# date = str(st.sidebar.date_input("Date"))
# systolic = st.sidebar.number_input("Systolic", min_value=0)
# diastolic = st.sidebar.number_input("Diastolic", min_value=0)

# if st.sidebar.button("Add Data"):
#     new_entry = pd.DataFrame()
#     new_entry["Date"] = [date]
#     new_entry["Systolic"] = [systolic]
#     new_entry["Diastolic"] = [diastolic]
#     st.session_state.blood_pressure_data = pd.concat([st.session_state.blood_pressure_data, new_entry], ignore_index=True)

# Display the stored data
conn = st.experimental_connection('db', type='sql')

# Query to retrieve all data from a specific table
query = "SELECT * FROM cardiovascular"  # Replace with your table name

# Execute the query and fetch the results
data = conn.session.execute(query).fetchall()

# Create a Pandas DataFrame from the fetched data
df = pd.DataFrame(data)

# Close the database connection
conn.session.close()

# Display the stored data
st.header("Stored Blood Pressure Data")
# st.dataframe(st.session_state.blood_pressure_data)
st.dataframe(df)

# Plot blood pressure values
st.header("Blood Pressure Trend")
if not df.empty:
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['systolic'], label='Systolic')
    ax.plot(df['date'], df['diastolic'], label='Diastolic')
    ax.set_xlabel('Date')
    ax.set_ylabel('mmHg')
    ax.set_title('Blood Pressure Trend')
    ax.legend()
    st.pyplot(fig)
else:
    st.warning("No data available for plotting.")