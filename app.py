import os
import pandas as pd
import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

st.set_page_config(
    page_title="MyHealthNote"
)

st.title("Welcome to Your Health Notes")

# Specify folder containing pages
pages_folder = "pages"

# Get the alphabetically sorted filenames of the pages
pages_filenames = sorted(os.listdir(pages_folder))

# Create the page index dynamically
show_pages(
    [Page("app.py", "Home")] + [Page(f"{pages_folder}/{page}", page[:-3]) for page in pages_filenames]
)

blood_pressure_data = pd.DataFrame()
blood_pressure_data["Date"] = ["2023-8-08", "2023-8-09", "2023-8-10", "2023-8-11", "2023-8-12"]
blood_pressure_data["Systolic"] = [120,135,125,140,130]
blood_pressure_data["Diastolic"] = [80,90,70,100,90]

allergies = pd.DataFrame()
allergies["Date"] = ["2023-8-08"]
allergies["Allergen"] = ["Peanuts"]
allergies["Reaction"] = ["Hives"]

treatment = pd.DataFrame()
treatment["Date"] = ["2023-8-08"]
treatment["Treatment"] = ["Epicutaneous immunotherapy (EPIT) for peanut allergy"]

fitness = pd.DataFrame()
fitness["Date"] = ["2023-8-10", "2023-8-11", "2023-8-12"]
fitness["Exercise"] = ["Cycling", "Running", "Walking"]
fitness["Duration"] = ["115", "43", "21"]

healthcarevisit = pd.DataFrame()
healthcarevisit["Date"] = ["2023-8-11"]
healthcarevisit["Notes"] = ["Cough, Auscultatory Findings"]
healthcarevisit["Diagnosis"] = ["Lower Airway Infection"]
healthcarevisit["Treatment"] = ["Azithromycine 500 mg QD, 3 days"]

metabolism = pd.DataFrame()
metabolism['Date'] = ["2023-8-11"]
metabolism['Meal'] = ["Tuna sandwich, Water, Salad"]
metabolism['Glucose'] = ["8.3"]

prevention = pd.DataFrame()
prevention["Date"] = ["2023-7-12"]
prevention["Age"] = ["37"]
prevention["Sex"] = ["Female"]
prevention["Familyhistory"] = ["Father suffered heart attack and died with age 47"]
prevention["Riskfactors"] = ["Smoking 21 py"]

vaccinations = pd.DataFrame()
vaccinations["Date"] = ["2023-6-15"]
vaccinations["Identifier"] = ["HPV12-52-456"]
vaccinations["Healthcareprovider"] = ["Tom Smith MD"]

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.experimental_connection('db', type='sql')

# Insert some data with conn.session.
with conn.session as s:
    s.execute('CREATE TABLE IF NOT EXISTS cardiovascular (date TEXT, systolic INTEGER, diastolic INTEGER);')
    for k in blood_pressure_data.to_dict(orient="records"):
        s.execute(
            'INSERT INTO cardiovascular (date, systolic, diastolic) VALUES (:date, :systolic, :diastolic);',
            params=dict(date=k["Date"], systolic=k["Systolic"], diastolic=k["Diastolic"])
        )
    s.commit()
    s.execute('CREATE TABLE IF NOT EXISTS allergies (date TEXT, allergen TEXT, reaction TEXT);')
    for k in allergies.to_dict(orient="records"):
        s.execute(
            'INSERT INTO allergies (date, allergen, reaction) VALUES (:date, :allergen, :reaction);',
            params=dict(date=k["Date"], allergen=k["Allergen"], reaction=k["Reaction"])
        )
    s.commit()
    s.execute('CREATE TABLE IF NOT EXISTS treatment (date TEXT, treatment TEXT);')
    for k in treatment.to_dict(orient="records"):
        s.execute(
            'INSERT INTO treatment (date, treatment) VALUES (:date, :treatment);',
            params=dict(date=k["Date"], treatment=k["Treatment"])
        )
    s.commit()
    s.execute('CREATE TABLE IF NOT EXISTS fitness (date TEXT, exercise TEXT, duration TEXT);')
    for k in fitness.to_dict(orient="records"):
        s.execute(
            'INSERT INTO fitness (date, exercise, duration) VALUES (:date, :exercise, :duration);',
            params=dict(date=k["Date"], exercise=k["Exercise"], duration=k["Duration"])
        )
    s.commit()
    s.execute('CREATE TABLE IF NOT EXISTS healthcarevisit (date TEXT, notes TEXT, diagnosis TEXT, treatment TEXT);')
    for k in healthcarevisit.to_dict(orient="records"):
        s.execute(
            'INSERT INTO healthcarevisit (date, notes, diagnosis, treatment) VALUES (:date, :notes, :diagnosis, :treatment);',
            params=dict(date=k["Date"], notes=k["Notes"], diagnosis=k["Diagnosis"], treatment=k["Treatment"])
        )
    s.commit()
    s.execute('CREATE TABLE IF NOT EXISTS metabolism (date TEXT, meal TEXT, glucose TEXT);')
    for k in metabolism.to_dict(orient="records"):
        s.execute(
            'INSERT INTO metabolism (date, meal, glucose) VALUES (:date, :meal, :glucose);',
            params=dict(date=k["Date"], meal=k["Meal"], glucose=k["Glucose"])
        )
    s.commit()
    s.execute('CREATE TABLE IF NOT EXISTS prevention (date TEXT, age TEXT, sex TEXT, familyhistory TEXT, riskfactors TEXT);')
    for k in prevention.to_dict(orient="records"):
        s.execute(
            'INSERT INTO prevention (date, age, sex, familyhistory, riskfactors) VALUES (:date, :age, :sex, :familyhistory, :riskfactors);',
            params=dict(date=k["Date"], age=k["Age"], sex=k["Sex"], familyhistory=k["Familyhistory"], riskfactors=k["Riskfactors"])
        )
    s.commit()
    s.execute('CREATE TABLE IF NOT EXISTS vaccinations (date TEXT, identifier TEXT, healthcareprovider TEXT);')
    for k in vaccinations.to_dict(orient="records"):
        s.execute(
            'INSERT INTO vaccinations (date, identifier, healthcareprovider) VALUES (:date, :identifier, :healthcareprovider);',
            params=dict(date=k["Date"], identifier=k["Identifier"], healthcareprovider=k["Healthcareprovider"])
        )
    s.commit()

# Display the stored data
st.header("Stored Blood Pressure Data")
st.dataframe(blood_pressure_data.iloc[-3:])

st.header("Allergies")
st.dataframe(allergies)