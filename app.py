import streamlit as st
import pandas as pd


# URL con la lista de pasajeros del Titanic
# https://github.com/KeithGalli/pandas/blob/master/pokemon_data.csv


url = "https://raw.githubusercontent.com/KeithGalli/pandas/master/pokemon_data.csv"
df = pd.read_csv(url)

sorted_df = df.sort_values("HP")

st.write(sorted_df)