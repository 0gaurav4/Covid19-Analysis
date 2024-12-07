import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset
df = pd.read_csv('data.csv')
st.success("Raw Dataset Overview")
st.dataframe(df)

# Title and Intro
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>COVID-19 Analytics Dashboard</h1>", 
    unsafe_allow_html=True
)

# Sidebar Filters
st.sidebar.markdown("<h2 style='color: #2B547E;'>Filters</h2>", unsafe_allow_html=True)
regions = df['WHO Region'].unique()
countries = df['Country/Region'].unique()

# Select WHO Region
selected_region = st.sidebar.selectbox('Select WHO Region', ['All'] + list(regions))

# Based on the WHO Region, dynamically filter the countries
if selected_region == 'All':
    selected_country = st.sidebar.selectbox('Select a Country wise', ['All'] + list(countries))
else:
    countries_in_region = df[df['WHO Region'] == selected_region]['Country/Region'].unique()
    selected_country = st.sidebar.selectbox('Select a Country wise', ['All'] + list(countries_in_region))

# Apply Filters
filtered_df = df.copy()

if selected_region != 'All':
    filtered_df = filtered_df[filtered_df['WHO Region'] == selected_region]
if selected_country != 'All':
    filtered_df = filtered_df[filtered_df['Country/Region'] == selected_country]

# Visualizations
st.markdown("## Visualizations")

# 1. Confirmed Cases by Country/Region
st.subheader(f"1. Confirmed Cases by Country - {selected_country}")
fig1 = px.bar(
    filtered_df, x='Country/Region', y='Confirmed', color='Confirmed',
    title='Confirmed Cases by Country/Region', text_auto=True
)
st.plotly_chart(fig1)

# 2. Total Deaths by Country/Region
st.subheader(f"2. Total Deaths by Country - {selected_country}")
fig2 = px.bar(
    filtered_df, x='Country/Region', y='Deaths', color='Deaths',
    title='Total Deaths by Country/Region', text_auto=True
)
st.plotly_chart(fig2)

# 3. Active Cases by WHO Region
st.subheader("3. Active Cases by WHO Region")
active_cases_by_region = df.groupby('WHO Region')['Active'].sum().reset_index()
fig3 = px.pie(
    active_cases_by_region, names='WHO Region', values='Active',
    title='Active Cases by WHO Region', color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig3)

# 4. Death Rate per 100 Cases by Country
st.subheader(f"4. Death Rate per 100 Cases by Country - {selected_country}")
fig4 = px.scatter(
    filtered_df, x='Country/Region', y='Deaths / 100 Cases', color='Deaths / 100 Cases',
    size='Deaths / 100 Cases', title='Death Rate per 100 Cases by Country'
)
st.plotly_chart(fig4)

# 5. 1 Week Change in Cases by Country
st.subheader(f"5. 1 Week Change in Cases by Country - {selected_country}")
fig5 = px.bar(
    filtered_df, x='Country/Region', y='1 week change', color='1 week change',
    title='1 Week Change in Cases by Country', text_auto=True
)
st.plotly_chart(fig5)

# 6. Deaths by WHO Region
st.subheader(f"6. Deaths by WHO Region - {selected_region}")
deaths_by_region = filtered_df.groupby('WHO Region')['Deaths'].sum().reset_index()
fig6 = px.bar(
    deaths_by_region, x='WHO Region', y='Deaths', color='Deaths',
    title='Total Deaths by WHO Region', text_auto=True
)
st.plotly_chart(fig6)

# 7. Confirmed vs Active Cases by Country
st.subheader(f"7. Confirmed vs Active Cases by Country - {selected_country}")
fig7 = px.bar(
    filtered_df, x='Country/Region', y=['Confirmed', 'Active'],
    title='Confirmed vs Active Cases by Country', barmode='group'
)
st.plotly_chart(fig7)

# 8. New Deaths vs New Recovered
st.subheader(f"8. New Deaths vs New Recovered - {selected_country} 'Country and' - {selected_region} 'WHO Region'")
fig8 = px.scatter(
    filtered_df, x='New deaths', y='New recovered', color='New deaths',
    size='New recovered', title='New Deaths vs New Recovered'
)
st.plotly_chart(fig8)

# 9. Recovery Rate by Country
st.subheader(f"9. Recovery Rate by Country - {selected_country}")
fig9 = px.choropleth(
    filtered_df, locations='Country/Region', locationmode='country names',
    color='Recovered / 100 Cases', title='Recovery Rate by Country'
)
st.plotly_chart(fig9)

# 10. Active Cases by Top 10 Countries
st.subheader(f"10. Active Cases by Top 10 Countries")
top_10_countries = df.nlargest(10, 'Active')
fig10 = px.bar(
    top_10_countries, x='Country/Region', y='Active', color='Active',
    title='Active Cases by Top 10 Countries', text_auto=True
)
st.plotly_chart(fig10)

# Conclusion
st.markdown("### Conclusion")
st.success(
    f"""
    **Summary of COVID-19 Cases**

    - **Total Confirmed Cases:** {filtered_df['Confirmed'].sum():,}
    - **Total Deaths:** {filtered_df['Deaths'].sum():,}
    - **Total Active Cases:** {filtered_df['Active'].sum():,}
    - **Total Recovered Cases:** {filtered_df['Recovered'].sum():,}
    """
)
st.warning(
    f"""
    **Key Takeaways Accross World**

    - **Most Active Cases:** {df.nlargest(1, 'Active')['Country/Region'].values[0]}
    - **Most Deaths:** {df.nlargest(1, 'Deaths')['Country/Region'].values[0]}
    - **Most Recovered:** {df.nlargest(1, 'Recovered')['Country/Region'].values[0]}
    - **Most Confirmed Cases:** {df.nlargest(1, 'Confirmed')['Country/Region'].values[0]}
    - **Most Deaths per 100 Cases:** {df.nlargest(1, 'Deaths / 100 Cases')['Country/Region'].values[0]}
    """)

