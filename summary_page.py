import streamlit as st
import pandas as pd

bird_data = pd.read_csv('Bird_Migration_Data_with_Origin.csv')

total_birds = round(bird_data.shape[0], 1)
num_species = bird_data['Species'].nunique()
regions_covered = bird_data['Region'].nunique()
avg_distance = bird_data['Flight_Distance_km'].mean()
avg_duration = bird_data['Flight_Duration_hours'].mean()
migration_success_rate = (bird_data['Migration_Success'] == 'Successful').mean() * 100
percent_interrupted = (bird_data['Migration_Interrupted'] == 'Yes').mean() * 100
avg_rest_stops = bird_data['Rest_Stops'].mean()

bird_summary_data = pd.DataFrame({
    "KPI": [
        "Total birds tracked",
        "Number of species",
        "Regions covered",
        "Avg flight distance (km)",
        "Avg flight duration (hrs)",
        "Migration success rate (%)",
        "% migrations interrupted",
        "Avg rest stops"
    ],
    "Value": [
        total_birds,
        num_species,
        regions_covered,
        round(avg_distance, 2),
        round(avg_duration, 2),
        round(migration_success_rate, 2),
        round(percent_interrupted, 2),
        round(avg_rest_stops, 2)
    ]
})

st.title("Overview & Key Metrics")
st.table(bird_summary_data)