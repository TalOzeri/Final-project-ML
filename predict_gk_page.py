from re import I
import streamlit as st
import numpy as np
import pickle
from PIL import Image

messi = Image.open('Messi.jpg')

st.image(messi)

def Load_model():
    with open('Final_Model_GK.pkl', 'rb') as file:
        regressor = pickle.load(file)
    return regressor


regressor = Load_model()

def Show_Predict_GK_Page():
    st.image(messi)
    st.title("Fifa Goalkeepers Rating Prediction")

    st.write("""## We need some information to predict the rating""")


    goalkeeping_diving = st.slider("DIVING", 1, 99, 50)

    goalkeeping_handling = st.slider("HANDLING", 1, 99, 50)

    goalkeeping_kicking = st.slider("KICKING", 1, 99, 50)

    goalkeeping_reflexes = st.slider("REFLEXES", 1, 99, 50)

    goalkeeping_speed = st.slider("SPEED", 1, 99, 50)

    goalkeeping_positioning = st.slider("POSITIONING", 1, 99, 50)

    

    ok = st.button("Calculate Rating")

    if ok:
        X = np.array([[goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking,
         goalkeeping_positioning, goalkeeping_reflexes, goalkeeping_speed]])

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



    

    

