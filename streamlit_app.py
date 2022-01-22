
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from tensorflow.keras.models import load_model
import streamlit as st

start = '2004-08-18'
end = '2022-01-20'


st.title('Predicción de tendencia de acciones')

user_input = st.text_input('Introducir cotización bursátil' , 'GOOG')

df = data.DataReader(user_input, 'yahoo', start, end)

# Describiendo los datos

st.subheader('Datos del 2004 al 2022') 
st.write(df.describe())
