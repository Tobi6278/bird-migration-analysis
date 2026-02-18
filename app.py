import streamlit as st

pg = st.navigation([st.Page("home_page.py"), st.Page("dataset_page.py"), st.Page("summary_page.py"), st.Page("species_analysis_page.py")])
pg.run()