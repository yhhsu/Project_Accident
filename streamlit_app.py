import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit_option_menu
from streamlit_option_menu import option_menu

# Import Pages
import vue_ensemble
import jeu_donnee
import dataviz
import preparation
import modelisation
import interpretation
import conclusion

df = pd.read_csv("data_preprocessed.csv")

with st.sidebar:
  selected = option_menu(
    menu_title = "Table des Matières",
    options = ["Vue d'Ensemble", "Jeu de Données", "Data Visualization", "Préparation des Données", "Modélisation", "Interprétation", "Conclusion"],
    icons = ["house", "bricks", "bar-chart-fill", "gear", "hourglass-split", "sunrise", "journal-text"], ### https://icons.getbootstrap.com/ ###
    menu_icon = "cast",
    default_index = 0,
  )

  st.write("")
  st.write("")
  st.markdown("---")  # Optional separator line
  st.markdown("### Project Members")
  st.markdown("Alassani Chakiratou AYEVA")
  st.markdown("Cédric KHONEKHAMMY")
  st.markdown("Mamadou KONATE")
  st.markdown("Yu-Hao HSU")

### Page 1 - Objectif ###
if selected == "Vue d'Ensemble":
  vue_ensemble.app()

### Page 2 - Jeu de Données ###
if selected == "Jeu de Données":
  jeu_donnee.app()

### Page 3 - Data Visualization ###
#if selected == "Data Visualization" : 
  #dataviz.app()

### Page 4 - Préparation des Données ###
if selected == "Préparation des Données" : 
  preparation.app()

### Page 5 - Modélisation ###
if selected == "Modélisation" : 
  modelisation.app()

### Page 6 - Interprétation ###
if selected == "Interprétation" : 
  interpretation.app()

### Page 7 - Conclusion ###
if selected == "Conclusion" : 
  conclusion.app()
