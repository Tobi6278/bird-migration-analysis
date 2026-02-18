import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


st.title('Bird Migration Analysis')

img = Image.open("images/migration.jpg")

st.image(img, caption="Migratory Birds in Flight", width=600)

st.markdown("An exploratory and analytical study of bird migration behavior using GPS tracking, environmental, and observational data. " \
"The analysis examines migration routes, flight distance and duration, speed and altitude profiles, and seasonal timing, " \
"alongside weather conditions, habitat type, and ecological pressures. Additional factors such as flock behavior, rest stops, " \
"predator sightings, tagging quality, and migration interruptions are analyzed to evaluate migration success and recovery outcomes. ")















































































