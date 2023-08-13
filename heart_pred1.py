# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:11:00 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

load_model = pickle.load(open('C:/Users/HP/Downloads/trained_model.sav', 'rb'))

def heart_disease_prediction(data):
    


    data_numpy = np.asarray(data)
    data_reshape = data_numpy.reshape(1, -1)

    prediction = load_model.predict(data_reshape)
    print(prediction)

    if (prediction[0] ==0):
      return"person does not have heart disease"

    else:
      return"person have heart disease"





def main():
    
    st.title('heart disease prediction web app')
    
  ##  Age,Sex,Chest pain type,BP,Cholesterol,FBS over 120,EKG results,Max HR,Exercise angina,ST depression,Slope of ST,Number of vessels fluro,Thallium
    Age = st.text_input('age')
    Sex = st.text_input('sex')
    Chest_pain_type   = st.text_input('chest pain type')
    BP = st.text_input('blood pressure')
    Cholesterol  = st.text_input('cholestrol')
    FBS_over_120  = st.text_input('FBS over 120')
    EKG_results  = st.text_input('EKG results')
    Max_HR = st.text_input('Max HR')
    Exercise_angina  = st.text_input('Exercise angina')
    ST_depression  = st.text_input('ST deprssion')
    Slope_of_ST   = st.text_input('slope of st')
    Number_of_vessels_fluro  = st.text_input('number of vessel fluro')
    Thallium =  st.text_input('thallium')
  
    
    diagnosis = ''
    
    
    if st.button('heart disease test result'):
        
        diagnosis =  heart_disease_prediction([ Age,Sex ,Chest_pain_type, BP , Cholesterol,  FBS_over_120 , EKG_results,  Max_HR, Exercise_angina, ST_depression,Slope_of_ST, Number_of_vessels_fluro,   Thallium   ])
    
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()