import streamlit as st
from predict_players_page import Show_Predict_Players_Page
from predict_gk_page import Show_Predict_GK_Page
from explore_page import show_explore_page



page = st.sidebar.selectbox("Explore Or Predict", ("Predict Players","Predict Goalkeepers","Explore"))


if page == "Predict Players":
    Show_Predict_Players_Page()
elif (page == "Predict Goalkeepers"):
    Show_Predict_GK_Page()
else:
    show_explore_page()



###streamlit run app.py