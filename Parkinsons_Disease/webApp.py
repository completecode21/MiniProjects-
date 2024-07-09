# -*- coding: utf-8 -*-
import streamlit as st
import joblib
import numpy as np


model = joblib.load('Parkinsons_Disease/Parkinsons_Model')

st.title('Parkinson Disease Prediction')
col1, col2, col3, col4, col5 = st.columns(5)


with col1:
        fo = st.text_input("MDVP: Fo(Hz)")
        
with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
with col3:
        flo = st.text_input('MDVP: Flo(Hz)')      
        
with col4:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        # Jitter_abs_float = convert_scientific_to_float(Jitter_Abs_str)

with col5:
        PPQ = st.text_input("MDVP: PPQ")
        
with col1:
        DDP = st.text_input('Jitter: DDP')
        
with col2:
        Shimmer = st.text_input('MDVP: Shimmer')       
        
with col3:
        APQ3 = st.text_input('Shimmer: APQ3')
        
with col4:
        APQ5 = st.text_input('Shimmer: APQ5')
        
with col5:
        APQ = st.text_input('MDVP: APQ')
        
with col1:
        NHR = st.text_input('NHR')
        
with col2:
        HNR = st.text_input('HNR')
        
with col3:
        RPDE = st.text_input('RPDE')
        
with col4:
        DFA = st.text_input('DFA')
        
with col5:
        spread1 = st.text_input('spread1')
        
with col1:
        spread2 = st.text_input('spread2')
        
with col2:
        D2 = st.text_input('D2')
        

# code for Prediction
parkinsons_diagnosis = ''
    
# creating a button for Prediction    
if st.button("Parkinson's Test Result"):
    features = [fo, fhi, flo, Jitter_Abs, PPQ,DDP,Shimmer,APQ3,APQ5,APQ,NHR,HNR,RPDE,DFA,spread1,spread2,D2]
    input_data = np.array(features).reshape(1,-1)
    parkinsons_prediction = model.predict(input_data)                          

    if (parkinsons_prediction[0] == 1):
        parkinsons_diagnosis = "The person has Parkinson's disease"
    else:
        parkinsons_diagnosis = "The person does not have Parkinson's disease"

st.success(parkinsons_diagnosis)