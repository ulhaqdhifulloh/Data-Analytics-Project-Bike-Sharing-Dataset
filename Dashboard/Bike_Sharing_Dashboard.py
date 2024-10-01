import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Choose Style
sns.set(style='dark')
plt.style.use('dark_background')

#Load Data
@st.cache
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/ulhaqdhifulloh/Data-Analytics-Project-Bike-Sharing-Dataset/refs/heads/main/Dashboard/all_data.csv')
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

df = load_data()

# Title and Description
st.title("Bike Sharing Data Analytics Dashboard")
st.text("This dashboard provides insights into bike rentals over the years 2011-2012.")
st.markdown("""
This dashboard covers the following insights:
- Average bike rentals by day of the week
- Bike rentals distribution by season
- Bike rental trends by hour of the day
- Influence of weather conditions on rentals
""")

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/ulhaqdhifulloh/Data-Analytics-Project-Bike-Sharing-Dataset/refs/heads/main/Dashboard/dataset-card.jpeg")

st.sidebar.header('Filter Data')
selected_year = st.sidebar.selectbox('Select Year', [2011, 2012, 'Both'])

st.sidebar.header("Visit my Profile:")

st.sidebar.markdown("Dhifulloh Dhiya Ulhaq")

col1, col2 = st.sidebar.columns(2)

with col1:
    st.markdown("[![LinkedIn](https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg)](https://www.linkedin.com/in/dhifulloh-dhiya-ulhaq-360809261/)")
with col2:
    st.markdown("[![Github](https://img.icons8.com/glyph-neue/64/FFFFFF/github.png)](https://github.com/ulhaqdhifulloh)")

# Average Bike Rentals by Weekday
st.header('Average Bike Rentals by Weekday')

def plot_bike_rentals_by_weekday():
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='weekday', y='cnt', estimator='mean', ci=None)
    plt.title('Average Bike Rentals by Weekday (0=Sunday, 6=Saturday)')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Rentals')
    st.pyplot(plt)

plot_bike_rentals_by_weekday()

# Bike Rentals Distribution by Season
st.header('Bike Rentals Distribution by Season')

def plot_bike_rentals_by_season():
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='season', y='cnt')
    plt.title('Bike Rentals Distribution by Season (1=Spring, 2=Summer, 3=Fall, 4=Winter)')
    plt.xlabel('Season')
    plt.ylabel('Total Rentals')
    st.pyplot(plt)

plot_bike_rentals_by_season()

# Bike Rental Trends by Hour of the Day
st.header('Bike Rental Trends by Hour of the Day')

def plot_bike_rentals_by_hour():
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='hr', y='cnt', estimator='mean', ci=None)
    plt.title('Average Bike Rentals by Hour of the Day')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Average Rentals')
    plt.xticks(range(0, 24))
    st.pyplot(plt)

plot_bike_rentals_by_hour()

# Bike Rentals by Weather Conditions
st.header('Bike Rentals by Weather Conditions')

def plot_bike_rentals_by_weather():
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x='weathersit', y='cnt', palette='viridis', ci=None)
    plt.title('Average Bike Rentals by Weather Condition (1=Clear, 2=Cloudy, 3=Light Snow/Rain, 4=Heavy Rain/Snow)')
    plt.xlabel('Weather Condition')
    plt.ylabel('Average Rentals')
    st.pyplot(plt)

plot_bike_rentals_by_weather()

# RFM Analysis of Bike Rentals
st.header("RFM Analysis of Bike Rentals")

def rfm_analysis(df):
    user_data = df.groupby('dteday').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum'
    }).reset_index()

    rfm_data = user_data.copy()
    current_date = df['dteday'].max()
    rfm_data['Recency'] = (current_date - rfm_data['dteday']).dt.days
    rfm_data['Frequency'] = rfm_data['cnt']
    rfm_data['Monetary'] = rfm_data['cnt']

    return rfm_data[['Recency', 'Frequency', 'Monetary']]

rfm_data = rfm_analysis(df)

# RFM Distribution Plots
st.subheader("RFM Distribution")

fig, axes = plt.subplots(3, 1, figsize=(10, 15))

sns.histplot(rfm_data['Recency'], bins=30, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution of Recency (Days since last rental)')
axes[0].set_xlabel('Recency (Days)')
axes[0].set_ylabel('Frequency')

sns.histplot(rfm_data['Frequency'], bins=30, kde=True, ax=axes[1], color='lightgreen')
axes[1].set_title('Distribution of Frequency (Total Rentals)')
axes[1].set_xlabel('Frequency (Total Rentals)')
axes[1].set_ylabel('Frequency')

sns.histplot(rfm_data['Monetary'], bins=30, kde=True, ax=axes[2], color='salmon')
axes[2].set_title('Distribution of Monetary (Total Rentals)')
axes[2].set_xlabel('Monetary (Total Rentals)')
axes[2].set_ylabel('Frequency')

st.pyplot(fig)

# RFM Heatmap
st.subheader("RFM Segmentation Heatmap")

def rfm_score(data):
    data['R_Score'] = pd.qcut(data['Recency'], 4, labels=[4, 3, 2, 1])
    data['F_Score'] = pd.qcut(data['Frequency'], 4, labels=[1, 2, 3, 4])
    data['M_Score'] = pd.qcut(data['Monetary'], 4, labels=[1, 2, 3, 4])
    return data

rfm_data = rfm_score(rfm_data)

rfm_heatmap_data = rfm_data.pivot_table(index='R_Score', columns='F_Score', values='Monetary', aggfunc='sum', fill_value=0)

plt.figure(figsize=(8, 6))
sns.heatmap(rfm_heatmap_data, annot=True, fmt='.0f', cmap='Blues', cbar_kws={'label': 'Total Rentals'})
plt.title('RFM Segmentation Heatmap')
plt.xlabel('Frequency Score')
plt.ylabel('Recency Score')
st.pyplot(plt)