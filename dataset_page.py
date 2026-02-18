import streamlit as st
import pandas as pd

bird_data = pd.read_csv('Bird_Migration_Data_with_Origin.csv')
bird_data = bird_data.sort_values(by=['Species', 'Region'])
st.title("Bird Immigration Dataset")
st.dataframe(bird_data, use_container_width=True)