import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Bird Migration Map", layout="wide")

st.title("Bird Migration Paths")

@st.cache_data
def load_data():
    df = pd.read_csv("Bird_Migration_Data_with_Origin.csv")
    return df.dropna(subset=[
        'Start_Latitude', 'Start_Longitude',
        'End_Latitude', 'End_Longitude', 'Species'
    ])

bird_data = load_data()

top_birds = (
    bird_data
    .sort_values('Species')
    .groupby('Species')
    .head(20)
    .reset_index(drop=True)
)

bird_data_long = pd.DataFrame({
    'Species': np.repeat(top_birds['Species'].to_numpy(), 2),
    'Lat': np.ravel(
        np.column_stack((
            top_birds['Start_Latitude'].to_numpy(),
            top_birds['End_Latitude'].to_numpy()
        ))
    ),
    'Lon': np.ravel(
        np.column_stack((
            top_birds['Start_Longitude'].to_numpy(),
            top_birds['End_Longitude'].to_numpy()
        ))
    ),
    'Point': ['Start', 'End'] * len(top_birds)
})

fig = px.line_geo(
    bird_data_long,
    lat="Lat",
    lon="Lon",
    color="Species",
    projection="natural earth"
)

fig.update_traces(
    mode="lines",
    line=dict(width=2)
)

points_fig = px.scatter_geo(
    bird_data_long,
    lat="Lat",
    lon="Lon",
    color="Species",
    symbol="Point",
    projection="natural earth"
)

points_fig.update_traces(marker=dict(size=6))

for trace in points_fig.data:
    fig.add_trace(trace)

fig.update_layout(
    title="Top 20 Birds per Species Migration Paths",
    height=700,
    legend_title="Species / Point"
)

fig.update_traces(visible="legendonly")

st.plotly_chart(fig, use_container_width=True)
