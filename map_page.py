import pandas as pd
import plotly.express as px
import numpy as np

bird_data = pd.read_csv('Bird_Migration_Data_with_Origin.csv')

top_birds = bird_data.groupby('Species').head(20).reset_index(drop=True)

n = len(top_birds)

bird_data_long = pd.DataFrame({
    'Species': np.repeat(top_birds['Species'], 2),
    'Lat': np.concatenate([top_birds['Start_Latitude'].to_numpy(), top_birds['End_Latitude'].to_numpy()]),
    'Lon': np.concatenate([top_birds['Start_Longitude'].to_numpy(), top_birds['End_Longitude'].to_numpy()]),
    'Point': ['Start', 'End'] * n
})

fig = px.line_geo(
    bird_data_long,
    lat='Lat',
    lon='Lon',
    color='Species',
    line_group='Species',
    projection='natural earth'
)

fig.update_traces(mode='lines+markers')
fig.update_layout(title='Top 20 Birds per Species Migration Paths')
fig.show()
