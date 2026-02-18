import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px



bird_data = pd.read_csv('Bird_Migration_Data_with_Origin.csv')




st.markdown(f"<h3 style='text-align: center;'>Region & Species Analysis</h3>", unsafe_allow_html=True)
bird_selection = st.selectbox(
    "Select Species for Region Distribution:",
    (bird_data['Species'].unique())
)


bird_data = pd.read_csv('Bird_Migration_Data_with_Origin.csv')

species_counts = bird_data['Species'].value_counts().reset_index()
species_counts.columns = ['Species', 'Count']

bird_distrib = px.pie(
    species_counts,
    names='Species',
    values='Count',
    hole=0.5,
    color_discrete_sequence=px.colors.qualitative.Set3,
    title="Species Distribution"
)

species_counts = bird_data[bird_data['Species'] == bird_selection]['Region'].value_counts().reset_index()
species_counts.columns = ['Region', 'Count']

bird_distrib_region = px.pie(
    species_counts,
    names='Region',
    values='Count',
    hole=0.5,
    color_discrete_sequence=px.colors.qualitative.Set3,
    title="Bird Region Distribution"
)

distance_vs_hours = px.scatter(
    bird_data, 
    x="Flight_Distance_km", 
    y="Flight_Duration_hours",
    color="Species",          
    size="Flight_Duration_hours",  
    hover_data=["Species"],
    title="Flight Hours vs Flight Distance" 
)

distance_vs_speed = px.violin(
    bird_data,
    x="Species",
    y="Average_Speed_kmph",
    box=True,
    points=False,
    title="Species vs Average Speed",
    color="Species"
)

grouped_df = (
    bird_data
    .groupby(
        ["Weather_Condition", "Migration_Success"],
        as_index=False
    )
    .agg(mean_distance=("Flight_Distance_km", "mean"))
)

weather_impact = px.bar(
    grouped_df,
    x="Weather_Condition",
    y="mean_distance",
    color="Migration_Success",   # 👈 grouping
    barmode="group",
    title="Mean Flight Distance by Weather and Migration Success",
    labels={"mean_distance": "Mean Distance (km)"}
)

weather_impact.update_layout(
    template="plotly_white",
    bargap=0.25,
    bargroupgap=0.1,
    legend_title_text="Migration Outcome"
)




bird_distrib.update_traces(textposition='inside', textinfo='percent+label')

col1, col2 = st.columns([1, 1]) 
with col1:
    bird_distrib.update_layout(
        legend=dict(
            orientation="h",    
            yanchor="bottom",       
            y=-0.2,             
            xanchor="left",     
            x=0                 
        )
        
    )
    st.plotly_chart(bird_distrib, )

with col2:
    bird_distrib_region.update_layout(
        legend=dict(
            orientation="h",    
            yanchor="bottom",       
            y=-0.2,             
            xanchor="left",     
            x=0                 
        )
    )
    
    st.plotly_chart(bird_distrib_region, use_container_width=True)
    
st.plotly_chart(distance_vs_hours, use_container_width=True)
st.plotly_chart(distance_vs_speed, use_container_width=True)
st.plotly_chart(weather_impact, use_container_width=True)