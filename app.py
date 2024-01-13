import streamlit as st
import pandas as pd
import pickle

model=pickle.load(open('model.pkl','rb'))

st.title("Water Quality Prediction")

pH=st.text_input("Enter the pH value:")
H=st.text_input("Enter the Hardness value:")
S=st.text_input("Enter the Solids value:")
Ch=st.text_input("Enter the Chloramines value:")
Su=st.text_input("Enter the Sulfate value:")
Co=st.text_input("Enter the Conductivity value:")
Oc=st.text_input("Enter the Organic_carbon value:")
T=st.text_input("Enter the Trihalomethanes value:")
Tur=st.text_input("Enter the Turbidity value:")


if st.button('Predict'):
    pH=float(pH)
    H=float(H)
    S=float(S)
    Ch=float(Ch)
    Su=float(Su)
    Co=float(Co)
    Oc=float(Oc)
    T=float(T)
    Tur=float(Tur)

    data=[[pH,H,S,Ch,Su,Co,Oc,T,Tur]]
    result=model.predict(data)
    st.success(result)

    if result[0]==0:
        st.write("Unfit for Drinking")
    else:
        st.write("Set For Drinking Water")