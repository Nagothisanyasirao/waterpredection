# import all nesessary libaries
import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

#load the model and sturacture
model = joblib.load("pollution_model.pkl")
model_colos = joblib.load("model_column.pkl")

#let's create and user interface
st.title("Water Pollutants Predictor")
st.write("Predict the water Pollutants based on Year and Station ID")

# user input
year_input = st.number_input("Enter Year" , min_value=2000, max_value=2100, value=2050)
station_id = st.text_input("Enter Station ID",value='1')

# to encode and then predict
if st.button('predict'):
    if not station_id:
        st.warning('please enter station ID')
    else:
        #prepare the input
        input_df = pd.DataFrame({'year': [year_input], 'id':[station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # align with model cols
        for col  in  model_colos:
            if col not in input_encoded.columns:
                input_encoded[model_colos] = 0
                input_encoded = input_encoded[model_colos]
                #predict
                predicted_pollutants = model.predict(input_encoded)[0]
                pollutants = ['02', 'NO3', 'NO2','SO4','PO4','CL']

                st.subheader(f"predicted pollutants level for the station '{station_id}' in {year_input}:")
                predicted_values = {}
                for p, val in zip(pollutants,predicted_pollutants):
                     st.write(f'{p}:{val:.2f}')
        




              

