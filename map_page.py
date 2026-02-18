import plotly.express as px
import pandas as pd

bird_data = pd.read_csv('Bird_Migration_Data_with_Origin.csv')

bird_data_long = pd.DataFrame({
    'Species': bird_data['Species'].repeat(2),
    'Lat': pd.concat([bird_data['Start_Latitude'], bird_data['End_Latitude']], ignore_index=True),
    'Lon': pd.concat([bird_data['Start_Longitude'], bird_data['End_Longitude']], ignore_index=True),
    'Point': ['Start', 'End']*len(bird_data)
})

fig = px.line_geo(
    bird_data_long,
    lat='Lat',
    lon='Lon',
    color='Species',       
    line_group='Species',  
    projection='natural earth'
)

fig.update_layout(title='Bird Migration Paths (auto-colored by species)')
fig.show()