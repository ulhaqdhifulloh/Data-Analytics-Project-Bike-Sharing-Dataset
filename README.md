# Data-Analytics-Project-Bike-Sharing-Dataset
The project I worked on while taking one of the courses at Dicoding, Learning Data Analysis with Python, in order to learn in the Bangkit 2024 Batch 2 program with the Machine Learning Path.

For the detailed analysis, you can check it out [here](https://github.com/ulhaqdhifulloh/Data-Analytics-Project-Bike-Sharing-Dataset/blob/main/Data_Analytics_Project_Bike_Sharing_Dataset.ipynb)!

### Defining Question
1. What is the trend of bicycle usage by time of day in the last two years, and when does peak usage occur?
2. How have weather conditions affected the total number of bicycle rentals over the past two years?

### Insights and Findings
1. The analysis revealed that bicycle usage shows distinct patterns throughout the day, with a notable peak during the morning and evening rush hours. Specifically, the highest rental counts occur around 8 AM to 9 AM and 5 PM to 6 PM. This trend is likely influenced by commuting behaviors, as many users rent bikes for work-related travel during these times. Conversely, usage tends to decline during the late night and early morning hours, indicating lower demand outside of typical commuting hours. The overall trend suggests that bike-sharing services are primarily utilized for transportation rather than leisure during weekdays.
2. The exploration of the impact of weather conditions on bicycle rentals highlighted significant relationships between weather variables and rental counts. Specifically, clear weather conditions (represented as weathersit = 1) correlate with higher rental counts, while adverse weather conditions such as rain or snow (weathersit = 3 and 4) significantly decrease bike rentals. Additionally, the analysis indicated that temperature also plays a crucial role, with moderate temperatures leading to increased usage. These findings suggest that weather is a critical factor influencing the behavior of bike-sharing users, emphasizing the need for operators to consider weather forecasts when managing bike availability and marketing strategies.

## Dashboard with Streamlit
### Streamlit Cloud

You can see the dashboard that I have created and deployed [here]([https://github.com/ulhaqdhifulloh/Data-Analytics-Project-Bike-Sharing-Dataset/blob/main/Data_Analytics_Project_Bike_Sharing_Dataset.ipynb](https://data-analytics-project-bike-sharing-dataset.streamlit.app/)!

This dashboard provides insights into bike rentals over the years 2011-2012.
This dashboard covers the following insights:
- Average bike rentals by day of the week
- Bike rentals distribution by season
- Bike rental trends by hour of the day
- Influence of weather conditions on rentals

<p align="center">
  <img src="/Dashboard/Dashboard_Preview.png" />

### Run Streamlit on Local

#### Install Dependencies

To install all the required libraries, open your terminal/command prompt/conda prompt, navigate to this project folder, and run the following command:

```bash
pip install -r requirements.txt
```

#### Run Dashboard
```bash
cd dashboard
streamlit run Bike_Sharing_Dashboard.py
```

Thanks for visiting my project :)
