import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt




@st.cache
def load_data():
    df = pd.read_csv("players_22.csv")

    df = df[df.club_position != 'GK']

    columns = ['overall', 'weak_foot', 'skill_moves', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing', 'attacking_finishing', 'attacking_heading_accuracy', 'attacking_short_passing', 
                 'attacking_volleys', 'skill_dribbling', 'skill_curve', 'skill_fk_accuracy', 'skill_long_passing', 'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed',
                 'movement_agility', 'movement_reactions', 'movement_balance', 'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength', 'power_long_shots', 'mentality_aggression', 'mentality_interceptions',
                 'mentality_positioning', 'mentality_vision', 'mentality_penalties', 'mentality_composure', 'defending_marking_awareness', 'defending_standing_tackle', 'defending_sliding_tackle',]
    
    df = df[columns]
    
    df.dropna(inplace=True)

    return df

df = load_data()

def show_explore_page():
    st.title("Explore FIFA Players")

    st.write(
        """
        ### FIFA 22 complete player dataset 
    """)




