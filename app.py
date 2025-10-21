import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Plateforme Ethnocosmétique - Huile d'Argan")

# Charger les données
data = pd.read_csv("data/huile.csv")
st.dataframe(data)

# Graphique simple
st.subheader("Teneur en acides oléiques")
plt.bar(data['Region'], data['Teneur_oleique'])
st.pyplot(plt)

