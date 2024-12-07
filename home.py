import streamlit as st
import pandas as pd

df = pd.read_csv('data.csv')

# Title and Styling
st.markdown(
    "<h1 style='text-align: center; color: #FF5733;'>COVID-19 Analytics</h1>", 
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size: 18px;'>"
    "Welcome to the COVID-19 Analytics Dashboard. Analyze the pandemic's global impact through interactive data visualizations and filters."
    "</p>",
    unsafe_allow_html=True
)

# Add an image
st.image(
    "https://cdn.24.co.za/files/Cms/General/d/9959/0bd64dab1ef44edbab63c488f20c6db9.jpg", 
    use_column_width=True
)

# Navigation Instruction
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>"
    "To get started, select the 'Dashboard' page from the sidebar."
    "</p>",
    unsafe_allow_html=True
)

# Highlight Key Features
st.markdown(
    """
    ### Features:
    - Interactive visualizations of COVID-19 data.
    - Filter data by region, country, and case ranges.
    - Gain insights into recovery rates, death rates, and active cases by country.
    - Visualize the pandemic's impact globally.
    - The data is from 2019-2020.
    """
)

st.sidebar.success(
    f"""
    **Summary of COVID-19 Cases**

    - **Total Confirmed Cases:** {df['Confirmed'].sum():,}
    - **Total Deaths:** {df['Deaths'].sum():,}
    - **Total Active Cases:** {df['Active'].sum():,}
    - **Total Recovered Cases:** {df['Recovered'].sum():,}
    """
)
