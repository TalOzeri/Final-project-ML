import streamlit as st
import numpy as np
import pickle



def Load_model():
    with open('Final_Model_Player.pkl', 'rb') as file:
        regressor = pickle.load(file)
    return regressor


regressor = Load_model()

def Show_Predict_Players_Page():
    st.title("Fifa Players Rating Prediction")

    st.write("""## We nedd some information to predict the rating""")



    skill_moves = st.slider("Skill Moves ⭐", 1, 5, 3)

    weak_foot = st.slider("Weak Foot 🦵", 1, 5, 3)
        
    st.write("""### PACE Stats:""")

    pace = st.slider("PACE ⚡️🏃🏻💨💨", 1, 99, 50)    

    movement_acceleration = st.slider("Acceleration", 1, 99, 50)

    movement_sprint_speed = st.slider("Sprint Speed", 1, 99, 50)


    st.write("""### SHOOTING Stats:""")

    shooting = st.slider("SHOOTING ⚽💨", 1, 99, 50)
    mentality_positioning = st.slider("Positioning", 1, 99, 50)

    attacking_finishing = st.slider("Finishing", 1, 99, 50)

    power_shot_power = st.slider("Shot Power", 1, 99, 50)

    power_long_shots = st.slider("Long Shots", 1, 99, 50)

    attacking_volleys = st.slider("Volleys", 1, 99, 50)

    mentality_penalties = st.slider("Penalties", 1, 99, 50)




    st.write("""### PASSING Stats:""")

    passing = st.slider("PASSING", 1, 99, 50)

    mentality_vision = st.slider("Vision", 1, 99, 50)

    attacking_crossing = st.slider("Crossing", 1, 99, 50)

    skill_fk_accuracy = st.slider("Free Kick Accuracy", 1, 99, 50)

    attacking_short_passing = st.slider("Short Passing", 1, 99, 50)

    skill_long_passing = st.slider("Long Passing", 1, 99, 50)

    skill_curve = st.slider("Curve", 1, 99, 50)



    st.write("""### DRIBBLING Stats:""")

    dribbling = st.slider("DRIBBLING", 1, 99, 50)

    movement_agility = st.slider("Agility", 1, 99, 50)

    movement_balance = st.slider("Balance", 1, 99, 50)

    movement_reactions = st.slider("Reactions", 1, 99, 50)

    skill_ball_control = st.slider("Ball Control", 1, 99, 50)

    skill_dribbling = st.slider("Dribbling", 1, 99, 50)

    mentality_composure = st.slider("Composure", 1, 99, 50)




    st.write("""### DEFENDING Stats:""")

    defending = st.slider("DEFENDING", 1, 99, 50)

    mentality_interceptions = st.slider("Interceptions", 1, 99, 50)

    attacking_heading_accuracy = st.slider("Heading Accuracy", 1, 99, 50)

    defending_marking_awareness = st.slider("Marking Awareness", 1, 99, 50)

    defending_standing_tackle = st.slider("Standing Tackle", 1, 99, 50)

    defending_sliding_tackle = st.slider("Sliding Tackle", 1, 99, 50)


    st.write("""### PHYSICALITY Stats:""")

    physic = st.slider("PHYSICALITY",1, 99, 50)

    power_jumping = st.slider("Jumping", 1, 99, 50)

    power_stamina = st.slider("Stamina",1, 99, 50)

    power_strength = st.slider("Strength", 1, 99, 50)


    mentality_aggression = st.slider("Aggression", 1, 99, 50)

    ok = st.button("Calculate Rating")

    if ok:
        X = np.array([[weak_foot, skill_moves, pace, shooting, passing,
       dribbling, defending, physic, attacking_crossing,
       attacking_finishing, attacking_heading_accuracy,
       attacking_short_passing, attacking_volleys, skill_dribbling,
       skill_curve, skill_fk_accuracy, skill_long_passing,
       skill_ball_control, movement_acceleration, movement_sprint_speed,
       movement_agility, movement_reactions, movement_balance,
       power_shot_power, power_jumping, power_stamina, power_strength,
       power_long_shots, mentality_aggression, mentality_interceptions,
       mentality_positioning, mentality_vision, mentality_penalties,
       mentality_composure, defending_marking_awareness,
       defending_standing_tackle, defending_sliding_tackle,]])

        rating = regressor.predict(X)
        if(rating<100):
            if(rating>85):
                st.subheader(f' You are a good player!!!\nThe estimated rating is {rating[0]:.2f}')
                st.balloons()
            else:
                st.subheader(f'The estimated rating is {rating[0]:.2f}')
                st.snow()

                
        else:
            st.subheader("you entered wrong num :(")


        
    


        


