import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Welcome")
    st.text("In this project I look into the transactions of taxis in NYC")

with dataset:
    st.header("NYC taxi dataset")
    taxi_data = pd.read_parquet("taxi_data.parquet")
    st.write(taxi_data.head())
    
with features:
    st.header("The features I created")

with model_training:
    st.header("Time to train the model")